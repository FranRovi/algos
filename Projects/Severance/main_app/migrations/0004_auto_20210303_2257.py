# Generated by Django 2.2.4 on 2021-03-03 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210303_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='severance',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='severances', to='main_app.User'),
        ),
    ]
