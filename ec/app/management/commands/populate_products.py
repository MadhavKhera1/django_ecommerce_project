from django.core.management.base import BaseCommand
from ec.app.models import Product

class Command(BaseCommand):
    help = 'Populate database with sample products'

    def handle(self, *args, **options):
        products = [
            {
                'title': 'Fresh Cow Milk',
                'selling_price': 60.0,
                'discounted_price': 50.0,
                'description': 'Pure and fresh cow milk, rich in calcium and protein. Perfect for daily consumption.',
                'composition': '100% Pure Cow Milk',
                'prodapp': 'Fresh Dairy Product',
                'category': 'ML',
                'product_image': 'product/cow-milk.png'
            },
            {
                'title': 'Buffalo Ghee',
                'selling_price': 800.0,
                'discounted_price': 750.0,
                'description': 'Pure buffalo ghee made from traditional methods. Rich in taste and aroma.',
                'composition': '100% Pure Buffalo Ghee',
                'prodapp': 'Traditional Ghee',
                'category': 'GH',
                'product_image': 'product/buffalo-ghee.png'
            },
            {
                'title': 'Premium Curd',
                'selling_price': 45.0,
                'discounted_price': 40.0,
                'description': 'Thick and creamy curd made from fresh milk. Perfect for breakfast and snacks.',
                'composition': 'Fresh Milk Curd',
                'prodapp': 'Dairy Product',
                'category': 'CR',
                'product_image': 'product/curd-premium.png'
            },
            {
                'title': 'Sweet Lassi',
                'selling_price': 35.0,
                'discounted_price': 30.0,
                'description': 'Refreshing sweet lassi made with fresh yogurt and natural sweeteners.',
                'composition': 'Yogurt, Sugar, Cardamom',
                'prodapp': 'Beverage',
                'category': 'LS',
                'product_image': 'product/sweet-lassi.png'
            },
            {
                'title': 'Chocolate Milkshake',
                'selling_price': 50.0,
                'discounted_price': 45.0,
                'description': 'Rich and creamy chocolate milkshake made with real chocolate.',
                'composition': 'Milk, Chocolate, Sugar',
                'prodapp': 'Beverage',
                'category': 'MS',
                'product_image': 'product/milk-shake-chocolate.png'
            },
            {
                'title': 'Fresh Paneer',
                'selling_price': 200.0,
                'discounted_price': 180.0,
                'description': 'Soft and fresh paneer made from pure milk. Perfect for cooking.',
                'composition': '100% Pure Milk Paneer',
                'prodapp': 'Fresh Dairy',
                'category': 'PN',
                'product_image': 'product/paneer-fresh.png'
            },
            {
                'title': 'Mozzarella Cheese',
                'selling_price': 300.0,
                'discounted_price': 280.0,
                'description': 'Premium mozzarella cheese perfect for pizzas and pasta.',
                'composition': 'Milk, Salt, Rennet',
                'prodapp': 'Cheese Product',
                'category': 'CZ',
                'product_image': 'product/mozzarellacheese.png'
            },
            {
                'title': 'Vanilla Ice Cream',
                'selling_price': 80.0,
                'discounted_price': 70.0,
                'description': 'Creamy vanilla ice cream made with real vanilla extract.',
                'composition': 'Milk, Cream, Vanilla, Sugar',
                'prodapp': 'Frozen Dessert',
                'category': 'IC',
                'product_image': 'product/kulfi.png'
            }
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(
                title=product_data['title'],
                defaults=product_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created product: {product.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Product already exists: {product.title}')
                )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated products!')
        )
