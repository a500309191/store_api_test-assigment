# Generated by Django 4.1.4 on 2022-12-14 13:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(upload_to='media', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'webp'])])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('article', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('status', models.CharField(choices=[('in_stock', 'In Stock'), ('on_request', 'On Request'), ('expected', 'Expected'), ('out_of_stock', 'Out Of Stock'), ('not_produced', 'Not Produced')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image_Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.format')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.image')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.product'),
        ),
    ]
