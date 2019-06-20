import graphene
from graphene_django import DjangoObjectType
from home.models import HomePage
# from django.db import models


class HomePageNode(DjangoObjectType):
    class Meta:
        model = HomePage
        only_fields = ['id', 'title']


class Query(graphene.ObjectType):
    articles = graphene.List(HomePageNode)

    @graphene.resolve_only_args
    def resolve_homepages(self):
        return HomePage.objects.live()

schema = graphene.Schema(query=Query)
