from rest_framework.serializers import ModelSerializer

from blogs.models import Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'image', 'intro', 'pub_date']


class NewPostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'category', 'intro', 'image', 'post_body']


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
