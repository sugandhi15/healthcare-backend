from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet

# Create router
router = DefaultRouter()

# Register the DoctorViewSet
router.register("", DoctorViewSet, basename="doctor")

# Export URLs
urlpatterns = router.urls