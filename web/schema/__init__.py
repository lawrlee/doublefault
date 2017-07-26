import graphene

from web.schema.query import Query
from web.schema.mutation import Mutations

__all__ = ['schema']

# schema = graphene.Schema(query=Query)
schema = graphene.Schema(query=Query, mutation=Mutations)