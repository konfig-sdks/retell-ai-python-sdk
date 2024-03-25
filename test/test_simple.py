# coding: utf-8

"""
    Retell SDK

    API for voice AI. Effortlessly integrate human-like Voice AI into your product. | We are building an API that enables your product to provide an intuitive and engaging way for user interaction - through voice.

    The version of the OpenAPI document: 1.0.0
    Contact: founders@retellai.com
    Created by: https://www.retellai.com/
"""

import unittest

import os
from pprint import pprint
from retell_ai_python_sdk import RetellAi

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        retellai = RetellAi(
        
            access_token = 'YOUR_BEARER_TOKEN'
        )
        self.assertIsNotNone(retellai)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
