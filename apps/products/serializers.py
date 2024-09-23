from rest_framework import serializers
from .models import Lesson, Owner, Product, UserProduct, UserProductLesson
from apps.users.models import User


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'url_to_lesson', 'duration']


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'firstname', 'lastname']


class ProductSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'owner', 'lessons']

class UserProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = serializers.StringRelatedField()  # Display user as a string (from User model's __str__)

    class Meta:
        model = UserProduct
        fields = ['id', 'product', 'user']




class UserProductLessonSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    user_product = UserProductSerializer()

    class Meta:
        model = UserProductLesson
        fields = ['id', 'lesson', 'user_product', 'view_duration', 'watched']
