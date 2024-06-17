<<<<<<< HEAD
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Movie, Cinema, Room, Seat, Showtime, Ticket, Feedback, Discount, Review, User
from .serializers import MovieSerializer, CinemaSerializer, RoomSerializer, SeatSerializer, ShowtimeSerializer, TicketSerializer, FeedbackSerializer, DiscountSerializer, ReviewSerializer, UserSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
=======
from rest_framework import generics
from .models import Movie, Cinema, Room, Seat, Showtime, Ticket, Feedback, Discount, PurchaseHistory
from .serializers import MovieSerializer, CinemaSerializer, RoomSerializer, SeatSerializer, ShowtimeSerializer, TicketSerializer, FeedbackSerializer, DiscountSerializer, PurchaseHistorySerializer
>>>>>>> 02bb152a1c2a2d7e009c8be31241d1d8a59643c5

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

<<<<<<< HEAD
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @method_decorator(cache_page(60*15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class CinemaViewSet(viewsets.ModelViewSet):
=======
class CinemaListCreateView(generics.ListCreateAPIView):
>>>>>>> 02bb152a1c2a2d7e009c8be31241d1d8a59643c5
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

class CinemaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

<<<<<<< HEAD
    @method_decorator(cache_page(60*15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class RoomViewSet(viewsets.ModelViewSet):
=======
class RoomListCreateView(generics.ListCreateAPIView):
>>>>>>> 02bb152a1c2a2d7e009c8be31241d1d8a59643c5
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class SeatListCreateView(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class SeatRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class ShowtimeListCreateView(generics.ListCreateAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer

class ShowtimeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer

class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class DiscountListCreateView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

<<<<<<< HEAD
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
=======
class DiscountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class PurchaseHistoryListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer

class PurchaseHistoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer
>>>>>>> 02bb152a1c2a2d7e009c8be31241d1d8a59643c5
