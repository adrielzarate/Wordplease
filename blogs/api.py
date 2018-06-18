from django.contrib.auth.models import User
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
        return BlogsListSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [PostPermissions]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'post_body']
    ordering = ['-pub_date']

    def get_serializer_class(self):
        if self.action == 'create':
            return NewPostSerializer
        elif self.action == 'list':
            return PostListSerializer
        else:
            return PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
