# Generated by Django 4.0.4 on 2022-05-25 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_profiles_prefixes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Prefixes',
            field=models.CharField(choices=[('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Ms', 'Ms'), ('Mr', 'Mr')], default='', max_length=60),
        ),
    ]
