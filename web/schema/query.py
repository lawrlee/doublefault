import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug

# from web.models import AbstractPost as _Post, Answer as _AnswerPost, Question as _QuestionPost, Tag as _Tag
from web.schema.nodes import CommentNode, AnswerNode, QuestionNode, TagNode


class Query(graphene.ObjectType):
    # List queries

    all_comments = DjangoFilterConnectionField(CommentNode)
    all_answers = DjangoFilterConnectionField(AnswerNode)
    all_questions = DjangoFilterConnectionField(QuestionNode)
    all_tags = DjangoFilterConnectionField(TagNode)

    # Single object queries

    question = relay.Node.Field(QuestionNode)
    answer = relay.Node.Field(AnswerNode)
    tag = relay.Node.Field(TagNode)
    comment = relay.Node.Field(CommentNode)

    debug = graphene.Field(DjangoDebug, name='__debug')
