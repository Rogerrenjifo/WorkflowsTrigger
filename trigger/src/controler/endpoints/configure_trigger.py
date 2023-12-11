"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: configure_trigger.py                                                   #
# Project: WorkFlowTrigger                                                     #
# Last Modified: Sunday, 10th December 2023 10:50:29 pm                        #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from flask import request
from flask_restx import Resource, Namespace
from trigger.src.controler.data_models.inputs import configure_input


configure_trigger = Namespace(
    "trigger", description="This endpoint trigger a GitHub Actions Workflow"
)


@configure_trigger.route("/configure")
class TriggerGitHubWorkflow(Resource):
    """
    Represents an endpoint for triggering a GitHub workflow based on a Slack request.
    """
    @configure_trigger.expect(configure_input)
    @configure_trigger.response(200, 'Success')
    @configure_trigger.response(400, 'Validation Error')
    def post(self):
        """
        Configure a new user and the information to trigger a workflow.

        :param token: Slack verification token.
        :return: JSON response indicating the success of the GitHub workflow trigger.
        :rtype: dict
        """
        print(configure_input)
        data = request.json
        return {"message":f"The request were configured successfully: {data}"}, 201
