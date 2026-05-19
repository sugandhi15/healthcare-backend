from rest_framework import serializers
from .models import PatientDoctorMapping


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    """
    Serializer for mapping patients to doctors.
    """

    class Meta:
        model = PatientDoctorMapping
        fields = [
            "id",
            "patient",
            "doctor",
            "assigned_at",
        ]
        read_only_fields = [
            "id",
            "assigned_at",
        ]