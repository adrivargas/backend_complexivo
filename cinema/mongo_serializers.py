from rest_framework import serializers

class MovieCatalogSerializer(serializers.Serializer):
    movie_title = serializers.CharField(max_length=120)
    genre = serializers.CharField(required=False, allow_blank=True)
    duration_min = serializers.IntegerField(required=False)
    is_active = serializers.BooleanField(default=True)

class ReservationEventsSerializer(serializers.Serializer):
    reservation_id = serializers.IntegerField()      
    event_type = serializers.CharField()       
    class event_type_string(serializers.MultipleChoiceField):
        CREATED = "creada", "Creada"
        CONFIRMED = "confirmado", "Confirmado"
        CANCELLED = "cancelado", "Cancelado"
        CHECKED_IN = "llegada", "Llegada"
    estado = serializers.CharField(
        max_length=20,
        default=event_type_string.CREATED
    )
    class source_string(serializers.MultipleChoiceField):
        WEB = "web", "Web"
        MOBILE = "movil", "Movil"
        SYSTEM = "sistema", "Sistema"
    estado = serializers.CharField(
        max_length=20,
        # choices=source_string.choices,
        default=source_string.SYSTEM
    )
    note = serializers.CharField(required=False)
    created_at = serializers.DateField(auto_now_add=True)