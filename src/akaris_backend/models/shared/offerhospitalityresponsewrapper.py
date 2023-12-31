"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .offerhospitalityresponse import OfferHospitalityResponse
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OfferHospitalityResponseWrapper:
    offer_hospitality_response: Optional[OfferHospitalityResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('OfferHospitalityResponse'), 'exclude': lambda f: f is None }})
    

