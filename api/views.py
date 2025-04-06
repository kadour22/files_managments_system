from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions , generics
from django.http import Http404
from django.http import FileResponse
from django.urls import reverse
from .models import Course
from .serializers import CourseSerializer , UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class CourseCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CourseSerializer

class CourseFileDownloadView(APIView):
    permission_classes = [permissions.AllowAny]  

    def get(self, request, course_id, *args, **kwargs):
        try:
            course = Course.objects.get(id=course_id)
            file_path = course.file.path  
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=course.file.name)
        except Course.DoesNotExist:
            raise Http404("Course not found")
        except Exception as e:
            return Response({"error": str(e)}, status=500)

class CourseListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Changed to IsAuthenticated

    def get(self, request, *args, **kwargs):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        for course in serializer.data:
            course_id = course['id']
            course['download_url'] = request.build_absolute_uri(
                reverse('course-file-download', args=[course_id])
            )
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserCreateView(APIView):

    def post(self , request , *args , **kwargs) :
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Protected_Endpoint(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({"message": f"Mr {user}u have access to  protected endpoint."}, status=status.HTTP_200_OK)