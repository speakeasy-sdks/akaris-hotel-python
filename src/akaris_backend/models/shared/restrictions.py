"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .documenttypeenum import DocumentTypeEnum
from .traveleridentifierref import TravelerIdentifierRef
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Restrictions:
    restriction: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Restriction') }})
    at_type: Optional[str] = dataclasses.field(default='Restrictions', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type'), 'exclude': lambda f: f is None }})
    document_type: Optional[DocumentTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DocumentType'), 'exclude': lambda f: f is None }})
    r"""Document type like EMD, MCO"""
    traveler_identifier_ref: Optional[List[TravelerIdentifierRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TravelerIdentifierRef'), 'exclude': lambda f: f is None }})
    

