from django.contrib import admin
from .models import Staff, Position, Shift, StaffShift, StaffAttendance

from django.contrib import admin
from .models import Position, Staff, Shift, StaffShift, StaffAttendance

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['user', 'position', 'is_staff']
    search_fields = ['user']
    list_filter = ['is_staff', 'position']

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_time', 'end_time']
    search_fields = ['name']

@admin.register(StaffShift)
class StaffShiftAdmin(admin.ModelAdmin):
    list_display = ['staff', 'shift', 'date']
    search_fields = ['staff']
    list_filter = ['date', ]

@admin.register(StaffAttendance)
class StaffAttendanceAdmin(admin.ModelAdmin):
    list_display = ['staff', 'date', 'status', 'staff_shift']
    search_fields = ['staff', 'status']
    list_filter = ['status', 'date']

    def staff_shift(self, obj):
        return obj.staff_shift()
    staff_shift.short_description = 'Shift'


