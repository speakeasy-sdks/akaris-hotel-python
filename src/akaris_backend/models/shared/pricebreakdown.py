"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import amount as shared_amount
from ..shared import commission as shared_commission
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PriceBreakdown:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    amount: Optional[shared_amount.Amount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Amount'), 'exclude': lambda f: f is None }})
    commission: Optional[shared_commission.Commission] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Commission'), 'exclude': lambda f: f is None }})
    

