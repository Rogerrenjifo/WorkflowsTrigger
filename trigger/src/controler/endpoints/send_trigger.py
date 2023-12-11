"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: send_trigger.py                                                        #
# Project: WorkFlowTrigger                                                     #
# Last Modified: Sunday, 10th December 2023 10:50:46 pm                        #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from os import getenv
from flask_restx import Resource, Namespace
from trigger.src.controler.data_models.inputs import slack_request
from trigger.src.model.requests.github import Github


send_trigger = Namespace(
    "trigger", description="This endpoint trigger a GitHub Actions Workflow"
)

@send_trigger.route("/send")
class TriggerGitHubWorkflow(Resource):
    """
    Represents an endpoint for triggering a GitHub workflow based on a Slack request.
    """
    @send_trigger.expect(slack_request)
    @send_trigger.response(201, 'Success')
    @send_trigger.response(400, 'Validation Error')
    @send_trigger.response(403, 'Forbidden')
    def post(self):
        """
        Triggers a GitHub workflow based on a Slack request.

        :param token: Slack verification token.
        :return: JSON response indicating the success of the GitHub workflow trigger.
        :rtype: dict
        """
        args = slack_request.parse_args()
        token = args.get("token")
        testing_type = args.get("text")
        print(args)
        Github().trigger()
        if token == getenv("SLACK_TOKEN"):
            return {"message": f"The {testing_type} testing is running"}, 201
        return {"message": f"The {testing_type} testing is running"}, 201
