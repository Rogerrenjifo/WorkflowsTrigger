"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: app.py                                                                 #
# Project: WorkFlowTrigger                                                     #
# Last Modified: Sunday, 10th December 2023 10:51:48 pm                        #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from flask import Flask
from trigger.src.configuration import api, db, ODBC, PORT, HOST
from trigger.src.controler.endpoints.send_trigger import send_trigger
from trigger.src.controler.endpoints.configure_trigger import configure_trigger
from trigger.src.controler.endpoints.delete_information import delete_information


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ODBC
app.config.SWAGGER_UI_DOC_EXPANSION = "list"

api.init_app(app)
db.init_app(app)

api.add_namespace(send_trigger)
api.add_namespace(configure_trigger)
api.add_namespace(delete_information)


if __name__ == "__main__":
    app.run(port=PORT, host=HOST)
