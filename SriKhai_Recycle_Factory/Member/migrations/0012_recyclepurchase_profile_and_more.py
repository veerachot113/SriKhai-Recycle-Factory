# Generated by Django 5.0.2 on 2024-02-25 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Member", "0011_alter_recyclepurchase_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="recyclepurchase",
            name="profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Member.profile",
            ),
        ),
        migrations.AlterField(
            model_name="recyclepurchase",
            name="address",
            field=models.TextField(),
        ),
    ]
