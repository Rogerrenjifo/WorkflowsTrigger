"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: outputs.py                                                             #
# Project: WorkFlowTrigger                                                     #
# Last Modified: Sunday, 10th December 2023 10:50:23 pm                        #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from flask_restx import fields
from trigger.src.configuration import api


information_model = api.model(
    "Roger", {"name": fields.String, "linkedin": fields.String, "email": fields.String}
)

curriculum_model = api.model(
    "curriculum", {'url': fields.String}
)
