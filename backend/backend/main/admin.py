from django.contrib import admin
from .models import User, Note
# Register your models here.

admin.site.register(Note)
admin.site.register(User )