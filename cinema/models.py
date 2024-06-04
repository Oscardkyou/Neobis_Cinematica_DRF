from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    is_active = models.BooleanField(default=True)
    rating = models.FloatField(default=0.0)
    poster_image = models.URLField(null=True, blank=True)
    trailer_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class Cinema(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=100)
    opening_hours = models.CharField(max_length=100, default='9:00 AM - 11:00 PM')

    def __str__(self):
        return self.name

class Room(models.Model):
    cinema = models.ForeignKey(Cinema, related_name='rooms', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cinema.name} - {self.name}"

class Seat(models.Model):
    room = models.ForeignKey(Room, related_name='seats', on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f"Room {self.room.name} - Seat {self.number}"

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, related_name='showtimes', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='showtimes', on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} - {self.room.name} at {self.time}"

class Ticket(models.Model):
    showtime = models.ForeignKey(Showtime, related_name='tickets', on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, related_name='ticket', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    purchased_by = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Ticket for {self.showtime} - Seat {self.seat.number}"

class Feedback(models.Model):
    user = models.ForeignKey(User, related_name='feedback', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username} at {self.created_at}"

class Discount(models.Model):
    user = models.ForeignKey(User, related_name='discounts', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Discount of {self.amount} for {self.user.username}"
