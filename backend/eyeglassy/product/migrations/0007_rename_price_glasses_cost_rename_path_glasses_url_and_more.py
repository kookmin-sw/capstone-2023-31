# Generated by Django 4.1.7 on 2023-05-15 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_glasses_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='glasses',
            old_name='price',
            new_name='cost',
        ),
        migrations.RenameField(
            model_name='glasses',
            old_name='path',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='glasses',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
