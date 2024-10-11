from django.core.management.base import BaseCommand
from game.tasks import generate_daily_image

class Command(BaseCommand):
    help = 'Generates the daily image'

    def handle(self, *args, **options):
        generate_daily_image()
        self.stdout.write(self.style.SUCCESS('Successfully generated daily image'))
