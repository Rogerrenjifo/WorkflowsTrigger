"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: configuration.py                                                       #
# Project: WorkFlowTrigger                                                     #
# Last Modified: Sunday, 10th December 2023 10:51:54 pm                        #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from os import getenv
from dotenv import load_dotenv
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

PORT = int(getenv("PORT_ML", "80"))
HOST = str(getenv("HOST_ML", "0.0.0.0"))


api = Api(
    version="1.0.0",
    title="Workflows Trigger API",
    description='<h3 style="font-family: \'Arial\', sans-serif; line-height: 1.6; margin: 20px;"> \
        <h4 style="font-family: \'Arial\', sans-serif; color: #345; background-color: #f7f7f7; padding: 10px;">Description:</h4> \
        <p>This API serves as middleware, facilitating the initiation of GitHub Workflows \
        through Slack integration.</p> \
        <h4 style="color: #034;">Endpoints:</h4> \
        <ul>\
            <li><strong>Send:</strong> Use this endpoint to send a request and start the workflow in GitHub Actions.</li> \
            <li><strong>Configure:</strong> Use this endpoint to create a new user or set up a new workflow.</li> \
            <li><strong>Delete:</strong> Use this endpoint to delete all the information created during the configure request.</li> \
        </ul>',
    license="MIT",
    license_url="https://opensource.org/licenses/MIT",
    contact="Roger Renjifo",
    contact_url="https://github.com/Rogerrenjifo/WorkflowsTrigger",
    contact_email="rrrenjifo@gmail.com.com",
    authorizations={
        "apiKey": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    security="apiKey",
)


db = SQLAlchemy()
user = getenv("DB_USERNAME")
key = getenv("DB_PASSWORD")
server = getenv("DB_SERVER")
database = getenv("DB_DATABASE")
driver = getenv("DB_DRIVER")

ODBC = f"mssql+pyodbc://{user}:{key}@{server}/{database}?{driver}"
