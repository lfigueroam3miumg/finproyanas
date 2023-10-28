"""sinergia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import routers, serializers, viewsets
from Login import views

from django.conf import settings
from django.conf.urls.static import static


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rutas api
    # path('api-users/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-generales/', include('generales.urls')),
    # Rutas front
    path('', views.helloWorld,name="inicio"),
    path('login/',views.LoginPage, name='login_page'),
    path('singUp/',views.SingUpPage, name='singUp'),
    path('home/',login_required(views.homePage, login_url='/login/'), name='home_page'),
    path('projects/',login_required(views.projectPage, login_url='/login/'), name='projects'),
    path('jobs/',login_required(views.jobsPage, login_url='/login/'), name='jobs'),
    path('help/',login_required(views.helpPage, login_url='/login/'), name='help'),
    path('logout/',views.cerrarSesion, name='logOut')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)