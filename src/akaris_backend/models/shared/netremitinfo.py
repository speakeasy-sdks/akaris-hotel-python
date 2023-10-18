"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import filedamount as shared_filedamount
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NetRemitInfo:
    at_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type'), 'exclude': lambda f: f is None }})
    actual_selling_fare: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ActualSellingFare'), 'exclude': lambda f: f is None }})
    r"""The actual selling fare which will override the Offer base fare on the document"""
    car_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CarCode'), 'exclude': lambda f: f is None }})
    r"""The CAR code applied to this product for use in net remit"""
    net_base_amount: Optional[shared_filedamount.FiledAmount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('NetBaseAmount'), 'exclude': lambda f: f is None }})
    r"""The base amount of a ticket price or net price that is filed in local currency"""
    value_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ValueCode'), 'exclude': lambda f: f is None }})
    r"""The Value code applied to this product for use in net remit"""
    

