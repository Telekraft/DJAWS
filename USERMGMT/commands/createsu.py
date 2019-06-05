from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username="tlk").exists():
            User.objects.create_superuser("tlk", "tlk@telekraft.dev", "inyourface")
