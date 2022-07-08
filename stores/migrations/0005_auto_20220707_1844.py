# Generated by Django 3.2.8 on 2022-07-07 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stores', '0004_alter_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='owner',
        ),
        migrations.AddField(
            model_name='books',
            name='auther',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
