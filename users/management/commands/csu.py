from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user, _ = User.objects.get_or_create(email='admin@example.com')
        user.set_password('12345')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
