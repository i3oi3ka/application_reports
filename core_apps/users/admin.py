from django.contrib import admin
from core_apps.users.models import User, UserProfile

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
