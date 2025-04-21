from django.contrib import admin

# Register your models here.
from .models import User


class userAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_student', 'is_teacher', 'is_admin')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_student', 'is_teacher', 'is_admin')


admin.site.register(User, userAdmin)
