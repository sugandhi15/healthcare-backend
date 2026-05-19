from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    """
    Serializer for Doctor model.
    Converts Doctor objects to JSON and validates incoming data.
    """

    class Meta:
        model = Doctor
        fields = [
            "id",
            "name",
            "specialization",
            "experience",
            "contact",
            "email",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]