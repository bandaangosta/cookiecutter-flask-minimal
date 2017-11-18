import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('{{cookiecutter.package_name}}.default_settings')
app.config.from_envvar('{{cookiecutter.package_name.upper()}}_SETTINGS', silent=True)
app.config.from_envvar('settings.cfg', silent=True)

import {{cookiecutter.package_name}}.views
