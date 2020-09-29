import graphene
import shawty.shawtier.schema


class Query(shawty.shawtier.schema.Query, graphene.ObjectType):
    pass


class Mutation(shawty.shawtier.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
