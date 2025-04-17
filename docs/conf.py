# conf.py
import os
import sys

# Minimal required Sphinx settings
project = 'My Static Site' # Replace with your project name if needed
copyright = '2025, Your Name' # Replace with your details
author = 'Your Name' # Replace with your details

# Required Sphinx stubs
extensions = []
master_doc = 'index' # Must point to index.rst (without extension)
language = 'en' # or 'ru' if needed
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Theme doesn't matter as its output will be overwritten,
# but Sphinx requires one. 'alabaster' is lightweight.
html_theme = 'alabaster'

# Ensure html_static_path does NOT point to your _static_html directory
# html_static_path = ['_static'] # Default Sphinx value, can be left or commented out

# DO NOT USE THESE SETTINGS FOR YOUR MAIN FILES:
# html_extra_path = ['../_static_html'] # Commented out or removed
# html_additional_pages = {} # Commented out or removed