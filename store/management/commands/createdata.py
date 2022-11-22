import random
import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from store.models import Product
from category.models import Category



CATEGORIES = [
    "Meat & Fish",
    "Dairy",
    "Vegetables and fruit",
    "Ice Cream",
    "Bread & bread spreads",
    "Dried Goods",
    "Snacks",
    "Care Products"
]


PRODUCTS = [
    "Turmeric powder - 100 gms",
    "Sugar - 1 kg",
    "Salt - 1 kg",
    "Rice - 5-7 kgs",
    "Raw rice - 5-7 kgs",
    "Energy Bar - 100 gms",
    "Dry fruits - 250 gms",
    "Vanilla Icecream - 500 gms",
    "Curd - 1 kgs",
    "Basmati rice - 1 to 2 kgs",
    "Milk - 1 litre",
    "croissant - 200 gms",
    "Wheat flour - 2 kgs",
    "Peanut butter - 1/2 kg",
    "Strawberries - 1 kg",
    "Oats - 1/2 kg",
    "Bananas - 1/2 kg",
    "Oranges - 1/2 kg",
    "Aples - 1 kg",
    "Tomatoes - 1 kg",
    "Potatoes - 1 kg (optional)",
    "Greenpeas - 500 gms",
    "Burger - 1 packet big",
    "Noodles -1 big packet",
    "Sago - 1/2 kg",
    "Tamarind - 1/2 kg",
    "chilli powder - 1/2 kg"
]


class Provider(faker.providers.BaseProvider):
    def ecommerce_category(self):
        return self.random_element(CATEGORIES)

    def ecommerce_products(self):
        return self.random_element(PRODUCTS)


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):

        fake = Faker(["en_US"])
        fake.add_provider(Provider)

        if Category.objects.all().count() == 0:
            for _ in range(8):
                d = fake.unique.ecommerce_category()
                Category.objects.create(category_name=d)
    
        for _ in range(20):
            items = list(Category.objects.all())
            random_item = random.choice(items)
            Product.objects.create(
                product_name=fake.unique.ecommerce_products(),
                description=fake.text(max_nb_chars=100),
                price= random.randint(100, 1500),
                category_id=random_item.id,
            )

        check_products = Product.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of products: {check_products}"))