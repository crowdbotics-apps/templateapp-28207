# Generated by Django 2.2.20 on 2021-06-24 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('username', models.CharField(blank=True, max_length=256, null=True)),
                ('password', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]