"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import texttitleanddescription as shared_texttitleanddescription
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CheckInOutPolicy:
    check_in_time: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('checkInTime') }})
    r"""Check-in time"""
    check_out_time: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('checkOutTime') }})
    r"""Check-out time"""
    at_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type'), 'exclude': lambda f: f is None }})
    description: Optional[list[shared_texttitleanddescription.TextTitleAndDescription]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Description'), 'exclude': lambda f: f is None }})
    minimum_age: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimumAge'), 'exclude': lambda f: f is None }})
    r"""Minimum age of guest checking in or out"""
    

