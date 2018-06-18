from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from blogs.models import Post
from blogs.permissions import PostPermissions
from blogs.serializers import PostListSerializer, PostDetailSerializer, NewPostSerializer


# class PostViewSet(ModelViewSet):
#     queryset = Post.objects.all()
#     permission_classes = [PostPermissions]
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ['title', 'image', 'intro', 'pub_date']
#     ordering = ['-pub_date']
#     ordering_fields = ['title', 'pub_date']
#
#     def get_serializer_class(self):
#         return PostDetailSerializer

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


class MyPostsAPI(ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)
