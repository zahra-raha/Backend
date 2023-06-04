from django.contrib import admin
from userprofile.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = "user", "phonenumber"    
    search_fields = "user__first_name", "user__last_name", "user__username"
    list_filter = "user__is_active",
    
