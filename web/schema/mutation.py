import graphene
from graphene import relay, Node

from web.models import Comment, Answer, Question, Tag
from web.schema.nodes import CommentNode, QuestionNode, AnswerNode, TagNode
from django.contrib.auth.models import User

__all__ = ['Mutations']


class CreateQuestion(relay.ClientIDMutation):
    class Input:
        text = graphene.String(required=True)
        owner_id = graphene.String(required=True)

    question = graphene.Field(lambda: QuestionNode)

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        owner_id = input.get('owner_id')
        text = input.get('text')

        try:
            _type, owner_pk = Node.from_global_id(owner_id)
        except Exception as e:
            raise Exception('Received wrong User id: {}'.format(owner_id))
        if _type != 'UserNode':
            raise Exception('The owner id must be from a valid User and not {}'.format(_type))

        question = QuestionNode._meta.model(text=text,
                                            owner_id=owner_pk)
        question.save()
        return CreateQuestion(question=question)


class CreateAnswer(relay.ClientIDMutation):
    """
    Creates an Answer object that is related to a single Question object. Answer objects are required
    to be attached to a Question
    """

    class Input:
        text = graphene.String()
        owner_id = graphene.String(required=True)
        question_id = graphene.String(required=True)

    answer = graphene.Field(lambda: AnswerNode)

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        owner_id = input.get('owner_id')
        text = input.get('text')
        question_id = input.get('question_id')

        _, owner_pk = Node.from_global_id(owner_id)
        _, question_pk = Node.from_global_id(question_id)

        answer = AnswerNode._meta.model(text=text,
                                        owner_id=owner_pk,
                                        question_id=question_pk)
        answer.save()
        return CreateAnswer(answer=answer)


class CreateComment(relay.ClientIDMutation):
    """
    This mutation is for a generic comment that has to be attached to an Answer or Question object.
    """

    class Input:
        text = graphene.String(required=True)
        owner_id = graphene.String(required=True)
        question_id = graphene.String()
        answer_id = graphene.String()

    comment = graphene.Field(lambda: CommentNode)

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        text = input.get('text')
        owner_id = input.get('owner_id')
        _, owner_pk = Node.from_global_id(owner_id)
        question_id = input.get('question_id', None)
        answer_id = input.get('answer_id', None)

        if question_id and answer_id:
            raise Exception('A comment can only be associated with either a question or an answer, not both')

        if question_id:
            _, question_pk = Node.from_global_id(question_id)
            comment = CommentNode._meta.model(text=text, owner_id=owner_pk, question_id=question_pk)
        elif answer_id:
            _, answer_pk = Node.from_global_id(answer_id)
            comment = CommentNode._meta.model(text=text, owner_id=owner_pk, answer_id=answer_pk)

        comment.save()

        return CreateComment(comment=comment)


class EditPostMixin(object):
    """
    A mixin that allows shared use of the `mutate_and_get_payload` method to all mutations that edit the text of
    a Comment, Question, or Answer object.
    """

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        post_cls = cls.post_cls
        field_name = cls.field_name

        text = input.get('text')
        user_id = input.get('user_id')
        _, user_pk = Node.from_global_id(user_id)
        post_id = input.get('{}_id'.format(field_name))
        _, post_pk = Node.from_global_id(post_id)

        post = post_cls.objects.get(pk=post_pk)

        if post.owner_id != int(user_pk):
            raise Exception(
                'User={} cannot edit {}={} owned by user={}.'.format(user_pk, post.__name__, post.id, post.owner_id))

        post.text = text
        post.save()
        return cls(**{cls.field_name: post})


class EditComment(relay.ClientIDMutation, EditPostMixin):
    class Input:
        text = graphene.String(required=True)
        comment_id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    post_cls = Comment
    field_name = 'comment'
    comment = graphene.Field(lambda: CommentNode)


class EditQuestion(relay.ClientIDMutation, EditPostMixin):
    class Input:
        text = graphene.String(required=True)
        question_id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    post_cls = Question
    field_name = 'question'
    question = graphene.Field(lambda: QuestionNode)


class EditAnswer(relay.ClientIDMutation, EditPostMixin):
    class Input:
        text = graphene.String(required=True)
        answer_id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    post_cls = Answer
    field_name = 'answer'
    post = graphene.Field(lambda: AnswerNode)


