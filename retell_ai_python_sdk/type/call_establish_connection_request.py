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

from retell_ai_python_sdk.type.call_establish_connection_request_retell_llm_dynamic_variables import CallEstablishConnectionRequestRetellLlmDynamicVariables

class RequiredCallEstablishConnectionRequest(TypedDict):
    # Unique id of agent used for the call. Your agent would contain the LLM Websocket url used for this call.
    agent_id: str

    # Where the audio websocket would connect from would determine the format / protocol of websocket messages, and would determine how our server read audio bytes and send audio bytes.:  - `web`: The protocol defined by Retell, commonly used for connecting from web frontend. Also useful for those who want to manipulate audio bytes directly.  - `twilio`: The [websocket protocol](https://www.twilio.com/docs/voice/twiml/stream#message-media) defined by Twilio, used when your system uses Twilio, and supplies Retell audio websocket url to Twilio.
    audio_websocket_protocol: str

    # The audio encoding of the call. The following formats are supported:   - `s16le` 16 bit linear PCM audio, the native format for web audio capture and playback.  - `mulaw` non-linear audio encoding technique used in telephony. Commonly used by Twilio.
    audio_encoding: str

    # Sample rate of the conversation, the input and output audio bytes will all conform to this rate. Check the audio source, audio format, and voice used for the agent to select one that works. supports value ranging from [8000, 48000]. Note for Twilio `mulaw` encoding, the sample rate has to be 8000.  - `s16le` sample rate recommendation (natively supported, lowest latency):    - elevenlabs voices: 16000, 22050, 24000, 44100.   - openai voices: 24000.    - deepgram voices: 8000, 16000, 24000, 32000, 48000.
    sample_rate: int

class OptionalCallEstablishConnectionRequest(TypedDict, total=False):
    # If users stay silent for a period, end the call. By default, it is set to 600,000 ms (10 min). The minimum value allowed is 10,000 ms (10 s).
    end_call_after_silence_ms: int

    # The caller number. This field is storage purpose only, set this if you want the call object to contain it so that it's easier to reference it. Not used for processing, when we connect to your LLM websocket server, you can then get it from the call object.
    from_number: str

    # The callee number. This field is storage purpose only, set this if you want the call object to contain it so that it's easier to reference it. Not used for processing, when we connect to your LLM websocket server, you can then get it from the call object.
    to_number: str

    # An abtriary object for storage purpose only. You can put anything here like your own id for the call, twilio SID, internal customer id. Not used for processing, when we connect to your LLM websocket server, you can then get it from the call object.
    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    retell_llm_dynamic_variables: CallEstablishConnectionRequestRetellLlmDynamicVariables

class CallEstablishConnectionRequest(RequiredCallEstablishConnectionRequest, OptionalCallEstablishConnectionRequest):
    pass
