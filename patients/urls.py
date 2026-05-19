from rest_framework.routers import DefaultRouter
from .views import PatientViewSet

# Create a router object
router = DefaultRouter()

# Register the PatientViewSet with the router
# This automatically generates all CRUD URLs
router.register("", PatientViewSet, basename="patient")

# Export the generated URL patterns
urlpatterns = router.urls