from django.urls import path, include
from .views import (
    MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView,
    CinemaListCreateAPIView, CinemaRetrieveUpdateDestroyAPIView,
    RoomListCreateAPIView, RoomRetrieveUpdateDestroyAPIView,
    SeatListCreateAPIView, SeatRetrieveUpdateDestroyAPIView,
    ShowtimeListCreateAPIView, ShowtimeRetrieveUpdateDestroyAPIView,
    TicketListCreateAPIView, TicketRetrieveUpdateDestroyAPIView,
    FeedbackListCreateAPIView, FeedbackRetrieveUpdateDestroyAPIView,
    DiscountListCreateAPIView, DiscountRetrieveUpdateDestroyAPIView
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Cinema API",
        default_version='v1',
        description="API documentation for the Cinema project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@cinema.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),

    path('cinemas/', CinemaListCreateAPIView.as_view(), name='cinema-list-create'),
    path('cinemas/<int:pk>/', CinemaRetrieveUpdateDestroyAPIView.as_view(), name='cinema-detail'),

    path('rooms/', RoomListCreateAPIView.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/', RoomRetrieveUpdateDestroyAPIView.as_view(), name='room-detail'),

    path('seats/', SeatListCreateAPIView.as_view(), name='seat-list-create'),
    path('seats/<int:pk>/', SeatRetrieveUpdateDestroyAPIView.as_view(), name='seat-detail'),

    path('showtimes/', ShowtimeListCreateAPIView.as_view(), name='showtime-list-create'),
    path('showtimes/<int:pk>/', ShowtimeRetrieveUpdateDestroyAPIView.as_view(), name='showtime-detail'),

    path('tickets/', TicketListCreateAPIView.as_view(), name='ticket-list-create'),
    path('tickets/<int:pk>/', TicketRetrieveUpdateDestroyAPIView.as_view(), name='ticket-detail'),

    path('feedback/', FeedbackListCreateAPIView.as_view(), name='feedback-list-create'),
    path('feedback/<int:pk>/', FeedbackRetrieveUpdateDestroyAPIView.as_view(), name='feedback-detail'),

    path('discounts/', DiscountListCreateAPIView.as_view(), name='discount-list-create'),
    path('discounts/<int:pk>/', DiscountRetrieveUpdateDestroyAPIView.as_view(), name='discount-detail'),

    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = [
    path('api/', include(urlpatterns)),
]
