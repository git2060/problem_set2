from django.urls import path
from .views import RegisterView, LoginView, HomeView, AppView, PointsView, TaskView, LogoutView,ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('app/<int:id>/', AppView.as_view(), name='app'),
    path('points/', PointsView.as_view(), name='points'),
    path('task/', TaskView.as_view(), name='task'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
