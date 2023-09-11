from django.db import migrations


def datamigrations(apps, schema_editor):
    try:
        OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    except LookupError:
        print('old app not installed')
        return

    NewProfile = apps.get_model('profiles', 'Profile')
    NewProfile.objects.bulk_create(
        NewProfile(
            user_id=old_object.user_id,
            favorite_city=old_object.favorite_city,
        )
        for old_object in OldProfile.objects.all()
    )


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(datamigrations),
    ]