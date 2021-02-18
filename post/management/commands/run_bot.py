from django.core.management.base import BaseCommand

from post.autobot import run


class Command(BaseCommand):
    help = 'Runs AUTO BOT'

    def handle(self, *args, **kwargs):
        run()
        self.stdout.write("AUTO BOT IS RUNNING")
