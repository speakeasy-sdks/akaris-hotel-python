"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .catalogofferingsquerybuildfromproperties import CatalogOfferingsQueryBuildFromProperties
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CatalogOfferingsQueryBuildFromPropertiesWrapper:
    catalog_offerings_query_build_from_properties: Optional[CatalogOfferingsQueryBuildFromProperties] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CatalogOfferingsQueryBuildFromProperties'), 'exclude': lambda f: f is None }})
    

