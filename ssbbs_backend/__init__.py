import pymysql
import logging

LOG = logging.getLogger(__name__)

pymysql.install_as_MySQLdb()
