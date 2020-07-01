# Generated by Django 2.2.4 on 2020-06-30 18:16

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.GenericIPAddressField(null=True, validators=[django.core.validators.validate_ipv4_address])),
                ('status', models.BooleanField(default=False)),
                ('env', models.CharField(max_length=20)),
                ('version', models.CharField(max_length=5)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True, validators=[django.core.validators.EmailValidator])),
                ('password', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(8, 'the password cant be small then 8')])),
                ('last_login', models.DateField(default=datetime.date.today)),
                ('group', models.ManyToManyField(to='api.Group')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('critical', 'critical.'), ('debug', 'debug'), ('error', 'error'), ('warning', 'warning'), ('information', 'info')], max_length=20)),
                ('data', models.TextField(max_length=500)),
                ('arquivado', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('agent', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='api.Agent')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.User'),
        ),
    ]
