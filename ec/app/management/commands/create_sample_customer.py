from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Customer

class Command(BaseCommand):
    help = 'Create a sample customer address for testing'

    def handle(self, *args, **options):
        # Get or create a test user
        user, created = User.objects.get_or_create(
            username='testuser',
            defaults={
                'email': 'test@example.com',
                'first_name': 'Test',
                'last_name': 'User'
            }
        )
        
        if created:
            user.set_password('testpass123')
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f'Created test user: {user.username}')
            )
        
        # Create a sample customer address
        customer, created = Customer.objects.get_or_create(
            user=user,
            defaults={
                'name': 'Test Customer',
                'locality': '123 Main Street',
                'city': 'Test City',
                'mobile': 1234567890,
                'zipcode': 12345,
                'state': 'Maharashtra'
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Created customer address for {user.username}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Customer address already exists for {user.username}')
            )

        self.stdout.write(
            self.style.SUCCESS('Sample customer setup complete!')
        )
        self.stdout.write(
            self.style.WARNING('You can now login with username: testuser, password: testpass123')
        )
