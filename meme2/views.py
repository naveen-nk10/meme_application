from django.shortcuts import render
from django.contrib.auth import login


from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
# Create your views here.
from django.http import JsonResponse
from rest_framework import generics,permissions
from knox.models import AuthToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.contrib.auth.models import User

# Create your views here.
@api_view(['GET'])
def taskList(request):
	tasks = User.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)
@api_view(['GET'])
def apiOverview(request):
	

	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

class RegisterAPI(generics.GenericAPIView):
    serializer_class=TaskSerializer
    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['email']
        user=serializer.save()
        return Response({
            "user":TaskSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)