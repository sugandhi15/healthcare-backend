from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet automatically provides:
    - POST   /api/patients/        -> create
    - GET    /api/patients/        -> list
    - GET    /api/patients/<id>/   -> retrieve
    - PUT    /api/patients/<id>/   -> update
    - PATCH  /api/patients/<id>/   -> partial update
    - DELETE /api/patients/<id>/   -> destroy
    """

    serializer_class = PatientSerializer

    def get_queryset(self):
        """
        Return only patients created by the currently authenticated user.
        This ensures users can access only their own patient records.
        """
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically set the logged-in user as the creator
        when a new patient is added.
        """
        serializer.save(created_by=self.request.user)