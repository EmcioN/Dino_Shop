from django.core.management.base import BaseCommand
from home.scrapers import fetch_patch_notes
from home.models import PatchNote

class Command(BaseCommand):
    help = 'Updates the patch notes from the ARK wiki'

    def handle(self, *args, **kwargs):
        notes = fetch_patch_notes()
        for note in notes:            
            PatchNote.objects.update_or_create(title=note['title'], defaults={'content': note['content']})