"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddressStreetNumber:
    r"""The street number alone is the numerical number that precedes the street name in the address"""
    po_box: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('po_Box'), 'exclude': lambda f: f is None }})
    r"""PO Box Number"""
    rural_route_nmbr: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ruralRouteNmbr'), 'exclude': lambda f: f is None }})
    r"""RuralRoute Number"""
    street_direction: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streetDirection'), 'exclude': lambda f: f is None }})
    r"""Dircetion of the Street"""
    street_nmbr_suffix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streetNmbrSuffix'), 'exclude': lambda f: f is None }})
    r"""Street Number Suffix"""
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    

