# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import pydantic_v1
from ..core.unchecked_base_model import UncheckedBaseModel
from .normalized_alignment import NormalizedAlignment


class AudioOutput(UncheckedBaseModel):
    audio: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    A generated partial audio chunk, encoded using the selected output_format, by default this
    is MP3 encoded as a base64 string.
    """

    is_final: typing.Optional[bool] = pydantic_v1.Field(alias="isFinal", default=None)
    """
    Indicates if the generation is complete. If set to `True`, `audio` will be null.
    """

    normalized_alignment: typing.Optional[NormalizedAlignment] = pydantic_v1.Field(
        alias="normalizedAlignment", default=None
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
