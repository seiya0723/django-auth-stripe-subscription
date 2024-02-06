from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse_lazy
from django.http import HttpResponseNotAllowed

from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


from .forms import SignupForm

class SignupView(CreateView):
    
    form_class      = SignupForm
    success_url     = reverse_lazy("login")
    template_name   = "registration/signup.html"

    # 認証済みの状態でリクエストした時、LOGIN_REDIRECT_URL へリダイレクトさせる
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

signup  = SignupView.as_view()

class CustomLoginView(LoginView):

    # 認証済みの状態でリクエストした時、LOGIN_REDIRECT_URL へリダイレクトさせる
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

login   = CustomLoginView.as_view()

# LogoutViewのGETメソッドを無効化する。(すでにDjango4.1で非推奨。5.0で削除される見通し)
# https://docs.djangoproject.com/ja/4.2/topics/auth/default/#django.contrib.auth.views.LogoutView
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(permitted_methods=['POST'])

logout  = CustomLogoutView.as_view()


password_change             = PasswordChangeView.as_view()
password_change_done        = PasswordChangeDoneView.as_view()
password_reset              = PasswordResetView.as_view()
password_reset_done         = PasswordResetDoneView.as_view()
password_reset_confirm      = PasswordResetConfirmView.as_view()
password_reset_complete     = PasswordResetCompleteView.as_view()


