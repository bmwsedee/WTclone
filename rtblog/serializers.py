from rest_framework import serializers
from talk.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_date')
