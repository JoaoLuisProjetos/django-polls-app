# Generated by Django 2.2.5 on 2019-09-26 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20190926_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=models.ImageField(null=True, upload_to='polls/static/polls/images/'),
        ),
    ]
