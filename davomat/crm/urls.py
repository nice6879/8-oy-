from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StaffViewSet, PositionViewSet, ShiftViewSet,
    StaffShiftViewSet, StaffAttendanceViewSet
)

router = DefaultRouter()
router.register('staff', StaffViewSet, basename='staff')
router.register('positions', PositionViewSet, basename='position')
router.register('shifts', ShiftViewSet, basename='shift')
router.register('staff-shifts', StaffShiftViewSet, basename='staffshift')
router.register('attendance', StaffAttendanceViewSet, basename='attendance')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]

