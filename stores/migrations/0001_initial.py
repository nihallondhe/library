# Generated by Django 3.2.8 on 2022-07-07 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.user')),
            ],
        ),
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=20)),
                ('book_type', models.CharField(max_length=10)),
                ('stock', models.IntegerField(default=1)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.store')),
            ],
        ),
    ]
