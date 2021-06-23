from django.urls import path
from . import views
from .views import RegisterAPI,LoginAPI
from knox import views as knox_views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
    path('usercreate', RegisterAPI.as_view(), name="usercreate"),
    path('task-list/', views.taskList, name="task-list"),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    
]
