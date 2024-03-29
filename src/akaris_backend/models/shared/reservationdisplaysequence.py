"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .displaysequence import DisplaySequence
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReservationDisplaySequence:
    at_type: Optional[str] = dataclasses.field(default='ReservationDisplaySequence', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type'), 'exclude': lambda f: f is None }})
    display_sequence: Optional[List[DisplaySequence]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DisplaySequence'), 'exclude': lambda f: f is None }})
    auto_delete_date_sequence: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('autoDeleteDateSequence'), 'exclude': lambda f: f is None }})
    r"""The sequence of the autoDeleteDate (retention segment) within the Reservation"""
    

