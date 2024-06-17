# CinematicConfig/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Cinema API",
        default_version='v1',
        description="API documentation for Cinema project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@cinema.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cinema.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


# # urls.py
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions
# from cinema.views import MovieViewSet, CinemaViewSet, RoomViewSet, SeatViewSet, ShowtimeViewSet, TicketViewSet, FeedbackViewSet, DiscountViewSet, PurchaseHistoryViewSet

# router = DefaultRouter()
# router.register(r'movies', MovieViewSet)
# router.register(r'cinemas', CinemaViewSet)
# router.register(r'rooms', RoomViewSet)
# router.register(r'seats', SeatViewSet)
# router.register(r'showtimes', ShowtimeViewSet)
# router.register(r'tickets', TicketViewSet)
# router.register(r'feedback', FeedbackViewSet)
# router.register(r'discounts', DiscountViewSet)
# router.register(r'purchase_histories', PurchaseHistoryViewSet)

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Cinema API",
#         default_version='v1',
#         description="API documentation for Cinema project",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@cinema.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]
