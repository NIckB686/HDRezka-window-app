import json
import os

SETTINGS_PATH = 'user_settings.json'

DEFAULT_SETTINGS = {
    'theme': 'system',
    'custom_colors': {}
}


def load_settings():
    if not os.path.exists(SETTINGS_PATH):
        save_settings(DEFAULT_SETTINGS)
    with open(SETTINGS_PATH, 'r') as f:
        return json.load(f)


def save_settings(settings: dict):
    with open(SETTINGS_PATH, 'w') as f:
        json.dump(settings, f, indent=4)
