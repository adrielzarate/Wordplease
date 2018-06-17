"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blogs.views import HomeView, BlogView, PostFormView, PostView, BlogsView
from users.views import LoginView, LogoutView, SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'), # ultimos posts de todos los usuarios
    path('blogs/', BlogsView.as_view(), name='blogs-list'), # listado de blogs
    path('blogs/<owner>', BlogView.as_view(), name='user-blog'), # blog de un usuario


    path('blogs/<owner>/<int:pk>', PostView.as_view(), name='user-post'), # post del blog de un usuario


    path('new-post', PostFormView.as_view(), name='new-post'), # formulario para crear nuevo post

    path('login', LoginView.as_view(), name='login'), # login
    path('logout', LogoutView.as_view(), name='logout'), # logout
    path('signup', SignupView.as_view(), name='signup'), # registrarse

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
