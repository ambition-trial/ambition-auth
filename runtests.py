#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname, join

extras = dict(
    SENTRY_ENABLED=False,
    INDEX_PAGE="/",
)


app_name = 'ambition_auth'
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ROOT_URLCONF="ambition_edc.urls",
    ETC_DIR=os.path.join(base_dir, app_name, "tests", "etc"),
    SUBJECT_CONSENT_MODEL="ambition_subject.subjectconsent",
    SUBJECT_VISIT_MODEL="ambition_subject.subjectvisit",
    SUBJECT_REQUISITION_MODEL="ambition_subject.subjectrequisition",
    ADVERSE_EVENT_ADMIN_SITE="ambition_ae_admin",
    ADVERSE_EVENT_APP_LABEL="ambition_ae",
    EDC_BOOTSTRAP=3,
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    EMAIL_CONTACTS={
        "data_request": "someone@example.com",
        "data_manager": "someone@example.com",
    },
    EMAIL_ENABLED=True,
    HOLIDAY_FILE=join(base_dir, app_name, "tests", "holidays.csv"),
    LIVE_SYSTEM=False,
    EDC_RANDOMIZATION_LIST_MODEL="ambition_rando.randomizationlist",
    EDC_RANDOMIZATION_LIST_FILE=join(
        base_dir, app_name, "tests", "etc", "randomization_list.csv"),
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "django_celery_results",
        "django_celery_beat",
        "django_crypto_fields.apps.AppConfig",
        "edc_action_item.apps.AppConfig",
        "edc_adverse_event.apps.AppConfig",
        "edc_appointment.apps.AppConfig",
        "edc_auth.apps.AppConfig",
        "edc_consent.apps.AppConfig",
        "edc_dashboard.apps.AppConfig",
        "edc_data_manager.apps.AppConfig",
        "edc_device.apps.AppConfig",
        "edc_export.apps.AppConfig",
        "edc_identifier.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_lab_dashboard.apps.AppConfig",
        "edc_locator.apps.AppConfig",
        "edc_metadata.apps.AppConfig",
        "edc_metadata_rules.apps.AppConfig",
        "edc_navbar.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_offstudy.apps.AppConfig",
        "edc_pharmacy.apps.AppConfig",
        "edc_protocol.apps.AppConfig",
        "edc_randomization.apps.AppConfig",
        "edc_reference.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_subject_dashboard.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        'ambition_ae.apps.AppConfig',
        'ambition_dashboard.apps.AppConfig',
        'ambition_labs.apps.AppConfig',
        'ambition_lists.apps.AppConfig',
        'ambition_auth.apps.AppConfig',
        'ambition_prn.apps.AppConfig',
        'ambition_rando.apps.AppConfig',
        'ambition_screening.apps.AppConfig',
        'ambition_subject.apps.AppConfig',
        'ambition_visit_schedule.apps.AppConfig',
        'ambition_edc.apps.AppConfig',

    ],
    add_dashboard_middleware=True,
    add_lab_dashboard_middleware=True,
    use_test_urls=True,
    **extras,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split('=')[1] for t in sys.argv if t.startswith('--tag')]
    failures = DiscoverRunner(failfast=True, tags=tags).run_tests(
        [f'{app_name}.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
