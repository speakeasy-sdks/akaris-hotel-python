"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .currencycode import CurrencyCode
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxBreakdown:
    airport_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('AirportCode') }})
    r"""The airport location the tax applies to"""
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Amount'), 'exclude': lambda f: f is None }})
    r"""The amount of the tax applied"""
    currency_code: Optional[CurrencyCode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CurrencyCode'), 'exclude': lambda f: f is None }})
    r"""Currency codes are the three-letter alphabetic codes that represent the various currencies used throughout the world."""
    

