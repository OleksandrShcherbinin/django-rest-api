from threading import Thread
from .autobot import AutoBot


def start_auto_bot(modeladmin, request, queryset):
    auto = AutoBot()
    bots = [auto]
    for _ in range(auto.number_of_users - 1):
        auto_bot = AutoBot()
        bots.append(auto_bot)
    for obj in bots:
        Thread(target=obj.user_sign_up, args=()).start()


start_auto_bot.short_description = 'AUTOBOT START'
