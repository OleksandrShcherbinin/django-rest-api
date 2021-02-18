from django.contrib import admin

from .models import Post, BotContentSource
from .actions import start_auto_bot


class BotContentSourceAdmin(admin.ModelAdmin):
    actions = (start_auto_bot,)


admin.site.register(Post)
admin.site.register(BotContentSource, BotContentSourceAdmin)
