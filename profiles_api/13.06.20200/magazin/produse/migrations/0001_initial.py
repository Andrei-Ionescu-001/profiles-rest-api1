# Generated by Django 3.0 on 2020-06-23 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=60)),
                ('marca', models.CharField(max_length=30)),
                ('poza', models.ImageField(blank=True, default='poze/none.png', null=True, upload_to='poze/')),
                ('descriere', models.TextField()),
                ('pret', models.FloatField()),
                ('stoc', models.IntegerField(default=0)),
                ('tip', models.CharField(choices=[('sport', 'sport'), ('casual', 'casual'), ('birou', 'birou'), ('plaja', 'plaja')], default='sport', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Poze',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(blank=True, default='poze/none.png', null=True, upload_to='poze/')),
                ('produse_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produse.Produse')),
            ],
        ),
    ]
