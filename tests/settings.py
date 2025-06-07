import os
from pathlib import Path

BASE_DIR = os.path.join(Path(os.path.dirname(__file__)).parent, "src")
print(BASE_DIR)
SECRET_KEY = "fake-key"
DEBUG = True
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "core.base",
    "core.users",
    "core.choirs",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
USE_TZ = True
AUTH_USER_MODEL = "core_users.User"
