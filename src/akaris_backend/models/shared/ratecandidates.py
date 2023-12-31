"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .ratecandidate import RateCandidate
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RateCandidates:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    rate_candidate: List[RateCandidate] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RateCandidate') }})
    post_pay_rates_only_ind: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postPayRatesOnlyInd'), 'exclude': lambda f: f is None }})
    r"""If true, only postpay rates will be returned"""
    pre_pay_rates_only_ind: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prePayRatesOnlyInd'), 'exclude': lambda f: f is None }})
    r"""If true, only prepay rates will be returned"""
    

