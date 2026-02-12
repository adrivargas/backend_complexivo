from rest_framework import serializers
from .models import Show,Reservations

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = ["id_reservation", "movie_title","room","price","available_seats"]

class ReservationSerializer(serializers.ModelSerializer):
    reservation_name = serializers.CharField(source="show_id.id_reservation", read_only=True)

    class Meta:
        model = Reservations
        fields = ["show_id","customer_name","seats","estado","created_at"]
