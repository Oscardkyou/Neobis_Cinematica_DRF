from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='cinema_users',  # Добавляем related_name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=('groups'),
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='cinema_users_permissions',  # Добавляем related_name
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )

    def __str__(self):
        return self.username

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    is_active = models.BooleanField(default=True)
    rating = models.FloatField(default=0.0)
    poster_image = models.ImageField(upload_to='posters/')
    trailer_url = models.URLField()

    def __str__(self):
        return self.title

class Cinema(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=50)
    opening_hours = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Room(models.Model):
    cinema = models.ForeignKey(Cinema, related_name='rooms', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Seat(models.Model):
    room = models.ForeignKey(Room, related_name='seats', on_delete=models.CASCADE)
    number = models.IntegerField()
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f'Seat {self.number} in {self.room.name}'

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, related_name='showtimes', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='showtimes', on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f'{self.movie.title} at {self.time} in {self.room.name}'

class Ticket(models.Model):
    showtime = models.ForeignKey(Showtime, related_name='tickets', on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, related_name='ticket', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_by = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f'Ticket for {self.showtime} in {self.seat.number}'

class Feedback(models.Model):
    user = models.ForeignKey(User, related_name='feedback', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback from {self.user.username}'

class Discount(models.Model):
    code = models.CharField(max_length=50, default='DEFAULT_CODE_VALUE')
    description = models.TextField()
    discount_percentage = models.FloatField(default=0.0)  # Provide a default value
    valid_until = models.DateField()

    def __str__(self):
        return f'Discount {self.code}'


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.movie.title}'
