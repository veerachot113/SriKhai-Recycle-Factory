# Generated by Django 5.0.2 on 2024-02-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0005_recycletype_delete_garbagetype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WastePurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='waste_purchases/')),
                ('address', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('waste_types', models.CharField(choices=[('Bottle', 'ขวด'), ('Bag', 'ถุง'), ('Crate', 'ลัง'), ('Glass bottle', 'ขวดแก้ว'), ('Paper', 'กระดาษ'), ('Can', 'กระป๋อง')], max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='RecyclePurchase',
        ),
        migrations.DeleteModel(
            name='RecycleType',
        ),
    ]
