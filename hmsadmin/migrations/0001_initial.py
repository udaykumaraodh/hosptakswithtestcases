# Generated by Django 3.1.7 on 2021-08-17 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales2Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mob2', models.BigIntegerField()),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('hopital', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hospital.prereghos')),
                ('salesperson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.sales')),
            ],
        ),
    ]