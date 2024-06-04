from rest_framework import serializers
from .models import Movie, Cinema, Room, Seat, Showtime, Ticket, Feedback, Discount
from django.utils import timezone

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'is_active', 'rating', 'poster_image', 'trailer_url']

    def validate_release_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Release date cannot be in the future.")
        return value

    def create(self, validated_data):
        validated_data['title'] = validated_data['title'].title()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'release_date' in validated_data and validated_data['release_date'] > timezone.now().date():
            raise serializers.ValidationError("Release date cannot be in the future.")
        return super().update(instance, validated_data)

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['id', 'name', 'address', 'contact_info', 'opening_hours']

    def validate_contact_info(self, value):
        if not value.startswith('+'):
            raise serializers.ValidationError("Contact info should start with a country code.")
        return value

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'cinema', 'name', 'capacity']

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'room', 'number', 'is_reserved']

class ShowtimeSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    cinema_name = serializers.CharField(source='room.cinema.name', read_only=True)
    room_name = serializers.CharField(source='room.name', read_only=True)

    class Meta:
        model = Showtime
        fields = ['id', 'movie', 'movie_title', 'room', 'cinema_name', 'room_name', 'time']

class TicketSerializer(serializers.ModelSerializer):
    showtime_details = serializers.CharField(source='showtime.__str__', read_only=True)
    seat_number = serializers.IntegerField(source='seat.number', read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'showtime', 'showtime_details', 'seat', 'seat_number', 'price', 'purchased_by', 'purchase_date', 'payment_method']

class FeedbackSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'user', 'user_name', 'message', 'created_at']

class DiscountSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Discount
        fields = ['id', 'user', 'user_name', 'amount', 'description', 'created_at']
