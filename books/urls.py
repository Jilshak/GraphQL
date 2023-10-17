from django.urls import path
from graphene_django.views import GraphQLView
from books.schema import test

urlpatterns = [
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=test)),
]
