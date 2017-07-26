import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType

from web.models import Comment, Answer, Question, Tag
from django.contrib.auth.models import User

__all__ = ['UserNode',
           'TagNode',
           'PostNode',
           'AnswerNode',
           'QuestionNode']


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        filter_fields = ['name', 'users']
        interfaces = (relay.Node,)


class CommentNode(DjangoObjectType):
    upvotes = graphene.List(UserNode)
    downvotes = graphene.List(UserNode)
    score = graphene.String(source='score')

    @graphene.resolve_only_args
    def resolve_upvotes(self):
        return self.upvotes.all()

    @graphene.resolve_only_args
    def resolve_downvotes(self):
        return self.downvotes.all()

    class Meta:
        model = Comment
        interfaces = (relay.Node,)


class AnswerNode(DjangoObjectType):
    upvotes = graphene.List(UserNode)
    downvotes = graphene.List(UserNode)
    score = graphene.String(source='score')
    comments = graphene.List(CommentNode)

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
        interfaces = (relay.Node,)


class QuestionNode(DjangoObjectType):
    upvotes = graphene.List(UserNode)
    downvotes = graphene.List(UserNode)
    score = graphene.String(source='score')
    comments = graphene.List(CommentNode)
    tags = graphene.List(TagNode)

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
        interfaces = (relay.Node,)
