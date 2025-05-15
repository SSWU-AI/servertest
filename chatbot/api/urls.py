from django.urls import path
from .views import SignupView, LoginView, UserInfoView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserInfoView.as_view()),
]
