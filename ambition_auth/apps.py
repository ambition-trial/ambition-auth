from django.apps import AppConfig as DjangoApponfig
from django.apps import apps as django_apps
from django.db.models.signals import post_migrate
from edc_auth.group_permissions_updater import GroupPermissionsUpdater


def post_migrate_update_edc_auth(sender=None, **kwargs):
    from ambition_auth.codenames_by_group import codenames_by_group

    GroupPermissionsUpdater(
        codenames_by_group=codenames_by_group, verbose=True, apps=django_apps
    )


class AppConfig(DjangoApponfig):
    name = "ambition_auth"
    verbose_name = "Ambition Authentication and Permissions"

    def ready(self):
        post_migrate.connect(post_migrate_update_edc_auth, sender=self)
