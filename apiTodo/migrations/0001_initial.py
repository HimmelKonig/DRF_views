# Generated by Django 3.2.9 on 2021-11-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='L', max_length=50)),
                ('done', models.BooleanField(default=False)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('createDate', models.DateTimeField()),
            ],
        ),
    ]
