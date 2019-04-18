#!/usr/bin/env python

import os


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

DEBUG = False

TIME_ZONE = "Europe/Stockholm"

# DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

SECRET_KEY = "not needed"

USE_TZ = True

LANGUAGE_CODE = "en"

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.admin",
    "wagtail.core",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.images",
    "wagtail.documents",
    "taggit",
    "wagtailtextanalysis",
    # "wagtailtextanalysis.tests.demopages",
    "wagtailtextanalysis.tests.demosite",
]

ROOT_URLCONF = "wagtailtextanalysis.tests.demosite.urls"

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.core.middleware.SiteMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
)

ALT_GENERATOR_MIN_CONFIDENCE = 0

COMPUTER_VISION_API_KEY = getattr(os.environ, "COMPUTER_VISION_API_KEY", None)
COMPUTER_VISION_REGION = "canada"
