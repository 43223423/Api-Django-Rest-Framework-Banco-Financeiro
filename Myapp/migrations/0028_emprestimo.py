# Generated by Django 4.1.6 on 2023-05-27 02:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0027_alter_conta_saldobancario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('codigo', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dataSolicitacao', models.DateTimeField(auto_now=True)),
                ('valorSolicitado', models.CharField(max_length=1000000)),
                ('numeroParcela', models.CharField(max_length=10)),
                ('obervacao', models.CharField(max_length=200, null=True)),
                ('emprestimo_Conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Emprestimo_Conta', to='Myapp.conta')),
            ],
        ),
    ]
