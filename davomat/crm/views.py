from rest_framework import viewsets, permissions
from .models import Staff, Position, Shift, StaffShift, StaffAttendance
from .serializers import StaffSerializer, PositionSerializer, ShiftSerializer,StaffShiftSerializer, StaffAttendanceSerializer


class IsStaffUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff

class IsAuthenticatedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsStaffUser]
        else:
            permission_classes = [IsAuthenticatedUser]
        return [permission() for permission in permission_classes]


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsStaffUser]
        else:
            permission_classes = [IsAuthenticatedUser]
        return [permission() for permission in permission_classes]


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsStaffUser]
        elif self.action == 'list':
            permission_classes = [IsStaffUser]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsStaffUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class StaffShiftViewSet(viewsets.ModelViewSet):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsStaffUser]
        elif self.action == 'list':
            permission_classes = [IsStaffUser]
        else:
            permission_classes = [IsStaffUser]
        return [permission() for permission in permission_classes]


class StaffAttendanceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticatedUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return StaffAttendance.objects.all()
        else:
            staff = Staff.objects.filter(user=user).first()
            if staff:
                return StaffAttendance.objects.filter(staff=staff)
            else:
                return StaffAttendance.objects.none()
