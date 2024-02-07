"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .customerloyalty import CustomerLoyalty
from .identifier import Identifier
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TermsAndConditions:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    customer_loyalty: Optional[List[CustomerLoyalty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CustomerLoyalty'), 'exclude': lambda f: f is None }})
    expiry_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ExpiryDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The data and time the offer will expire"""
    identifier: Optional[Identifier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Identifier'), 'exclude': lambda f: f is None }})
    r"""Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Local indentifier within a given message for this object."""
    terms_and_conditions_ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('termsAndConditionsRef'), 'exclude': lambda f: f is None }})
    r"""Used to reference another instance of this object in the same message."""
    

