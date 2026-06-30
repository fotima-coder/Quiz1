from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from .permissions import IsAdmin
from .models import User
from .serializers import TeacherSerializer, GroupSerializer
from main.models import Group

class TeacherListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdmin]

    queryset = User.objects.filter(role = "Teacher")
    serializer_class = TeacherSerializer

class TeacherUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdmin]
    queryset = User.objects.filter(role = "Teacher")
    serializer_class = TeacherSerializer

class GroupListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdmin]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdmin]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer