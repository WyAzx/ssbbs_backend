import json
import os

import pymysql
import logging

LOG = logging.getLogger(__name__)

pymysql.install_as_MySQLdb()

with open("environment.json") as env_file:
    env_data = json.load(env_file)
    for key, val in env_data.items():
        os.environ[key] = str(val)
