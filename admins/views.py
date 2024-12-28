from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import AppAdmin
from rest_framework import status
from django.contrib import messages
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework.permissions import AllowAny
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .serializers import AdminActivitySerializer, UserRegistrationSerializer, UserLoginSerializer
from users.views import HomeView



class AppAdminView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin.html'
    permission_classes = [IsAdminUser]

    def get(self, request):
        return render(request, 'admin.html')

    def post(self, request):
        serializer = AdminActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'App added successfully!')
            return redirect('admin')
        else:
            messages.error(request, 'Please provide all required details!')
            return redirect('admin')


class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register.html'
    user = User.objects.get(username="iop") 
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
        else:
            messages.error(request, 'Something wrong please Register Aagain')
        return render(request, 'register.html')


class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        serializer = UserLoginSerializer(data=request.POST)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('admin')
                
            else:
                messages.error(request, 'Invalid credentials')

        else:
            messages.error(request, 'Invalid data')
        return render(request, 'login.html')




class LogoutView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        logout(request)
        return redirect('login')

