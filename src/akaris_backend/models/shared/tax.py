"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .yesnounknownenum import YesNoUnknownEnum
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Tax:
    code_authority: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codeAuthority'), 'exclude': lambda f: f is None }})
    r"""Code Authority"""
    currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currencyCode'), 'exclude': lambda f: f is None }})
    r"""Currency code of the city."""
    decimal_authority: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('decimalAuthority'), 'exclude': lambda f: f is None }})
    r"""Decimal Authority"""
    decimal_place: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('decimalPlace'), 'exclude': lambda f: f is None }})
    r"""Allowed number of decimals."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""additional information"""
    exempt_ind: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exemptInd'), 'exclude': lambda f: f is None }})
    r"""If true, this tax is exempt"""
    included_in_base: Optional[YesNoUnknownEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('includedInBase'), 'exclude': lambda f: f is None }})
    r"""Yes , No , Unknown"""
    purpose: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purpose'), 'exclude': lambda f: f is None }})
    r"""purpose"""
    reporting_authority: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportingAuthority'), 'exclude': lambda f: f is None }})
    r"""Identifies the reporting authority such as airport code for XF taxes."""
    tax_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxCode'), 'exclude': lambda f: f is None }})
    r"""Tax code of the city"""
    value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    

