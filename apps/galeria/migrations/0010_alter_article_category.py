# Generated by Django 4.1.4 on 2023-04-19 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0009_alter_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('FRONTEND', 'Front-end'), ('BACKEND', 'Back-end'), ('FULLSTACK', 'Full-Stack'), ('PYTHON', 'Python'), ('DJANGO', 'Django'), ('JAVASCRIPT', 'JavaScript'), ('REACTJS', 'ReactJs'), ('REACTNATIVE', 'React Native'), ('NODEJS', 'NodeJS')], default='', max_length=255),
        ),
    ]