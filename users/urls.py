from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('teachers/', TeacherListCreateAPIView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/',TeacherUpdateDestroyAPIView.as_view(), name='teacher-detail'),
    path('groups/', GroupListCreateAPIView.as_view(), name='group-list-create'),
    path('groups/<int:pk>/', GroupRetrieveUpdateDestroyAPIView.as_view(), name='group-detail'),
]