from django.urls import path
from .views import PatientDoctorMappingViewSet

mapping_list = PatientDoctorMappingViewSet.as_view({
    "get": "list",
    "post": "create",
})

mapping_detail = PatientDoctorMappingViewSet.as_view({
    "delete": "destroy",
})

mapping_by_patient = PatientDoctorMappingViewSet.as_view({
    "get": "list",
})

urlpatterns = [
    path("", mapping_list, name="mapping-list"),

    path("<int:patient_id>/", mapping_by_patient, name="mapping-by-patient"),

    path("delete/<int:pk>/", mapping_detail, name="mapping-delete"),
]