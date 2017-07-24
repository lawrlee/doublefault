import graphene

from graphene_django.types import DjangoObjectType

from web.models import Post, AnswerPost, QuestionPost, Tag
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class PostType(DjangoObjectType):
    upvotes = graphene.List(UserType)
    downvotes = graphene.List(UserType)
    score = graphene.String(source='score')

    @graphene.resolve_only_args
    def resolve_upvotes(self):
        return self.upvotes.all()

    @graphene.resolve_only_args
    def resolve_downvotes(self):
        return self.downvotes.all()

    class Meta:
        model = Post


class AnswerPostType(DjangoObjectType):
    upvotes = graphene.List(UserType)
    downvotes = graphene.List(UserType)
    score = graphene.String(source='score')
    child_posts = graphene.List(PostType)

    @graphene.resolve_only_args
    def resolve_upvotes(self):
        return self.upvotes.all()

    @graphene.resolve_only_args
    def resolve_downvotes(self):
        return self.downvotes.all()

    @graphene.resolve_only_args
    def resolve_child_posts(self):
        return self.child_posts.all()

    class Meta:
        model = AnswerPost


class QuestionPostType(DjangoObjectType):
    upvotes = graphene.List(UserType)
    downvotes = graphene.List(UserType)
    score = graphene.String(source='score')
    child_posts = graphene.List(PostType)
    tags = graphene.List(TagType)

    @graphene.resolve_only_args
    def resolve_upvotes(self):
        return self.upvotes.all()

    @graphene.resolve_only_args
    def resolve_downvotes(self):
        return self.downvotes.all()

    @graphene.resolve_only_args
    def resolve_child_posts(self):
        return self.child_posts.all()

    @graphene.resolve_only_args
    def resolve_tags(self):
        return self.tags.all()

    class Meta:
        model = QuestionPost


class Query(graphene.ObjectType):
    # List queries

    all_posts = graphene.List(PostType)
    all_answer_posts = graphene.List(AnswerPostType)
    all_question_posts = graphene.List(QuestionPostType)
    all_tags = graphene.List(TagType)

    def resolve_all_posts(self, args, context, info):
        return Post.objects.all()

    def resolve_all_answer_posts(self, args, context, info):
        return AnswerPost.objects.all()

    def resolve_all_question_posts(self, args, context, info):
        return QuestionPost.objects.all()

    def resolve_all_tags(self, args, context, info):
        return Tag.objects.all()

    # Single object queries

    question_post = graphene.Field(QuestionPostType,
                                   id=graphene.Int())

    def resolve_question_post(self, args, content, info):
        id = args.get('id')

        if id is not None:
            return QuestionPost.objects.get(pk=id)

        return None




# class Query(DoubleFaultQuery, graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query)
