from rest_framework import serializers
from .models import Course , User

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = ['id' , 'email' , 'username' , 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class CourseSerializer(serializers.ModelSerializer) :
    class Meta :
        model  = Course
        fields = "__all__" 

