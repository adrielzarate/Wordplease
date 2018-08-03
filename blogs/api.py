from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from blogs.models import Post
from blogs.permissions import PostPermissions
from blogs.serializers import PostListSerializer, PostDetailSerializer, NewPostSerializer, BlogsListSerializer


class BlogsViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = BlogsListSerializer
    permission_classes = [PostPermissions]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username']
    ordering = ['first_name']

    def get_serializer_class(self):
        if self.action == 'list':
            return BlogsListSerializer


class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [PostPermissions]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'post_body']
    ordering = ['-pub_date']

    def get_serializer_class(self):
        return self.serializer_class if self.action != 'list' else PostListSerializer

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return self.queryset.filter(pub_date__lte=timezone.now())
        else:
            return self.queryset.filter(Q(owner=self.request.user) | Q(pub_date__lte=timezone.now()))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
