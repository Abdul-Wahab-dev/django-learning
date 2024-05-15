from django.contrib import admin
from .models import Course
@admin.register(Course)
class Admincourse(admin.ModelAdmin):
    list_display = ('id' , 'name')

# admin.site.register(Course , Admincourse)

