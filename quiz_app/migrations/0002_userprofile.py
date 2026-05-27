import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def create_profiles_for_existing_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    UserProfile = apps.get_model('quiz_app', 'UserProfile')

    profiles = [
        UserProfile(user=user, department='it')
        for user in User.objects.filter(profile__isnull=True)
    ]
    UserProfile.objects.bulk_create(profiles)


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('it', 'IT Department'), ('life_science', 'Life Science Department'), ('commerce', 'Commerce Department'), ('arts', 'Arts Department'), ('science', 'Science Department')], default='it', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(create_profiles_for_existing_users, migrations.RunPython.noop),
    ]
