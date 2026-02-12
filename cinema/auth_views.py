from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from cinema.serializers import ReservationSerializer, ShowSerializer
from .auth_serializers import RegisterSerializer

@api_view(["POST"])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response(
        {"id": user.id, "username": user.username, "email": user.email},
        status=status.HTTP_201_CREATED
    )
    
    
@api_view(["GET"])
@permission_classes([AllowAny])
def listShow_view(request):
    serializer = ShowSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    id_reservation = serializer.get_fields()
    return Response(
        {"id_reservation":id_reservation.id_reservation, "movie_title":id_reservation.movie_title, "room":id_reservation.room, "price":id_reservation.price, "available_seats":id_reservation.available_seats},
        status=status.HTTP_200_OK
    )   
    
    
@api_view(["GET"])
@permission_classes([AllowAny])
def listReservation_view(request):
    serializer = ShowSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    show_id = serializer.get_fields()
    return Response(
        {"id_reservation": show_id.id_reservation, "movie_title":show_id.movie_title,"room":show_id.room,"price":show_id.price,"available_seats":show_id.avaliable_seats},
        status=status.HTTP_200_OK
    )   
    
    
@api_view(["POST"])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    show_id = serializer.save()
    return Response(
        {"id_reservation": show_id.id_reservation, "movie_title":show_id.movie_title,"room":show_id.room,"price":show_id.price,"available_seats":show_id.avaliable_seats},
        status=status.HTTP_201_CREATED
    )
    