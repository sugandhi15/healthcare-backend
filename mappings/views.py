from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer


class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    """
    CRUD APIs for patient-doctor assignments.
    """

    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        ).select_related("patient", "doctor")

        patient_id = self.kwargs.get("patient_id")
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)

        return queryset