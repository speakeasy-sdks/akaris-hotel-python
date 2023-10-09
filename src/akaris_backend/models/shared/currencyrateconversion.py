"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import conversionrate as shared_conversionrate
from ..shared import currencycode as shared_currencycode
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CurrencyRateConversion:
    conversion_rate: shared_conversionrate.ConversionRate = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ConversionRate') }})
    r"""A conversion metric from standard to another with the contextual authority such as IATA, OAG, ISO, etc."""
    source_currency: shared_currencycode.CurrencyCode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('SourceCurrency') }})
    r"""Currency codes are the three-letter alphabetic codes that represent the various currencies used throughout the world."""
    target_currency: shared_currencycode.CurrencyCode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TargetCurrency') }})
    r"""Currency codes are the three-letter alphabetic codes that represent the various currencies used throughout the world."""
    at_type: Optional[str] = dataclasses.field(default='CurrencyRateConversion', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type'), 'exclude': lambda f: f is None }})
    
