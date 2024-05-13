# Generated by Django 5.0.1 on 2024-02-10 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_address_cartorder_cartorderitem_category_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productreview',
            old_name='qty',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='productreview',
            old_name='descriptions',
            new_name='review',
        ),
        migrations.AddField(
            model_name='cartorderitem',
            name='invoice_no',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
