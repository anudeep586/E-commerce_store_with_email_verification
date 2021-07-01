from . import views
from django.urls import path




urlpatterns = [
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path('token',views.token_send,name="token_send"),
    path('success',views.success,name="success"),
    path('error',views.error_page,name="error"),
    path('verify/<auth_token>',views.verify,name="verify")

]