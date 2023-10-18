"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import buildfromcatalogofferingsrequest as shared_buildfromcatalogofferingsrequest
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OfferQueryBuildFromCatalogOfferingsHospitality:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    build_from_catalog_offerings_request: Optional[shared_buildfromcatalogofferingsrequest.BuildFromCatalogOfferingsRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('BuildFromCatalogOfferingsRequest'), 'exclude': lambda f: f is None }})
    

