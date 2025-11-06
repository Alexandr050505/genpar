import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Password Generator'
copyright = '2025, Александр'
author = 'Александр'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'

html_theme_options = {
    'description': 'Генератор безопасных паролей с CLI-интерфейсом',
    'github_user': 'Alexandr050505',
    'github_repo': 'genpar',
    'fixed_sidebar': True,
    'show_powered_by': True,
    'show_relbars': True,
    'sidebar_width': '300px',
    'page_width': '1200px',
    'code_font_size': '0.9em',
}

html_static_path = ['_static']