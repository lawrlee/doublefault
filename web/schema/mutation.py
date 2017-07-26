import graphene

from web.models import Comment, Answer, Question, Tag
from web.schema.nodes import CommentNode, QuestionNode, AnswerNode, TagNode
from django.contrib.auth.models import User

__all__ = ['Mutations']


class IdObject(graphene.InputObjectType):
    """
    To facilitate nested input data objects like

    {'id': 1}
    """
    id = graphene.Int()


class CreateQuestionPost(graphene.ClientIDMutation):
    class Input:
        post_text = graphene.String()
        owner_id = graphene.Int()

    question_post = graphene.Field(lambda: QuestionNode)
    ok = graphene.Boolean()

    @classmethod
    def mutate_and_get_payload(cls, input, info):
        owner_id = input.get('owner_id')
        post_text = input.get('post_text')

        question_post = QuestionNode._meta.model(post_text=post_text,
                                                 owner_id=owner_id)
        return CreateQuestionPost(question_post=question_post, ok=bool(question_post.id))


class CreateAnswerPost(graphene.ClientIDMutation):
    """
    Creates an Answer object that is related to a single Question object. Answer objects are required
    to be attached to a Question
    """

    class Input:
        post_text = graphene.String()
        owner_id = graphene.Int()
        question_id = graphene.Int()

    answer_post = graphene.Field(lambda: AnswerNode)
    ok = graphene.Boolean()

    @classmethod
    def mutate_and_get_payload(cls, input, info):
        owner_id = input.get('owner_id')
        post_text = input.get('post_text')
        question_id = input.get('question_id')

        answer_post = AnswerNode._meta.model(post_text=post_text,
                                             owner_id=owner_id,
                                             question_id=question_id)
        return CreateAnswerPost(answer_post=answer_post, ok=bool(answer_post.id))


# class CreatePost(graphene.Mutation):
#     """
#     This mutation is for a generic post that has to be attached to an Answer or Question object. The
#     `parent_post` input parameter is the IdObject for either of those. A generic post, however, cannot have a
#     child post.
#     """
#
#     class Input:
#         post_text = graphene.String()
#         owner = graphene.Argument(IdObject)
#         parent_post = graphene.Argument(IdObject)
#
#     post = graphene.Field(lambda: PostType)
#
#     @staticmethod
#     def mutate(root, args, context, info):
#         owner_data = args.get('owner')
#         owner_id = owner_data.get('id')
#         post_text = args.get('post_text')
#         parent_data = args.get('parent')
#         parent_id = parent_data.get('id')
#
#         post = PostType(post_text=post_text,
#                      owner_id=owner_id,
#                      parent_id=parent_id)
#         return CreatePost(post=post)
#
#
# class EditPost(graphene.Mutation):
#     """
#     This generic edit AbstractPost function is for AbstractPost, Question, and Answer objects. Only the owner of the post
#     should be able to edit it.
#     """
#
#     class Input:
#         post_text = graphene.String()
#         post = graphene.Argument(IdObject)
#
#     post = graphene.Field(lambda: PostType)
#
#     @staticmethod
#     def mutate(root, args, context, info):
#         post_data = args.get('post')
#         post_id = post_data.get('id')
#         post_text = args.get('post_text')
#
#         post = PostType.objects.get(pk=post_id)
#         post.post_text = post_text
#         post.save()
#         return EditPost(post=post)
#
#
# class UpvotePost(graphene.Mutation):
#     """
#     The upvote and downvote mutations work on independent many to many relationships, thus it is possible for a user
#     to _both_ upvote and downvote a post. We'll likely need some logic to prevent that scenario or a change in the data
#     model to only allow either an upvote or downvote.
#     """
#
#     class Input:
#         post = graphene.Argument(IdObject)
#         user = graphene.Argument(IdObject)
#
#     post = graphene.Field(lambda: PostType)
#
#     @staticmethod
#     def mutate(root, args, context, info):
#         post_data = args.get('post')
#         post_id = post_data.get('id')
#         user_data = args.get('user')
#         user_id = user_data.get('id')
#         user = User.objects.get(pk=user_id)
#
#         post = PostType.objects.get(pk=post_id)
#         post.upvotes.add(user)
#         post.save()
#         return EditPost(post=post)
#
#
# class DownvotePost(graphene.Mutation):
#     """
#     The upvote and downvote mutations work on independent many to many relationships, thus it is possible for a user
#     to _both_ upvote and downvote a post. We'll likely need some logic to prevent that scenario or a change in the data
#     model to only allow either an upvote or downvote.
#     """
#
#     class Input:
#         post = graphene.Argument(IdObject)
#         user = graphene.Argument(IdObject)
#
#     post = graphene.Field(lambda: PostType)
#
#     @staticmethod
#     def mutate(root, args, context, info):
#         post_data = args.get('post')
#         post_id = post_data.get('id')
#         user_data = args.get('user')
#         user_id = user_data.get('id')
#         user = User.objects.get(pk=user_id)
#
#         post = AbstractPost.objects.get(pk=post_id)
#         post.downvotes.add(user)
#         post.save()
#         return EditPost(post=post)
#
#
# class EditQuestionTags(graphene.Mutation):
#     """
#     tags is a list of IdObjects
#     """
#
#     class Input:
#         question = graphene.Argument(IdObject)
#         tags = graphene.List(IdObject)
#
#     question = graphene.Field(lambda: QuestionPostType)
#
#     @staticmethod
#     def mutate(root, args, context, info):
#         tags = args.get('tags')
#         tag_objects = Tag.objects.filter(id__in=[tag['id'] for tag in tags])
#         question_data = args.get('question')
#         question_id = question_data.get('id')
#         question = Question.get(pk=question_id)
#         question.tags.clear()
#         question.tags.add(*tag_objects)
#         question.save()
#
#         return EditQuestionTags(question=question)


class Mutations(graphene.ObjectType):
    create_question_post = CreateQuestionPost.Field()
    create_answer_post = CreateAnswerPost.Field()
    # create_post = CreatePost.Field()
    # edit_post = EditPost.Field()
    # upvote_post = UpvotePost.Field()
    # downvote_post = DownvotePost.Field()
    # edit_tags = EditQuestionTags.Field()
