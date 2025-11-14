from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, RegisterView, loginView
from django.urls import path, include   

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
     path('', include(router.urls)),
     path('register/', RegisterView.as_view(), name='register'), 
     path('login/', loginView.as_view(), name='login'),
]
    
