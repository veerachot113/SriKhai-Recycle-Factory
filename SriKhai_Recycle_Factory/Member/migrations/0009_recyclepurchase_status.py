# Generated by Django 5.0.2 on 2024-02-24 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0008_remove_recyclepurchase_types_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recyclepurchase',
            name='status',
            field=models.CharField(blank=True, choices=[('กำลังดำเนินการ', 'กำลังดำเนินการ'), ('กำลังเข้ารับ', 'กำลังเข้ารับ'), ('รับแล้ว', 'รับแล้ว'), ('ตรวจสอบขยะ', 'ตรวจสอบขยะ'), ('รอชำระเงิน', 'รอชำระเงิน'), ('เสร็จสิ้น', 'เสร็จสิ้น'), ('ยกเลิก', 'ยกเลิก')], max_length=200, null=True),
        ),
    ]