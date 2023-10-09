"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import currencycode as shared_currencycode
from ..shared import taxbreakdown as shared_taxbreakdown
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TaxInfo:
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Amount') }})
    r"""The amount of the tax applied"""
    tax_breakdown: list[shared_taxbreakdown.TaxBreakdown] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TaxBreakdown') }})
    r"""The breakdown of the tax for this tax code"""
    tax_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TaxCode') }})
    r"""The tax code"""
    currency_code: Optional[shared_currencycode.CurrencyCode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CurrencyCode'), 'exclude': lambda f: f is None }})
    r"""Currency codes are the three-letter alphabetic codes that represent the various currencies used throughout the world."""
    
