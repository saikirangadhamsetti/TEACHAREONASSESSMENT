# Generated by Django 4.1.3 on 2022-12-21 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productMainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Size', models.IntegerField(choices=[('10', 10), ('20', 20), ('30', 30)], default=10)),
                ('Quality', models.CharField(choices=[('high', 'high'), ('low', 'low'), ('medium', 'medium')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='productImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmainmodel')),
            ],
        ),
        migrations.CreateModel(
            name='productColour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(choices=[('red', 'red'), ('blue', 'blue'), ('green', 'green'), ('black', 'black')], max_length=5)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmainmodel')),
            ],
        ),
    ]
