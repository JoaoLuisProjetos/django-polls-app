# Generated by Django 2.2.5 on 2019-09-26 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=models.ImageField(null=True, upload_to='mysite/polls/static/polls/images'),
        ),
    ]
