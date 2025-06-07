import os
from pathlib import Path

BASE_DIR = os.path.join(Path(os.path.dirname(__file__)).parent, "src")
print(BASE_DIR)
SECRET_KEY = "fake-key"
DEBUG = True
INSTALLED_APPS = [
    "core.base",
    "core.users",
    "django.contrib.auth",
    "django.contrib.contenttypes",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
USE_TZ = True
AUTH_USER_MODEL = "core_users.User"
