"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import catalogofferingshospitalityresponse as shared_catalogofferingshospitalityresponse
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CatalogOfferingsHospitalityResponseWrapper:
    catalog_offerings_hospitality_response: Optional[shared_catalogofferingshospitalityresponse.CatalogOfferingsHospitalityResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CatalogOfferingsHospitalityResponse'), 'exclude': lambda f: f is None }})
    
