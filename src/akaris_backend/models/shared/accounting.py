"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .identifier import Identifier
from .namevaluepair import NameValuePair
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Accounting:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    accounting_ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('AccountingRef'), 'exclude': lambda f: f is None }})
    r"""Accounting reference"""
    identifier: Optional[Identifier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Identifier'), 'exclude': lambda f: f is None }})
    r"""Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database."""
    name_value_pair: Optional[List[NameValuePair]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('NameValuePair'), 'exclude': lambda f: f is None }})
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Accounting data type"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    template: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('template'), 'exclude': lambda f: f is None }})
    r"""Accounting template"""
    

