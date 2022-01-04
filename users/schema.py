import graphene
import graphql_jwt
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphql_jwt.shortcuts import get_token
from django.contrib.auth.hashers import check_password

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
class LoginUser(graphene.Mutation):
    
    user = graphene.Field(UserType)
    token = graphene.String()

    class Arguments:
        email = graphene.String(required=True)
        password=graphene.String(required=True)
        
    def mutate(self,info, email, password):
        u=get_user_model().objects.get(email=email)
        haspassword=u.password
        token = ''
        if get_user_model().objects.filter(email=email).exists() and check_password(password, haspassword): 
            user = get_user_model().objects.get(email=email)
            token = get_token(user)
        else:
            raise Exception("Auth credential is not provided")
        return LoginUser(user=user, token=token)
class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        name= graphene.String(required=True)
        username= graphene.String(required=True)
        phone_no=graphene.Int(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        
    def mutate(self, info, name, username,password,phone_no,email):
        if get_user_model().objects.filter(email=email).exists():
            raise Exception("email already used")
        users=get_user_model().objects.all()
        for user in users:
            if user.check_password(password):
                raise Exception("password already used")
        user = get_user_model()(
            name=name,
            username=username,
            phone_no=phone_no,
            email=email,  
        )
        user.set_password(password)
        user.save()
        return CreateUser(user=user)    

class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id= graphene.ID()
        name= graphene.String(required=True)
        username= graphene.String(required=True)
        phone_no=graphene.Int(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        
    def mutate(self, info,id, name, username,password,phone_no,email):
        user=get_user_model().objects.get(id=id)
        user.name=name
        user.username=username
        user.phone_no=phone_no
        # user.password=password
        user.email=email
        user.save()
        user.set_password(password)
        user.save()
        return UpdateUser(user=user)        



class Mutation(graphene.ObjectType):   
    login_user = LoginUser.Field()
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()
schema = graphene.Schema(query=Query,mutation=Mutation)
