from django.urls import path
from .views import RegisterView, LoginView, AppAdminView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/admin/', AppAdminView.as_view(), name='admin'),
]

