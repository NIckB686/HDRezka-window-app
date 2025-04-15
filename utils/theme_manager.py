import os.path

import darkdetect


def get_theme_filename(theme_name):
    theme_map = {
        'light': 'light.qss',
        'dark': 'dark.qss',
        'material_light': 'material_light.qss',
        'material_dark': 'material_dark.qss',
        'user_theme': 'user_theme.qss'
    }

    if theme_name == 'system':
        return theme_map['material_dark'] if darkdetect.isDark() else theme_map['material_light']
    print(theme_map.get(theme_name))
    return theme_map.get(theme_name)


def load_stylesheet(theme_name):
    filename = get_theme_filename(theme_name)
    abs_path = os.path.abspath(__file__)
    path = os.path.join(os.path.dirname(os.path.dirname(abs_path)), 'themes', filename)

    if os.path.exists(path):
        with open(path, 'r') as f:
            return f.read()

    return ''
