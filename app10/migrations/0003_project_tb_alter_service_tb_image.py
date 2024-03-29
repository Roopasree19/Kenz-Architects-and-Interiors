# Generated by Django 4.1.7 on 2023-02-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app10', '0002_service_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='project_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='projectimg/')),
            ],
        ),
        migrations.AlterField(
            model_name='service_tb',
            name='image',
            field=models.ImageField(upload_to='serviceimg/'),
        ),
    ]
