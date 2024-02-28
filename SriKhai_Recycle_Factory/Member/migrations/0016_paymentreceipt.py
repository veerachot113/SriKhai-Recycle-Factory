# Generated by Django 5.0.2 on 2024-02-28 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Member", "0015_remove_recyclepurchase_has_bag_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentReceipt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("receipt_image", models.ImageField(upload_to="receipts/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Member.recyclepurchase",
                    ),
                ),
            ],
        ),
    ]
