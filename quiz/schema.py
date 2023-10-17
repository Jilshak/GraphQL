import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Questions, Category, Quizzes, Answer


# Notes:

# These are the neccessory imports required
# import graphene
# from graphene_django import DjangoObjectType, DjangoListField

# this is the defention of graphQL type using
# graphene which helps to convert/map our
# django models to GraphQL types --> that is why we import DjangoObjectType from graphene
# class QuestionType(DjangoObjectType):
#     class Meta:
#         model = Questions
#         fields = '__all__'

# inside the qurey we define the available queries in GraphQL
# insider here we create function that define how to retrieve data when a query is made
# class Query(graphene.ObjectType):

# this line defines a qurey field that returns the list of the question type
# it tells GraphQL that you request a list of questions through the query named all_questions or //allQuestions
# all_questions = graphene.List(QuestionType)

# this is the resolver function. It is a method inside the Query
# class that tells graphQL that tells how to retrive data when all_question query is made/executed
# def resolve_all_books(root, info):
#     return Questions.objects.all()

# this line creates the GraphQL Schema. The schema is the entry point of your GraphQL schema
# it defines which queries and mutations are available
# schema = graphene.Schema(query=Query)

class QuestionType(DjangoObjectType):
    class Meta:
        model = Questions
        fields = '__all__'


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = '__all__'


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = '__all__'


class Query(graphene.ObjectType):

    quiz = graphene.String()
    
    def resolve_quiz():
        return f'This is the first question'


schema = graphene.Schema(query=Query)
