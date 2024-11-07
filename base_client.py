# This file was auto-generated by Fern from our API Definition.

import os
import typing

import httpx

from .audio_native.client import AsyncAudioNativeClient, AudioNativeClient
from .chapters.client import AsyncChaptersClient, ChaptersClient
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .dubbing.client import AsyncDubbingClient, DubbingClient
from .environment import ElevenLabsEnvironment
from .history.client import AsyncHistoryClient, HistoryClient
from .models.client import AsyncModelsClient, ModelsClient
from .projects.client import AsyncProjectsClient, ProjectsClient
from .pronunciation_dictionary.client import AsyncPronunciationDictionaryClient, PronunciationDictionaryClient
from .samples.client import AsyncSamplesClient, SamplesClient
from .speech_to_speech.client import AsyncSpeechToSpeechClient, SpeechToSpeechClient
from .text_to_speech.client import AsyncTextToSpeechClient, TextToSpeechClient
from .user.client import AsyncUserClient, UserClient
from .voice_generation.client import AsyncVoiceGenerationClient, VoiceGenerationClient
from .voices.client import AsyncVoicesClient, VoicesClient
from .workspace.client import AsyncWorkspaceClient, WorkspaceClient


class BaseElevenLabs:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : ElevenLabsEnvironment
        The environment to use for requests from the client. from .environment import ElevenLabsEnvironment



        Defaults to ElevenLabsEnvironment.PRODUCTION



    api_key : typing.Optional[str]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from elevenlabs.client import ElevenLabs

    client = ElevenLabs(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: ElevenLabsEnvironment = ElevenLabsEnvironment.PRODUCTION,
        api_key: typing.Optional[str] = os.getenv("ELEVEN_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.history = HistoryClient(client_wrapper=self._client_wrapper)
        self.samples = SamplesClient(client_wrapper=self._client_wrapper)
        self.text_to_speech = TextToSpeechClient(client_wrapper=self._client_wrapper)
        self.speech_to_speech = SpeechToSpeechClient(client_wrapper=self._client_wrapper)
        self.voice_generation = VoiceGenerationClient(client_wrapper=self._client_wrapper)
        self.user = UserClient(client_wrapper=self._client_wrapper)
        self.voices = VoicesClient(client_wrapper=self._client_wrapper)
        self.projects = ProjectsClient(client_wrapper=self._client_wrapper)
        self.chapters = ChaptersClient(client_wrapper=self._client_wrapper)
        self.dubbing = DubbingClient(client_wrapper=self._client_wrapper)
        self.models = ModelsClient(client_wrapper=self._client_wrapper)
        self.audio_native = AudioNativeClient(client_wrapper=self._client_wrapper)
        self.pronunciation_dictionary = PronunciationDictionaryClient(client_wrapper=self._client_wrapper)
        self.workspace = WorkspaceClient(client_wrapper=self._client_wrapper)


class AsyncBaseElevenLabs:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : ElevenLabsEnvironment
        The environment to use for requests from the client. from .environment import ElevenLabsEnvironment



        Defaults to ElevenLabsEnvironment.PRODUCTION



    api_key : typing.Optional[str]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from elevenlabs.client import AsyncElevenLabs

    client = AsyncElevenLabs(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: ElevenLabsEnvironment = ElevenLabsEnvironment.PRODUCTION,
        api_key: typing.Optional[str] = os.getenv("ELEVEN_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.history = AsyncHistoryClient(client_wrapper=self._client_wrapper)
        self.samples = AsyncSamplesClient(client_wrapper=self._client_wrapper)
        self.text_to_speech = AsyncTextToSpeechClient(client_wrapper=self._client_wrapper)
        self.speech_to_speech = AsyncSpeechToSpeechClient(client_wrapper=self._client_wrapper)
        self.voice_generation = AsyncVoiceGenerationClient(client_wrapper=self._client_wrapper)
        self.user = AsyncUserClient(client_wrapper=self._client_wrapper)
        self.voices = AsyncVoicesClient(client_wrapper=self._client_wrapper)
        self.projects = AsyncProjectsClient(client_wrapper=self._client_wrapper)
        self.chapters = AsyncChaptersClient(client_wrapper=self._client_wrapper)
        self.dubbing = AsyncDubbingClient(client_wrapper=self._client_wrapper)
        self.models = AsyncModelsClient(client_wrapper=self._client_wrapper)
        self.audio_native = AsyncAudioNativeClient(client_wrapper=self._client_wrapper)
        self.pronunciation_dictionary = AsyncPronunciationDictionaryClient(client_wrapper=self._client_wrapper)
        self.workspace = AsyncWorkspaceClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: ElevenLabsEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
