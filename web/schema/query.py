import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug

# from web.models import AbstractPost as _Post, Answer as _AnswerPost, Question as _QuestionPost, Tag as _Tag
from web.models import Comment, Answer, Question, Tag
from django.contrib.auth.models import User
from web.schema.types import CommentType, AnswerType, QuestionType, TagType, UserType

class Query(graphene.ObjectType):
    question = graphene.Field(QuestionType, id=graphene.Int())
    all_questions = graphene.List(QuestionType)
    answer = graphene.Field(AnswerType, id=graphene.Int())
    all_answers = graphene.List(AnswerType)
    comment = graphene.Field(CommentType, id=graphene.Int())
    all_comments = graphene.List(CommentType)
    tag = graphene.Field(TagType, id=graphene.Int())
    all_tags = graphene.List(TagType)
    all_users = graphene.List(UserType)

    def resolve_question(self, attrs, request, info):
        id = attrs.get('id')

        if id is not None:
            return Question.objects.get(pk=id)

        return None

    def resolve_all_questions(self, *args, **kwargs):
        return Question.objects.all()

    def resolve_answer(self, attrs, request, info):
        id = attrs.get('id')

        if id is not None:
            return Answer.objects.get(pk=id)

        return None

    def resolve_all_answers(self, *args, **kwargs):
        return Answer.objects.all()

    def resolve_comment(self, attrs, request, info):
        id = attrs.get('id')

        if id is not None:
            return Comment.objects.get(pk=id)

        return None

    def resolve_all_comments(self, *args, **kwargs):
        return Comment.objects.all()

    def resolve_tag(self, attrs, request, info):
        id = attrs.get('id')

        if id is not None:
            return Tag.objects.get(pk=id)

        return None

    def resolve_all_tags(self, *args, **kwargs):
        return Tag.objects.all()

    def resolve_all_users(self, *args, **kwargs):
        return User.objects.all()

    debug = graphene.Field(DjangoDebug, name='__debug')
