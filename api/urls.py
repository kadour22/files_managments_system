from django.urls import path
from .views import CourseFileDownloadView, CourseListAPIView , CourseCreateView , UserCreateView , Protected_Endpoint
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', UserCreateView.as_view(), name='UserCreateView'),

    path('courses/create/', CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:course_id>/download/', CourseFileDownloadView.as_view(), name='course-file-download'),
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('protected/', Protected_Endpoint.as_view(), name='protected-endpoint'),
]