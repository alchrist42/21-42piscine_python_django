# Generated by Django 4.0.4 on 2022-05-25 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0004_tipday_dislikes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipday',
            options={'ordering': ['-date'], 'permissions': (('can_be_downvote', 'can_be_downvote'),)},
        ),
    ]