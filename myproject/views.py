
from .models import Task
from .serializers import TaskSerializer, RegisterSerializer
from rest_framework import viewsets, permissions, generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def  get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RegisterView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class loginView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username_or_email = request.data.get('username_or_email')
        password = request.data.get('password')


        user = authenticate(username=username_or_email, password=password)
        if user is not None:
            try:
                user_object = User.objects.get(email=username_or_email)
                user = authenticate(username=user_object.username, password=password)
            except User.DoesNotExist:
                user = None

        if user is None:
            return Response({'message': 'Invalid credentials'}, status=401) 

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "username": user.username,
            "email": user.email
            })
        

    