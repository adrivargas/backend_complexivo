from django.db import models

class Show(models.Model):
    id_reservation = models.IntegerField()
    movie_title = models.CharField(max_length=120)
    room = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    available_seats = models.IntegerField()

    def __str__(self):
        return f"{self.id_reservation} {self.movie_title} {self.room} {self.price} {self.available_seats}"

class Reservations(models.Model):
    show_id = models.ForeignKey(Show, on_delete=models.PROTECT, related_name="reservation")
    customer_name = models.CharField(max_length=120)
    seats = models.IntegerField()
    class Estado(models.TextChoices):
        RESERVED = "reservado", "Reservado"
        CONFIRMED = "confirmado", "Confirmado"
        CANCELLED = "cancelado", "Cancelado"
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.RESERVED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.show_id.id_reservation} {self.customer_name} {self.seats} {self.status} {self.created_at}"
    
