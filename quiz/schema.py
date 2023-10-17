import graphene
from graphene_django import DjangoObjectType
from .models import Questions


class QuestionType(DjangoObjectType):
    class Meta:
        model = Questions
        fields = '__all__'


class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionType)
    
    def resolve_all_books(root, info):
        return Questions.objects.all()


schema = graphene.Schema(query=Query)
