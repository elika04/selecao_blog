# Generated by Django 5.1.4 on 2024-12-15 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tags_remove_blog_category_alter_blog_user_and_more'),
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail_blog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.users'),
        ),
    ]
