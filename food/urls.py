from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("",views.index,name="index"),
    path("pizza",views.index,name="index"),
    path("login",views.login,name="login"),
    path("salads",views.salads,name="salads"),
    path("noodles",views.noodles,name="noodles"),
    path("checkout",views.checkout,name="checkout"),
    path("home",views.home,name="home"),
    path("project/<str:pk>/",views.projectPage,name="project"),
    
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)