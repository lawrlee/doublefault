import graphene
from graphene_django.types import DjangoObjectType

from web.models import Comment, Answer, Question, Tag
from django.contrib.auth.models import User

__all__ = ['UserType',
           'TagType',
           'PostType',
           'AnswerType',
           'QuestionType']


class UserType(DjangoObjectType):
    get_full_name = graphene.String(source='get_full_name')

    class Meta:
        model = User


class TagType(DjangoObjectType):
    users = graphene.List(UserType)

    @graphene.resolve_only_args
    def resolve_users(self):
        return self.users.all()

    class Meta:
        model = Tag
        filter_fields = ['name', 'users']


class CommentType(DjangoObjectType):
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
        model = Comment


class AnswerType(DjangoObjectType):
    upvotes = graphene.List(UserType)
    downvotes = graphene.List(UserType)
    score = graphene.String(source='score')
    comments = graphene.List(CommentType)

    @graphene.resolve_only_args
    def resolve_upvotes(self):
        return self.upvotes.all()

    @graphene.resolve_only_args
    def resolve_downvotes(self):
        return self.downvotes.all()

    @graphene.resolve_only_args
    def resolve_comments(self):
        return self.comments.all()

    class Meta:
        model = Answer


class QuestionType(DjangoObjectType):
    upvotes = graphene.List(UserType)
    downvotes = graphene.List(UserType)
    score = graphene.String(source='score')
    comments = graphene.List(CommentType)
    tags = graphene.List(TagType)

    @graphene.resolve_only_args
    def resolve_upvotes(self):
        return self.upvotes.all()

    @graphene.resolve_only_args
    def resolve_downvotes(self):
        return self.downvotes.all()

    @graphene.resolve_only_args
    def resolve_comments(self):
        return self.comments.all()

    @graphene.resolve_only_args
    def resolve_tags(self):
        return self.tags.all()

    class Meta:
        model = Question