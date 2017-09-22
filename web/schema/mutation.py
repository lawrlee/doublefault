import graphene
# from graphene import relay, Type

from web.models import Comment, Answer, Question, Tag
from web.schema.types import CommentType, QuestionType, AnswerType, TagType
from django.contrib.auth.models import User

__all__ = ['Mutations']


class CreateQuestion(graphene.Mutation):
    """
    mutation M {
    createQuestion(text: "creating in graphiql again", ownerId:1) {
        question {
          id
          text
        }
        ok
    }
    """

    class Input:
        text = graphene.String(required=True)
        owner_id = graphene.String(required=True)
        # question_data = QuestionInput(required=True)

    ok = graphene.Boolean()
    question = graphene.Field(lambda: QuestionType)

    @staticmethod
    def mutate(root, args, context, info):
        question = Question(text=args.get('text'), owner_id=int(args.get('owner_id')))
        question.save()
        ok = True
        return CreateQuestion(question=question, ok=ok)


class CreateAnswer(graphene.Mutation):
    """
    Creates an Answer object that is related to a single Question object. Answer objects are required
    to be attached to a Question
    """

    class Input:
        text = graphene.String(required=True)
        owner_id = graphene.String(required=True)
        question_id = graphene.String(required=True)

    ok = graphene.Boolean()
    answer = graphene.Field(lambda: AnswerType)

    @staticmethod
    def mutate(root, args, context, info):
        answer = Answer(text=args.get('text'),
                        owner_id=int(args.get('owner_id')),
                        question_id=int(args.get('question_id')))
        answer.save()
        ok = True
        return CreateAnswer(answer=answer, ok=ok)


class CreateComment(graphene.Mutation):
    """
    This mutation is for a generic comment that has to be attached to an Answer or Question object.
    """

    class Input:
        text = graphene.String(required=True)
        owner_id = graphene.String(required=True)
        question_id = graphene.String()
        answer_id = graphene.String()

    ok = graphene.Boolean()
    comment = graphene.Field(lambda: CommentType)

    @staticmethod
    def mutate(root, input, context, info):
        text = input.get('text')
        owner_id = input.get('owner_id')
        question_id = input.get('question_id', None)
        answer_id = input.get('answer_id', None)

        if question_id and answer_id:
            raise Exception('A comment can only be associated with either a question or an answer, not both')

        if question_id:
            comment = Comment(text=text,
                              owner_id=owner_id,
                              question_id=question_id)
        elif answer_id:
            comment = Comment(text=text,
                              owner_id=owner_id,
                              answer_id=answer_id)
        comment.save()
        ok = True
        return CreateComment(comment=comment, ok=ok)


class EditComment(graphene.Mutation):
    class Input:
        text = graphene.String(required=True)
        id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    ok = graphene.Boolean()
    comment = graphene.Field(lambda: CommentType)

    @staticmethod
    def mutate(root, input, context, info):
        text = input.get('text')
        user_id = input.get('user_id')
        post_id = input.get('id')

        post = Comment.objects.get(pk=post_id)

        if post.owner_id != int(user_id):
            raise Exception(
                'User={} cannot edit {}={} owned by user={}.'.format(user_id, post.__class__.__name__, post.id,
                                                                     post.owner_id))

        post.text = text
        post.save()
        ok = True
        return EditComment(comment=post, ok=ok)


class EditQuestion(graphene.Mutation):
    class Input:
        text = graphene.String(required=True)
        id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    post_cls = Question
    ok = graphene.Boolean()
    question = graphene.Field(lambda: QuestionType)

    @staticmethod
    def mutate(root, input, context, info):
        text = input.get('text')
        user_id = input.get('user_id')
        post_id = input.get('id')

        post = Question.objects.get(pk=post_id)

        if post.owner_id != int(user_id):
            raise Exception(
                'User={} cannot edit {}={} owned by user={}.'.format(user_id, post.__class__.__name__, post.id,
                                                                     post.owner_id))

        post.text = text
        post.save()
        ok = True
        return EditQuestion(question=post, ok=ok)


