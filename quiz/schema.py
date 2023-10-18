import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Questions, Category, Quizzes, Answer


# Notes:

# These are the neccessory imports required
# import graphene
# from graphene_django import DjangoObjectType, DjangoListField

#  > djangoObjectType --> allows us to map our models to graphql objects

#  > from the above import the DjangoListField ---> allows us to generate list and return it to us
#  > graphense.List() --> also provides the same functionality althogh there is only a minute differece between them
# for this we dont need to define a resolve

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
# withing the function resolve_all_books()
# root --> is the entry point to the query which is mandatory
# info ---> allows us to pass some information to run our query


# def resolve_all_books(root, info):
#     return Questions.objects.all()


# this line creates the GraphQL Schema. The schema is the entry point of your GraphQL schema
# it defines which queries and mutations are available
# schema = graphene.Schema(query=Query)


# DAY 2 (VIDEO PART 2)

# class Query(graphene.ObjectType):

#     all_quizzes = DjangoListField(QuizzesType)

#     def resolve_all_quizzes(root, info):
#         return Quizzes.objects.filter(id=1)


# schema = graphene.Schema(query=Query)

# in the above piece of code the query name is all_quizzes so if we were to access this
# from graphiql we will get all the objects related to that model
# so for customizing the data received we need to create a resolve method
#   >> the important thing to notice is that if we were create a custom method for fine grained control over what we need
# then after the resolve_ it has to be the query name (all_quizzes) --> even the spelling must be the same then and only then we can
# do custom filtering to that model
#  Note:
# > filtering data on the backend is not ideal for graphql as it defeats the purpose of even using this so for this we will be filtering data from the fronte end itself

# class Query(graphene.ObjectType):

#     all_quizzes = DjangoListField(QuizzesType)
#     all_questions = DjangoListField(QuestionType)

#     def resolve_all_quizzes(root, info):
#         return Quizzes.objects.all()

#     def resolve_all_questions(root, info):
#         return Questions.objects.all()


# schema = graphene.Schema(query=Query)

#  if we want we can also run two queries at the same time we only need to extend the query in the graphiql interface
# it will look something like
# {
#   allQuizzes {
#     id
#     title
#   }
#   allQuestions{
#     id
#     title
#   }
# }

#  now if we need to get a single item from the models without using the filter method in the backend we
# can use Field() instead of djangoListField()
# it is from graphene.Field()

# class Query(graphene.ObjectType):

#     all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())

#     def resolve_all_quizzes(root, info, id):
#         return Quizzes.objects.get(pk=id)

# schema = graphene.Schema(query=Query)

# in the above code we have setup a few things
# 1. changed the djangoListField with graphene.List()
# 2. added a new field inside the graphene.Field named id
# 3. Declared its datatype ie; graphene.Int()
# 4. then withing the resolve method we added a new parameter named id for the id in the query field to be available
# 5. then we used the id to get that particular object with that id from the Quizzes

# {
#   allQuizzes(id:1) {
#     id
#     title
#   }
# }

# Now coming to the graphiql interface we added a new filed
# allQuizzes(id:1)
# after what we done in the backend now this particular query field is expecting an id so it has to be given to it.

# query getQuizzessAndAnswers($id: Int = 1) {
#   allQuizzes(id: $id) {
#     id
#     title
#   }
# }

#  Now a few things to note here is that:
# > we have given here a name called getQuizzesAndAnswers ---> it won't affect the query itself it helps for us to identify the query and function
#  > we can use argumants and use it in the query like the id we passed here. (Learn the syntax we have to mention the type of whatever we are typing in there)


# DAY - 3 (VIDEO PART 3) ---> CRUD Operations

# > FOR ADDING SOMETHING TO THE DB THROUGH GRAPHQL WE NEED "MUTATIONS"

# class CategoryMutation(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)
#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls, root, info, name):
#         category = Category(name=name)
#         category.save()
#         return CategoryMutation(category=category)

# class Mutation(graphene.ObjectType):
#     update_category = CategoryMutation.Field()

# schema = graphene.Schema(query=Query, mutation=Mutation)
# Note:
# > A mutation is a way of changing/modify data over the server

# In the above given code there are a few things to note and those are:
# 1. we created a new class named Mutation which extends from the graphene.Mutation ---> required for the CRUD Operation
# 2. Then we defined a new class named Arguments --> this denotes the field which you want to mutate
# 3. Then we defined a new instance of category type to category --> represents the category that will be mutated
# 4. Then we define a classmethod within which we define a lot of things: ---> this is the actual step where the mutation occurs
# > we created a mutate function which has an arguments --> cls, root, info, name
#  > cls --> the class itself (it is important in mutation ---> otherwise data won't be created)
#  > root --> the root object (not used in mutation)
#  > info --> Information about the GraphQL query/mutation (not used in this mutation).

# > then we create an instance of the Category with the name which we pass into the name
# > then we save it
# > finally we return the CategoryMutation(category=category)

# Then we create a new class named mutation --> (The Mutation class is an object type that contains all the mutation fields. we only have update_category here but not that other mutations can also be added)
# after that we define a schema creating an instance of graphene schema where you pass in the query and mutation which are available in our api


# UPDATION OF FIELDS:

        # class CategoryUpdation(graphene.Mutation):
        #     class Arguments:
        #         id = graphene.ID()
        #         name = graphene.String(required=True)

        #     category = graphene.Field(CategoryType)

        #     @classmethod
        #     def mutate(cls, root, info, id, name):
        #         category = Category.objects.get(id=id)
        #         category.name = name
        #         category.save()
        #         return CategoryUpdation(category=category)


        # class Mutation(graphene.ObjectType):
        #     update_category = CategoryUpdation.Field()


        # schema = graphene.Schema(query=Query, mutation=Mutation)
        
# FRONT END LOOKS LIKE
        
        # mutation firstmutation {
        #   updateCategory(id: 10, name: "thirdCategory"){
        #     category{
        # 			name
        #     }
        #   }
        # }
        
        
# This is how the updation of the existing field looks like in graphiql
    #  > For updation of the existing field we also need to get the id so we use
            # id in the graphene as graphene.ID()
            # all the rest is the same the only difference here is that we pass in the id in the mutation field along with the name
            # then the rest is simple django we find the category with the id and then we assing the new name and saves it
            
            
# DELETION OF DATA IN THE TABLE: 

        # class CategoryDeletion(graphene.Mutation):
        #     class Arguments:
        #         id = graphene.ID()
        #     category = graphene.Field(CategoryType)
            
        #     @classmethod
        #     def mutate(cls, root, info, id):
        #         category = Category.objects.get(id=id)
        #         print(category)
        #         category.delete()
        #         return
        
        #  > For the deletion method also we use the same principle
        #  > there is no change whatsoever and its relatively very easy same of that of the updation and creation
        #  > after deletion we don't need  to return anything hence the empty return


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
        fields = ("id", "title")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = '__all__'


class Query(graphene.ObjectType):

    all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())
    all_answers = DjangoListField(AnswerType)

    def resolve_all_quizzes(root, info, id):
        return Quizzes.objects.get(pk=id)

    def resolve_all_answers(root, info):
        return Answer.objects.all()


class CategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return CategoryMutation(category=category)


class CategoryUpdation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id, name):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return CategoryUpdation(category=category)


class CategoryDeletion(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    category = graphene.Field(CategoryType)
    
    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        print(category)
        category.delete()
        return

class Mutation(graphene.ObjectType):
    add_category = CategoryMutation.Field()
    update_category = CategoryUpdation.Field()
    delete_category = CategoryDeletion.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
