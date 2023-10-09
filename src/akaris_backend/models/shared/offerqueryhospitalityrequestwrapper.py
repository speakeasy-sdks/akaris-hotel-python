"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import offerqueryhospitalityrequest as shared_offerqueryhospitalityrequest
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OfferQueryHospitalityRequestWrapper:
    offer_query_hospitality_request: Optional[shared_offerqueryhospitalityrequest.OfferQueryHospitalityRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('OfferQueryHospitalityRequest'), 'exclude': lambda f: f is None }})
    
