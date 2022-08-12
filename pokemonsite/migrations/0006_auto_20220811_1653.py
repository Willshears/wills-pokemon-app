# Generated by Django 3.2.15 on 2022-08-11 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemonsite', '0005_auto_20220811_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ability',
            name='pokemon_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemonsite.pokemon'),
        ),
        migrations.AlterField(
            model_name='move',
            name='pokemon_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemonsite.pokemon'),
        ),
        migrations.AlterField(
            model_name='type',
            name='pokemon_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemonsite.pokemon'),
        ),
    ]