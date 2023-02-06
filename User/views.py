from .serializers import UserSerializer
from .models import User
from rest_framework_mongoengine import generics
from django.http import HttpResponse,JsonResponse


# createing  the users
class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class =UserSerializer

    
# getting all the users
class UserList(generics.ListAPIView):
    UserSerializer.Meta.model=User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get_queryset(self):
        queryset = self.queryset    
        return queryset





