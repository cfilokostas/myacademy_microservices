from django.contrib import admin
from .models import Course
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('level', 'category')
    list_display = ('title', 'instructor', 'created_at',
                    'updated_at', 'price', 'duration', 'level', 'category', 'rating', 'enrollment_count')
    search_fields = ('title', 'description', 'instructor',
                     'category', 'level', 'rating', 'enrollment_count')


admin.site.register(Course, CourseAdmin)
