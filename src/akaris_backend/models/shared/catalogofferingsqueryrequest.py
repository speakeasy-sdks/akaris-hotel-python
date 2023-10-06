"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import catalogofferingsrequesthospitality as shared_catalogofferingsrequesthospitality
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CatalogOfferingsQueryRequest:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    catalog_offerings_request: list[shared_catalogofferingsrequesthospitality.CatalogOfferingsRequestHospitality] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CatalogOfferingsRequest') }})
    

