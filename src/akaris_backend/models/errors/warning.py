"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..errors import namevaluepair as errors_namevaluepair
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class WarningT(Exception):
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Message'), 'exclude': lambda f: f is None }})
    r"""The Travelport standardized error or warning message"""
    name_value_pair: Optional[list[errors_namevaluepair.NameValuePair]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('NameValuePair'), 'exclude': lambda f: f is None }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('StatusCode'), 'exclude': lambda f: f is None }})
    r"""Http standard response code"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)
