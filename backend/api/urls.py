from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from . import views
from .views import MyTokenObtainPairView

urlpatterns=[
    path("token/",MyTokenObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view()),
    path("register/",views.RegisterView.as_view()),
    path("dashboard/",views.dashboard),
    path("test/",views.testEndPoint, name='test'),
    path('',views.getRoutes)
]