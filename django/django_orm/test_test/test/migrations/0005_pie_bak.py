# Generated by Django 5.0.6 on 2024-07-26 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0004_remove_pie_bak'),
    ]

    operations = [
        migrations.AddField(
            model_name='pie',
            name='bak',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='pie_bak', to='test.user'),
            preserve_default=False,
        ),
    ]
