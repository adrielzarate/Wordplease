from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from blogs.models import Post


class BlogsListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

    def to_representation(self, obj):
        return {
            'username': obj.username,
            'url': '/blogs/' + obj.username
        }


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'image', 'intro', 'pub_date']


class NewPostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'category', 'intro', 'image', 'post_body', 'pub_date']


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
