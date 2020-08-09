# Generated by Django 3.1 on 2020-08-09 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('short_text', models.TextField(max_length=100)),
                ('full_text', models.TextField(max_length=500)),
                ('news_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='types.type')),
            ],
        ),
    ]
