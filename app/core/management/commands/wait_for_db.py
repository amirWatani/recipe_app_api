"""Django command to pause execution until database is available"""
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        pass