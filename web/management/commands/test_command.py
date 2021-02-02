from django.core.management.base import BaseCommand

from web import models


class Command(BaseCommand):

    def handle(self, *args, **options):
        models.CronNote.objects.create()
