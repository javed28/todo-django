from rest_framework import serializers
from .models import Blog,Comment

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogsSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True,read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
