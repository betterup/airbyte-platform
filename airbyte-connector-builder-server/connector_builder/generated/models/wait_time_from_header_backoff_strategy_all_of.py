# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from connector_builder.generated.models.any_of_interpolated_stringstring import AnyOfInterpolatedStringstring


class WaitTimeFromHeaderBackoffStrategyAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    WaitTimeFromHeaderBackoffStrategyAllOf - a model defined in OpenAPI

        header: The header of this WaitTimeFromHeaderBackoffStrategyAllOf.
        config: The config of this WaitTimeFromHeaderBackoffStrategyAllOf.
        regex: The regex of this WaitTimeFromHeaderBackoffStrategyAllOf [Optional].
    """

    header: AnyOfInterpolatedStringstring = Field(alias="header")
    config: Dict[str, Any] = Field(alias="config")
    regex: Optional[str] = Field(alias="regex", default=None)

WaitTimeFromHeaderBackoffStrategyAllOf.update_forward_refs()