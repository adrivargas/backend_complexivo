from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Show,Reservations
from .serializers import ShowSerializer,ReservationSerializer
from .permissions import IsAdminOrReadOnly

class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all().order_by("id_reservation")
    serializer_class = ShowSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["movie_title"]
    ordering_fields = ["id_reservation", "movie_title"]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservations.objects.select_related("customer_name").all().order_by("show_id")
    serializer_class = ReservationSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["customer_name"]
    search_fields = ["show_id"]
    ordering_fields = ["show_id","customer_name","seats","estado","created_at"]

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     status = self.request.query_params.get("status")
    #     anio_max = self.request.query_params.get("anio_max")
    #     if anio_min:
    #         qs = qs.filter(anio__gte=int(anio_min))
    #     if anio_max:
    #         qs = qs.filter(anio__lte=int(anio_max))
    #     return qs

    def get_permissions(self):
        # Público: SOLO listar vehículos
        if self.action == "list":
            return [AllowAny()]
        return super().get_permissions()