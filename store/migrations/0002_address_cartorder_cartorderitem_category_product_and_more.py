# Generated by Django 5.0.1 on 2024-01-28 15:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7777)),
                ('paid_status', models.BooleanField(blank=True, default=False, null=True)),
                ('products_status', models.CharField(choices=[('Process', 'Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='processing', max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'cart order',
            },
        ),
        migrations.CreateModel(
            name='CartOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_status', models.CharField(max_length=200, null=True)),
                ('item', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='products/')),
                ('qty', models.IntegerField(default='0')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7777)),
                ('total', models.DecimalField(decimal_places=2, max_digits=7777)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.cartorder')),
            ],
            options={
                'verbose_name_plural': 'cart order items',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='category/')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='products/')),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7777)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=7777)),
                ('specifications', models.TextField(blank=True, null=True)),
                ('products_status', models.CharField(choices=[('Draft', 'Draft'), ('Disabled', 'Disabled'), ('Rejected', 'Rejected'), ('In_review', 'In_review'), ('Published', 'Published')], max_length=200, null=True)),
                ('status', models.BooleanField(blank=True, default=True, null=True)),
                ('in_stock', models.BooleanField(blank=True, default=True, null=True)),
                ('feature', models.BooleanField(blank=True, default=False, null=True)),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
            ],
            options={
                'verbose_name_plural': 'product images',
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField()),
                ('qty', models.IntegerField(choices=[('Draft', 'Draft'), ('Disabled', 'Disabled'), ('Rejected', 'Rejected'), ('In_review', 'In_review'), ('Published', 'Published')], default=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'product review',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='vendor/')),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('address', models.CharField(default='123 main street', max_length=200, null=True)),
                ('contact', models.CharField(default='+234 (345) 787', max_length=200, null=True)),
                ('chat_rep_time', models.CharField(default='10', max_length=200, null=True)),
                ('shipping_on_time', models.CharField(default='10', max_length=200, null=True)),
                ('authentic_rating', models.CharField(default='10', max_length=200, null=True)),
                ('days_return', models.CharField(default='10', max_length=200, null=True)),
                ('warranty_period', models.CharField(default='10', max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Vendors',
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'wishlist',
            },
        ),
        migrations.DeleteModel(
            name='Song',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.tags'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]