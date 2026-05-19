from django.urls import path
from .views import PatientDoctorMappingViewSet

# Create viewset shortcuts
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
    # POST /api/mappings/
    # GET  /api/mappings/
    path("", mapping_list, name="mapping-list"),

    # GET /api/mappings/<patient_id>/
    path("<int:patient_id>/", mapping_by_patient, name="mapping-by-patient"),

    # DELETE /api/mappings/delete/<id>/
    path("delete/<int:pk>/", mapping_detail, name="mapping-delete"),
]