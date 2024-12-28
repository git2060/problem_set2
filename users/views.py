from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from admins.models import AppAdmin
from .serializers import UserRegistrationSerializer, AppSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render, redirect
from django.contrib import messages

class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register.html'
    
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            messages.error(request, 'Something wrong please Register Aagain')
        return render(request, 'register.html')


class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'
    
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.error(request, 'Looged in Successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid data')
        return render(request, 'login.html')



class HomeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'
    permission_classes = [IsAuthenticated]

    def get(self, request):
        app =AppAdmin.objects.all()
        serializer = AppSerializer(app, many=True)
        return Response({'data':serializer.data})



class AppView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app.html'
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        app = AppAdmin.objects.get(id=id)
        serializer = AppSerializer(app)
        return Response({'data': serializer.data})
    

    def post(self, request, id):
        app = AppAdmin.objects.get(id=id)

        serializer = AppSerializer(app,data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.error(request, "Data Fetch Successfully")
            return render(request, 'app.html')
        else:    
            messages.error(request, 'Somwthing worng no data found')
        return render(request, 'app.html')


class PointsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'points.html'
    permission_classes = [IsAuthenticated]

    def get(self, request):
        apps =AppAdmin.objects.all()
        serializer = AppSerializer(apps, many=True)
        return Response({'apps': serializer.data})

    def get(self, request):
        total_apps = AppAdmin.objects.all()
        total_points = sum([app.points for app in total_apps])
        app_names = [app.app_name for app in total_apps]
        app_points = [app.points for app in total_apps]

        return Response({
            'total_points': total_points,
            'app_names': app_names,
            'app_points': app_points
        })


class TaskView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'task.html'
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_apps = AppAdmin.objects.all()
        app_names = [app.app_name for app in total_apps]
        return Response({'app_names': app_names})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        logout(request)
        messages.error(request, "Logged out Successfully")
        return render(request,'logout.html')



class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request):
        return render(request,'profile.html')