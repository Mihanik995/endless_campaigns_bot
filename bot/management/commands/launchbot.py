import asyncio

from django.core.management import BaseCommand

from users.views import bot


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        asyncio.run(bot.polling())
