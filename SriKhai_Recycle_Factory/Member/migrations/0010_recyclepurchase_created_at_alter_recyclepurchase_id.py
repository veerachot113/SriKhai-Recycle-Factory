# Generated by Django 5.0.2 on 2024-02-24 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0009_recyclepurchase_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='recyclepurchase',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='recyclepurchase',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
