# coding: utf-8

"""
    Retell SDK

    API for voice AI. Effortlessly integrate human-like Voice AI into your product. | We are building an API that enables your product to provide an intuitive and engaging way for user interaction - through voice.

    The version of the OpenAPI document: 1.0.0
    Contact: founders@retellai.com
    Created by: https://www.retellai.com/
"""

from retell_ai_python_sdk.paths.create_agent.post import CreateNewAgentRaw
from retell_ai_python_sdk.paths.delete_agent_agent_id.delete import DeleteExistingAgentRaw
from retell_ai_python_sdk.paths.list_agents.get import GetAllRaw
from retell_ai_python_sdk.paths.get_agent_agent_id.get import GetDetailsRaw
from retell_ai_python_sdk.paths.update_agent_agent_id.patch import UpdateExistingAgentRaw


class AgentApiRaw(
    CreateNewAgentRaw,
    DeleteExistingAgentRaw,
    GetAllRaw,
    GetDetailsRaw,
    UpdateExistingAgentRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
