# Generated by Django 4.2.16 on 2024-10-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ladodireito',
            name='instagram',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ladodireito',
            name='linkedin',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ladodireito',
            name='youtube',
            field=models.CharField(max_length=50),
        ),
    ]
