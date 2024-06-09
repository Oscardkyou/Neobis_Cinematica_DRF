from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, CinemaViewSet, RoomViewSet, SeatViewSet, ShowtimeViewSet, TicketViewSet, FeedbackViewSet, DiscountViewSet, PurchaseHistoryViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'cinemas', CinemaViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'showtimes', ShowtimeViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'purchase_histories', PurchaseHistoryViewSet)

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
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


# from django.urls import path
# from .views import (
#     MovieListCreateView, MovieRetrieveUpdateDestroyView,
#     CinemaListCreateView, CinemaRetrieveUpdateDestroyView,
#     RoomListCreateView, RoomRetrieveUpdateDestroyView,
#     SeatListCreateView, SeatRetrieveUpdateDestroyView,
#     ShowtimeListCreateView, ShowtimeRetrieveUpdateDestroyView,
#     TicketListCreateView, TicketRetrieveUpdateDestroyView,
#     FeedbackListCreateView, FeedbackRetrieveUpdateDestroyView,
#     DiscountListCreateView, DiscountRetrieveUpdateDestroyView,
#     PurchaseHistoryListCreateView, PurchaseHistoryRetrieveUpdateDestroyView
# )

# urlpatterns = [
#     path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
#     path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
#     path('cinemas/', CinemaListCreateView.as_view(), name='cinema-list-create'),
#     path('cinemas/<int:pk>/', CinemaRetrieveUpdateDestroyView.as_view(), name='cinema-detail'),
#     path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
#     path('rooms/<int:pk>/', RoomRetrieveUpdateDestroyView.as_view(), name='room-detail'),
#     path('seats/', SeatListCreateView.as_view(), name='seat-list-create'),
#     path('seats/<int:pk>/', SeatRetrieveUpdateDestroyView.as_view(), name='seat-detail'),
#     path('showtimes/', ShowtimeListCreateView.as_view(), name='showtime-list-create'),
#     path('showtimes/<int:pk>/', ShowtimeRetrieveUpdateDestroyView.as_view(), name='showtime-detail'),
#     path('tickets/', TicketListCreateView.as_view(), name='ticket-list-create'),
#     path('tickets/<int:pk>/', TicketRetrieveUpdateDestroyView.as_view(), name='ticket-detail'),
#     path('feedbacks/', FeedbackListCreateView.as_view(), name='feedback-list-create'),
#     path('feedbacks/<int:pk>/', FeedbackRetrieveUpdateDestroyView.as_view(), name='feedback-detail'),
#     path('discounts/', DiscountListCreateView.as_view(), name='discount-list-create'),
#     path('discounts/<int:pk>/', DiscountRetrieveUpdateDestroyView.as_view(), name='discount-detail'),
#     path('purchase_histories/', PurchaseHistoryListCreateView.as_view(), name='purchasehistory-list-create'),
#     path('purchase_histories/<int:pk>/', PurchaseHistoryRetrieveUpdateDestroyView.as_view(), name='purchasehistory-detail'),
# ]


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import MovieViewSet, CinemaViewSet, RoomViewSet, SeatViewSet, ShowtimeViewSet, TicketViewSet, FeedbackViewSet, DiscountViewSet
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions

# router = DefaultRouter()
# router.register(r'movies', MovieViewSet)
# router.register(r'cinemas', CinemaViewSet)
# router.register(r'rooms', RoomViewSet)
# router.register(r'seats', SeatViewSet)
# router.register(r'showtimes', ShowtimeViewSet)
# router.register(r'tickets', TicketViewSet)
# router.register(r'feedback', FeedbackViewSet)
# router.register(r'discounts', DiscountViewSet)

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Cinema API",
#         default_version='v1',
#         description="API documentation for the Cinema project",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@cinema.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

# urlpatterns = [
#     path('', include(router.urls)),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]

