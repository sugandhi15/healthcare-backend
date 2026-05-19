from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    """
    Provides complete CRUD operations for doctors.

    Endpoints generated automatically:
    - POST   /api/doctors/
    - GET    /api/doctors/
    - GET    /api/doctors/<id>/
    - PUT    /api/doctors/<id>/
    - PATCH  /api/doctors/<id>/
    - DELETE /api/doctors/<id>/
    """

    queryset = Doctor.objects.all().order_by("-created_at")
    serializer_class = DoctorSerializer

    permission_classes = [IsAuthenticated]