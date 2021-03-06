# Generated by Django 3.1.1 on 2020-10-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('number', models.IntegerField()),
                ('type', models.CharField(choices=[('OLD', 'Present client'), ('NEW', 'New client')], default='NEW', max_length=3)),
                ('core', models.DecimalField(decimal_places=2, max_digits=5)),
                ('premium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