class UpvotePostMixin(object):
    """
    The upvote and downvote mutations work on independent many to many relationships, thus it is possible for a user
    to _both_ upvote and downvote a post. We'll likely need some logic to prevent that scenario or a change in the data
    model to only allow either an upvote or downvote.
    """

    @staticmethod
    def mutate_and_get_payload(cls, input, context, info):
        post_cls = cls.post_cls
        field_name = cls.field_name

        user_id = input.get('user_id')
        _, user_pk = Node.from_global_id(user_id)
        post_id = input.get('{}_id'.format(field_name))
        _, post_pk = Node.from_global_id(post_id)

        user = User.objects.get(pk=user_pk)
        post = post_cls.objects.get(pk=post_pk)

        post.upvote.add(user)
        post.save()
        return cls(**{cls.field_name: post})


class UpvoteComment(relay.ClientIDMutation, UpvotePostMixin):
    class Input:
        comment_id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    post_cls = Comment
    field_name = 'comment'
    comment = graphene.Field(lambda: CommentNode)


class UpvoteQuestion(relay.ClientIDMutation, UpvotePostMixin):
    class Input:
        question_id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    post_cls = Question
    field_name = 'question'
    question = graphene.Field(lambda: QuestionNode)


class UpvoteAnswer(relay.ClientIDMutation, UpvotePostMixin):
    class Input:
        answer_id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    post_cls = Answer
    field_name = 'answer'
    answer = graphene.Field(lambda: AnswerNode)


class DownvotePostMixin(object):
    """
    The upvote and downvote mutations work on independent many to many relationships, thus it is possible for a user
    to _both_ upvote and downvote a post. We'll likely need some logic to prevent that scenario or a change in the data
    model to only allow either an upvote or downvote.
    """

    @staticmethod
    def mutate_and_get_payload(cls, input, context, info):
        post_cls = cls.post_cls
        field_name = cls.field_name

        user_id = input.get('user_id')
        _, user_pk = Node.from_global_id(user_id)
        post_id = input.get('{}_id'.format(field_name))
        _, post_pk = Node.from_global_id(post_id)

        user = User.objects.get(pk=user_pk)
        post = post_cls.objects.get(pk=post_pk)

        post.downvote.add(user)
        post.save()
        return cls(**{cls.field_name: post})


class DownvoteComment(relay.ClientIDMutation, DownvotePostMixin):
    class Input:
        comment_id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    post_cls = Comment
    field_name = 'comment'
    comment = graphene.Field(lambda: CommentNode)


class DownvoteQuestion(relay.ClientIDMutation, DownvotePostMixin):
    class Input:
        question_id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    post_cls = Question
    field_name = 'question'
    question = graphene.Field(lambda: QuestionNode)


class DownvoteAnswer(relay.ClientIDMutation, DownvotePostMixin):
    class Input:
        answer_id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    post_cls = Answer
    field_name = 'answer'
    answer = graphene.Field(lambda: AnswerNode)


class EditQuestionTags(relay.ClientIDMutation):
    """
    tags is a list of IdObjects
    """

    class Input:
        question_id = graphene.String(required=True)
        tags = graphene.List(graphene.String)

    question = graphene.Field(lambda: QuestionNode)

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        tag_ids = input.get('tags')
        tag_pks = [Node.from_global_id(id)[1] for id in tag_ids]
        tag_objects = Tag.objects.filter(id__in=tag_pks)
        question_id = input.get('question_id')
        question_pk = Node.from_global_id(question_id)[1]
        question = Question.get(pk=question_pk)

        question.tags.clear()
        question.tags.add(*tag_objects)
        question.save()

        return EditQuestionTags(question=question)


class Mutations(graphene.ObjectType):
    create_question = CreateQuestion.Field()
    create_answer = CreateAnswer.Field()
    create_comment = CreateComment.Field()
    edit_question = EditQuestion.Field()
    edit_answer = EditAnswer.Field()
    edit_comment = EditComment.Field()
    upvote_question = UpvoteQuestion.Field()
    upvote_answer = UpvoteAnswer.Field()
    upvote_comment = UpvoteComment.Field()
    downvote_question = DownvoteQuestion.Field()
    downvote_answer = DownvoteAnswer.Field()
    downvote_comment = DownvoteComment.Field()
    edit_question_tags = EditQuestionTags.Field()
