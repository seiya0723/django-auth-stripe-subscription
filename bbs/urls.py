from django.urls import path
from . import views

app_name    = "bbs"
urlpatterns = [
    path("", views.index, name="index"),
    path("checkout/", views.checkout, name="checkout"),
    path("success/", views.success, name="success"),
    path("portal/", views.portal, name="portal"),
    path("premium/", views.premium, name="premium"),
]



