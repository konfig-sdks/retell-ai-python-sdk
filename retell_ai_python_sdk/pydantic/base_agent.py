# coding: utf-8

"""
    Retell SDK

    API for voice AI. Effortlessly integrate human-like Voice AI into your product. | We are building an API that enables your product to provide an intuitive and engaging way for user interaction - through voice.

    The version of the OpenAPI document: 1.0.0
    Contact: founders@retellai.com
    Created by: https://www.retellai.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from retell_ai_python_sdk.pydantic.base_agent_boosted_keywords import BaseAgentBoostedKeywords

class BaseAgent(BaseModel):
    # The URL we will establish LLM websocket for getting response, usually your server. Check out [LLM WebSocket](https://raw.githubusercontent.com) for more about request format (sent from us) and response format (send to us).
    llm_websocket_url: typing.Optional[str] = Field(None, alias='llm_websocket_url')

    # Unique voice id used for the agent. Find list of available voices and their preview in Dashboard.
    voice_id: typing.Optional[str] = Field(None, alias='voice_id')

    # Controls how stable the voice is. Value ranging from [0,2]. Lower value means more stable, and higher value means more variant speech generation. Currently this setting only applies to `11labs` voices. If unset, default value 1 will apply.
    voice_temperature: typing.Optional[typing.Union[int, float]] = Field(None, alias='voice_temperature')

    # Controls speed of voice. Value ranging from [0.5,2]. Lower value means slower speech, while higher value means faster speech rate. If unset, default value 1 will apply.
    voice_speed: typing.Optional[typing.Union[int, float]] = Field(None, alias='voice_speed')

    # Controls how responsive is the agent. Value ranging from [0,1]. Lower value means less responsive agent (wait more, respond slower), while higher value means faster exchanges (respond when it can). If unset, default value 1 will apply.
    responsiveness: typing.Optional[typing.Union[int, float]] = Field(None, alias='responsiveness')

    # Controls whether the agent would backchannel (agent interjects the speaker with phrases like \"yeah\", \"uh-huh\" to signify interest and engagement). Backchannel when enabled tends to show up more in longer user utterances. If not set, agent will not backchannel.
    enable_backchannel: typing.Optional[bool] = Field(None, alias='enable_backchannel')

    # If set, will add ambient environment sound to the call to make experience more realistic. Currently supports the following options:  - `coffee-shop`: Coffee shop ambience with people chatting in background. [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/coffee-shop.wav)  - `convention-hall`: Convention hall ambience, with some echo and people chatting in background. [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/convention-hall.wav)  - `summer-outdoor`: Summer outdoor ambience with cicada chirping. [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/summer-outdoor.wav)  - `mountain-outdoor`: Mountain outdoor ambience with birds singing. [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/mountain-outdoor.wav)   Set to string `null` to remove ambient sound from this agent. 
    ambient_sound: typing.Optional[Literal["coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor", "null"]] = Field(None, alias='ambient_sound')

    # The name of the agent. Only used for your own reference.
    agent_name: typing.Optional[str] = Field(None, alias='agent_name')

    # `Beta feature, use with caution.`   This setting specifies the agent's operational language, including base language and dialect. Speech recognition considers both elements, but text-to-speech currently only recognizes the base language.    For instance, selecting `en-GB` optimizes speech recognition for British English, yet text-to-speech output will be in standard English. If dialect-specific text-to-speech is required, please contact us for support.   - `11lab voices`: supports English(en), German(de), Spanish(es), Hindi(hi), Portuguese(pt)   - `openAI voices`: supports English(en), German(de), Spanish(es), Hindi(hi), Portuguese(pt), Japanese(ja)   - `deepgram voices`: supports English(en) 
    language: typing.Optional[Literal["en-US", "en-IN", "en-GB", "de-DE", "es-ES", "es-419", "hi-IN", "ja-JP", "pt-PT", "pt-BR"]] = Field(None, alias='language')

    # The webhook for agent to listen to call events. See what events it would get at [webhook doc](https://raw.githubusercontent.com). If set, will binds webhook events for this agent to the specified url, and will ignore the account level webhook for this agent. Set to string `null` to remove webhook url from this agent.
    webhook_url: typing.Optional[str] = Field(None, alias='webhook_url')

    boosted_keywords: typing.Optional[BaseAgentBoostedKeywords] = Field(None, alias='boosted_keywords')

    # Whether to format the transcribed text with inverse text normalization. It transforms the spoken form of text into written form for entities like phone number, email address, street address, etc. For example, \"february fourth twenty twenty two\" can be converted into \"february 4th 2022\". If not set, the default is true.
    format_text: typing.Optional[bool] = Field(None, alias='format_text')

    # Disable transcripts and recordings storage for enhanced privacy. Access transcripts securely via webhooks.
    opt_out_sensitive_data_storage: typing.Optional[bool] = Field(None, alias='optOutSensitiveDataStorage')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
