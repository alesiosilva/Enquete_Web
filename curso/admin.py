from .models import Course
from django.contrib import admin

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_date', 'updated_date']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Course, CourseAdmin)