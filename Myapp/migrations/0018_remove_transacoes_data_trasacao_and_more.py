# Generated by Django 4.1.6 on 2023-05-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0017_alter_transacoes_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transacoes',
            name='data_trasacao',
        ),
        migrations.AddField(
            model_name='transacoes',
            name='data_transacao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]