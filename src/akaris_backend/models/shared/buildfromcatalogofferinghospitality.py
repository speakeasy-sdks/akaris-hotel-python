"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import identifier as shared_identifier
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BuildFromCatalogOfferingHospitality:
    at_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type'), 'exclude': lambda f: f is None }})
    catalog_offering_identifier: Optional[shared_identifier.Identifier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CatalogOfferingIdentifier'), 'exclude': lambda f: f is None }})
    r"""Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database."""
    number_of_rooms: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('NumberOfRooms'), 'exclude': lambda f: f is None }})
    r"""Number of rooms required."""
    
