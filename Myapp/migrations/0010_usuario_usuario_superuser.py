# Generated by Django 4.1.6 on 2023-05-15 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Myapp', '0009_remove_usuario_usuario_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Usuario_superUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
