"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import offerquerybuildfromcatalogofferingshospitality as shared_offerquerybuildfromcatalogofferingshospitality
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OfferQueryBuildFromCatalogOfferingsHospitalityWrapper:
    offer_query_build_from_catalog_offerings_hospitality: Optional[shared_offerquerybuildfromcatalogofferingshospitality.OfferQueryBuildFromCatalogOfferingsHospitality] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('OfferQueryBuildFromCatalogOfferingsHospitality'), 'exclude': lambda f: f is None }})
    

