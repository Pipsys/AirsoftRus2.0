from django.db import migrations

def create_initial_categories(apps, schema_editor):
    Category = apps.get_model('shop', 'Category')
    Category.objects.get_or_create(name='Страйкбольное оружие', slug='straykbolnoe-oruzhie')
    Category.objects.get_or_create(name='Снаряжение', slug='snaryazhenie')
    Category.objects.get_or_create(name='Защита', slug='zashchita')
    Category.objects.get_or_create(name='Аккамуляторы', slug='akkumulyatory')

class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_categories),
    ]
