from django.urls import path
from .views import SignupView, LoginView, PasswordResetView, VerifyCodeView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('reset-password/', PasswordResetView.as_view()),
    path('verify-code/', VerifyCodeView.as_view()),
]
