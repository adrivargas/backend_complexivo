from django.urls import path
from rest_framework.routers import DefaultRouter

from cinema.cinema_views import vehicle_services_detail, vehicle_services_list_create
from cinema.service_types_views import service_types_detail, service_types_list_create
from .views import ShowViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r"show", ShowViewSet, basename="show")
router.register(r"reservations", ReservationViewSet, basename="reservations")

urlpatterns = [
    # Mongo
    path("service-types/", service_types_list_create),
    path("service-types//", service_types_detail),
    path("vehicle-services/", vehicle_services_list_create),
    path("vehicle-services//", vehicle_services_detail),
]

urlpatterns += router.urls