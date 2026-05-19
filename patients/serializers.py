from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient

        # Fields to include in API responses and requests
        fields = [
            "id",
            "created_by",
            "name",
            "age",
            "gender",
            "contact",
            "address",
            "created_at",
        ]

        # These fields are automatically set by the system
        # and cannot be modified directly by the user.
        read_only_fields = [
            "id",
            "created_by",
            "created_at",
        ]