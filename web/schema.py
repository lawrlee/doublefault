import graphene

from graphene_django.types import DjangoObjectType

from web.models import Post, AnswerPost, QuestionPost, Tag

class PostType(DjangoObjectType):
    class Meta:
        model = Post
    
class AnswerPostType(DjangoObjectType):
    class Meta:
        model = AnswerPost
    
class QuestionPostType(DjangoObjectType):
    class Meta:
        model = QuestionPost

class TagType(DjangoObjectType):
    class Meta:
        model = QuestionPost

class DoubleFaultQuery(graphene.AbstractType):
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


class Query(DoubleFaultQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)