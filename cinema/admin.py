from django.contrib import admin
from .models import Movie, Cinema, Room, Seat, Showtime, Ticket, Feedback, Discount

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'is_active', 'rating')
    list_filter = ('is_active', 'release_date')
    search_fields = ('title',)

@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_info', 'opening_hours')
    search_fields = ('name', 'address')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('cinema', 'name', 'capacity')
    list_filter = ('cinema',)
    search_fields = ('name',)

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('room', 'number', 'is_reserved')
    list_filter = ('room', 'is_reserved')

@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ('movie', 'room', 'time')
    list_filter = ('movie', 'room', 'time')
    search_fields = ('movie__title', 'room__name')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('showtime', 'seat', 'price', 'purchased_by', 'purchase_date', 'payment_method')
    list_filter = ('showtime', 'purchase_date', 'payment_method')
    search_fields = ('purchased_by__username',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount_percentage', 'valid_until')
    list_filter = ('valid_until',)
    search_fields = ('code', 'description')
