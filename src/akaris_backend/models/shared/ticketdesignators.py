"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import traveleridentifierref as shared_traveleridentifierref
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TicketDesignators:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    ticket_designator: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TicketDesignator') }})
    traveler_identifier_ref: Optional[list[shared_traveleridentifierref.TravelerIdentifierRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TravelerIdentifierRef'), 'exclude': lambda f: f is None }})
    

