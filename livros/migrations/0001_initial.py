# Generated by Django 4.2.16 on 2024-11-02 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('streaming', models.CharField(choices=[('N', 'Netflix'), ('A', 'Amazon Prime')], max_length=2)),
                ('nota', models.IntegerField(blank=True, null=True)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('categorias', models.ManyToManyField(to='livros.categorias')),
            ],
        ),
    ]