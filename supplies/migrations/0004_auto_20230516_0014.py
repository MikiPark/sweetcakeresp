# Generated by Django 3.2.19 on 2023-05-16 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordendecompra', '__first__'),
        ('supplies', '0003_auto_20230514_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplies',
            name='estado',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='supplies',
            name='ordendc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ordendecompra.ordendc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplies',
            name='preciounidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplies',
            name='marca_producto',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
