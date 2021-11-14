from .models import *
from django.contrib import admin

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_date', 'updated_date']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'email', 'phone', 'date')
    search_fields = ('name', 'email', 'phone')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'status', 'created_at', 'updated_at')

admin.site.register(Course, CourseAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)