class EditAnswer(graphene.Mutation):
    class Input:
        text = graphene.String(required=True)
        id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    ok = graphene.Boolean()
    answer = graphene.Field(lambda: AnswerType)

    @staticmethod
    def mutate(root, input, context, info):
        text = input.get('text')
        user_id = input.get('user_id')
        post_id = input.get('id')

        post = Answer.objects.get(pk=post_id)

        if post.owner_id != int(user_id):
            raise Exception(
                'User={} cannot edit {}={} owned by user={}.'.format(user_id, post.__class__.__name__, post.id,
                                                                     post.owner_id))

        post.text = text
        post.save()
        ok = True
        return EditAnswer(answer=post, ok=ok)


class UpvoteComment(graphene.Mutation):
    class Input:
        id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    ok = graphene.Boolean()
    comment = graphene.Field(lambda: CommentType)

    @staticmethod
    def mutate(root, input, context, info):
        user_id = input.get('user_id')
        post_id = input.get('id')

        user = User.objects.get(pk=user_id)
        post = Comment.objects.get(pk=post_id)

        post.upvotes.add(user)
        post.save()
        return UpvoteComment(comment=post, ok=True)


class UpvoteQuestion(graphene.Mutation):
    class Input:
        id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    ok = graphene.Boolean()
    question = graphene.Field(lambda: QuestionType)

    @staticmethod
    def mutate(root, input, context, info):
        user_id = input.get('user_id')
        post_id = input.get('id')

        user = User.objects.get(pk=user_id)
        post = Question.objects.get(pk=post_id)

        post.upvotes.add(user)
        post.save()
        return UpvoteQuestion(question=post, ok=True)


class UpvoteAnswer(graphene.Mutation):
    class Input:
        id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    ok = graphene.Boolean()
    answer = graphene.Field(lambda: AnswerType)

    @staticmethod
    def mutate(root, input, context, info):
        user_id = input.get('user_id')
        post_id = input.get('id')

        user = User.objects.get(pk=user_id)
        post = Answer.objects.get(pk=post_id)

        post.upvotes.add(user)
        post.save()
        return UpvoteAnswer(answer=post, ok=True)


class DownvoteComment(graphene.Mutation):
    class Input:
        id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    ok = graphene.Boolean()
    comment = graphene.Field(lambda: CommentType)

    @staticmethod
    def mutate(root, input, context, info):
        user_id = input.get('user_id')
        post_id = input.get('id')

        user = User.objects.get(pk=user_id)
        post = Comment.objects.get(pk=post_id)

        post.downvotes.add(user)
        post.save()
        return DownvoteComment(comment=post, ok=True)


class DownvoteQuestion(graphene.Mutation):
    class Input:
        id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    ok = graphene.Boolean()
    question = graphene.Field(lambda: QuestionType)

    @staticmethod
    def mutate(root, input, context, info):
        user_id = input.get('user_id')
        post_id = input.get('id')

        user = User.objects.get(pk=user_id)
        post = Question.objects.get(pk=post_id)

        post.downvotes.add(user)
        post.save()
        return DownvoteQuestion(question=post, ok=True)


class DownvoteAnswer(graphene.Mutation):
    class Input:
        id = graphene.String(required=True)
        user_id = graphene.String(required=True)

    ok = graphene.Boolean()
    answer = graphene.Field(lambda: AnswerType)

    @staticmethod
    def mutate(root, input, context, info):
        user_id = input.get('user_id')
        post_id = input.get('id')

        user = User.objects.get(pk=user_id)
        post = Answer.objects.get(pk=post_id)

        post.downvotes.add(user)
        post.save()
        return DownvoteAnswer(answer=post, ok=True)


class EditQuestionTags(graphene.Mutation):
    """
    tags is a list of IdObjects
    """

    class Input:
        question_id = graphene.String(required=True)
        tags = graphene.List(graphene.String)

    question = graphene.Field(lambda: QuestionType)

    @staticmethod
    def mutate(root, input, context, info):
        tag_ids = input.get('tags')
        tag_objects = Tag.objects.filter(id__in=tag_ids)
        question_id = input.get('question_id')
        question = Question.get(pk=question_id)

        question.tags.clear()
        question.tags.add(*tag_objects)
        question.save()

        return EditQuestionTags(question=question, ok=True)


class IncrementQuestionView(graphene.Mutation):
    class Input:
        id = graphene.String(required=True)

    ok = graphene.Boolean()
    question = graphene.Field(lambda: QuestionType)

    @staticmethod
    def mutate(root, input, context, info):
        question_id = input.get('id')
        question = Question.objects.get(pk=question_id)
        question.views += 1
        question.save()
        return IncrementQuestionView(question=question, ok=True)


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
