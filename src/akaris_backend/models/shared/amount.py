"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import currencycode as shared_currencycode
from ..shared import currencysourceenum as shared_currencysourceenum
from ..shared import fees as shared_fees
from ..shared import taxes as shared_taxes
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Amount:
    at_type: Optional[str] = dataclasses.field(default='Amount', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type'), 'exclude': lambda f: f is None }})
    approximate_ind: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approximateInd'), 'exclude': lambda f: f is None }})
    r"""True if this amount has been converted from the original amount"""
    base: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Base'), 'exclude': lambda f: f is None }})
    r"""The price prior to all applicable taxes of a product such as the rate for a room or fare for a flight."""
    currency_code: Optional[shared_currencycode.CurrencyCode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CurrencyCode'), 'exclude': lambda f: f is None }})
    r"""Currency codes are the three-letter alphabetic codes that represent the various currencies used throughout the world."""
    currency_source: Optional[shared_currencysourceenum.CurrencySourceEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currencySource'), 'exclude': lambda f: f is None }})
    r"""The system requesting or returning the currency code specified in the attribute"""
    fees: Optional[shared_fees.Fees] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Fees'), 'exclude': lambda f: f is None }})
    taxes: Optional[shared_taxes.Taxes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Taxes'), 'exclude': lambda f: f is None }})
    total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Total'), 'exclude': lambda f: f is None }})
    r"""Specifies the total price including base + taxes + fees"""
    

