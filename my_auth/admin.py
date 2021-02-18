from django.contrib import admin
from django.contrib.auth.models import User

from .models import Profile


class ProfileInline(admin.TabularInline):
    model = Profile
    fields = ('info',)
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
