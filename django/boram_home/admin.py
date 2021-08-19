from django.contrib import admin
from .models import *

# Register your models here.
class ResponseAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name', 'gubun', 'kk1', 'reg_date' ]

admin.site.register(Response, ResponseAdmin)