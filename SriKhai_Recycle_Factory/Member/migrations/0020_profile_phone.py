# Generated by Django 5.0.2 on 2024-03-01 15:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Member", "0019_remove_recyclepurchase_receipt_slip_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="phone",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]