from django.urls import path

from . import views

# ここでapp_nameを指定してしまうと、テンプレート、ビューのすべてのURL逆引きを修正する必要があるため、あえて指定しない
#app_name    = "accounts"
urlpatterns = [ 
    path("signup/", views.signup, name="signup"),

    # 書き方を統一させるため前もってas_view化しておく。(一部オーバーライドしている。)
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("password_change/", views.password_change, name="password_change"),
    path("password_change/done/", views.password_change_done, name="password_change_done"),
    path("password_reset/", views.password_reset, name="password_reset"),
    path("password_reset/done/", views.password_reset_done, name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.password_reset_confirm, name="password_reset_confirm"),
    path("reset/done/", views.password_reset_complete, name="password_reset_complete"),
]


