# Generated by Django 4.0.4 on 2022-05-25 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markitten_app', '0008_alter_category_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='Categories',
        ),
        migrations.AlterModelTable(
            name='comment',
            table='Comments',
        ),
        migrations.AlterModelTable(
            name='product',
            table='Products',
        ),
        migrations.AlterModelTable(
            name='productarchive',
            table='ProductArchives',
        ),
        migrations.AlterModelTable(
            name='profile',
            table='Profiles',
        ),
        migrations.AlterModelTable(
            name='supplierarchive',
            table='SupplierArchives',
        ),
        migrations.AlterModelTable(
            name='supplierproduct',
            table='SupplierProducts',
        ),
    ]
