"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .confirmationstatusenum import ConfirmationStatusEnum
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TravelerProduct:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    confirmation_status_enum: Optional[ConfirmationStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ConfirmationStatusEnum'), 'exclude': lambda f: f is None }})
    r"""Status returned in a response for a two or more phase commitment process"""
    offer_ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('OfferRef'), 'exclude': lambda f: f is None }})
    r"""A pointer to the Offer id"""
    product_ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ProductRef'), 'exclude': lambda f: f is None }})
    r"""A pointer to the product id"""
    traveler_ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TravelerRef'), 'exclude': lambda f: f is None }})
    r"""A pointer to the traveler id"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    

