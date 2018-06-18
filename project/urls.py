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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blogs.api import PostViewSet, BlogsViewSet
from blogs.views import HomeView, BlogView, PostFormView, PostView, BlogsView
from users.api import UserViewSet
from users.views import LoginView, LogoutView, SignupView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('blogs', BlogsViewSet, base_name='blogs')
router.register('posts', PostViewSet, base_name='posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('blogs/', BlogsView.as_view(), name='blogslist'),
    path('blogs/<owner>', BlogView.as_view(), name='user-blog'),
    path('blogs/<owner>/<int:pk>', PostView.as_view(), name='user-post'),
    path('new-post', PostFormView.as_view(), name='new-post'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignupView.as_view(), name='signup'),
    path('api/v1/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
