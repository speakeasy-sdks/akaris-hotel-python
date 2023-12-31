"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .catalogofferingsqueryrequest import CatalogOfferingsQueryRequest
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CatalogOfferingsQueryRequestHospitalityWrapper:
    catalog_offerings_query_request: Optional[CatalogOfferingsQueryRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CatalogOfferingsQueryRequest'), 'exclude': lambda f: f is None }})
    

