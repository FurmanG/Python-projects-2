# Generated by Django 4.0.4 on 2022-05-31 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_alter_profiles_prefixes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Prefixes',
            field=models.CharField(choices=[('Miss', 'Miss'), ('Ms', 'Ms'), ('Mr', 'Mr'), ('Mrs', 'Mrs')], default='', max_length=60),
        ),
    ]
