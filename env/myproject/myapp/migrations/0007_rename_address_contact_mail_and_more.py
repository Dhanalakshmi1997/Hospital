# Generated by Django 5.0.4 on 2024-04-25 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='address',
            new_name='mail',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='name',
        ),
    ]
