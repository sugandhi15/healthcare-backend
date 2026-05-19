from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient

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

        read_only_fields = [
            "id",
            "created_by",
            "created_at",
        ]