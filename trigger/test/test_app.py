"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: test_app.py                                                            #
# Project: WorkFlowTrigger                                                     #
# Last Modified: Monday, 11th December 2023 12:21:23 am                        #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""



import unittest
from trigger.src.app import app


class TestFlaskApp(unittest.TestCase):
    """
    This test suite contains unit tests for the Flask app.
    """

    def setUp(self):
        """
        Set up the test client for the Flask app.
        """
        self.app = app.test_client()

    def test_run_the_app(self):
        """
        Test if the Flask app runs successfully.

        This test sends a GET request to the root URL ('/') and checks if the
        response status code is 200, indicating a successful response.
        """
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
