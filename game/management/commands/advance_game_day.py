from django.core.management.base import BaseCommand
from django.utils import timezone
from game.models import Image
from game.tasks import generate_daily_image

class Command(BaseCommand):
    help = 'Advances the game to a new day for testing purposes'

    def handle(self, *args, **options):
        latest_date = Image.objects.latest('created_at').created_at
        new_date = latest_date + timezone.timedelta(days=1)
        
        # Update the date of undescribed images to the new date
        Image.objects.filter(has_been_described=False).update(created_at=new_date)
        
        # Generate a new image for the new day
        generate_daily_image()
        
        self.stdout.write(self.style.SUCCESS(f'Successfully advanced the game to {new_date}'))
