import os
#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
# ROW_LIMIT = 5000
SUPERSET_WORKERS = 1 # for it to work in heroku basic/hobby dynos increase as you like

# SUPERSET_WEBSERVER_PORT = 8088
#---------------------------------------------------------

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'  # noqa

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# Superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
# SQLALCHEMY_DATABASE_URI = 'postgres://apvbeslrkahhca:e89c24baaf6680a0808ed7febc8785408ac9172a7eb0a6a1a25915b7f4579cc1@ec2-107-20-151-189.compute-1.amazonaws.com:5432/d4hptidm84k3tu'


# Flask-WTF flag for CSRF
CSRF_ENABLED = True
