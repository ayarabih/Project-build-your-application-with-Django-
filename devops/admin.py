from django.contrib import admin
from .models import Student, Track
# Register your models here.

class customstudent(admin.ModelAdmin):
    fieldsets = (
        ['student information', {'fields' :['fname','lname','age']}],
        ['scholarship information', {'fields' :['student_track']}]
        )
    list_display = ('fname','lname','age','student_track', 'is_graduated')
    list_filter = ['student_track']
    search_fields = ['fname']
class InlineStudent(admin.StackedInline):
    model = Student
    extra = 2

class customTrack(admin.ModelAdmin):
    inlines = [InlineStudent]

admin.site.register(Student, customstudent) 
admin.site.register(Track, customTrack)
