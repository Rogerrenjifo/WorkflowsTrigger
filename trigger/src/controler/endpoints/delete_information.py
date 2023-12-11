"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: delete_information.py                                                  #
# Project: WorkFlowTrigger                                                     #
# Last Modified: Monday, 11th December 2023 12:13:11 am                        #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from flask_restx import Resource, Namespace
from trigger.src.controler.data_models.inputs import id_data


delete_information = Namespace(
    "delete_user_information", description="This endpoint delete the user informationfrom \
                                            the configure request."
)

@delete_information.route("/send")
class TriggerGitHubWorkflow(Resource):
    """
    Represents an endpoint for triggering a GitHub workflow based on a Slack request.
    """
    @delete_information.expect(id_data)
    def delete(self):
        """
        Delete the user information.
        """
        args = id_data.parse_args()
        user_id = args.get("id")
        return {"message": f"User {user_id} removed successfully."}, 200
