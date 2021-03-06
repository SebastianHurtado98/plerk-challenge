# Generated by Django 3.2.6 on 2022-05-25 14:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'activa'), (2, 'inactiva')], verbose_name='status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'companies',
                'ordering': ['name'],
            },
        ),
    ]
