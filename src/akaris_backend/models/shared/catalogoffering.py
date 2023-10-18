"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import identifier as shared_identifier
from ..shared import pricedetail as shared_pricedetail
from ..shared import productoptions as shared_productoptions
from ..shared import termsandconditions as shared_termsandconditions
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CatalogOffering:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    price: shared_pricedetail.PriceDetail = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Price') }})
    product_options: List[shared_productoptions.ProductOptions] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ProductOptions') }})
    catalog_offering_ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CatalogOfferingRef'), 'exclude': lambda f: f is None }})
    r"""Used to reference another instance of this object in the same message"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Local indentifier within a given message for this object."""
    identifier: Optional[shared_identifier.Identifier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Identifier'), 'exclude': lambda f: f is None }})
    r"""Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database."""
    terms_and_conditions: Optional[shared_termsandconditions.TermsAndConditions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TermsAndConditions'), 'exclude': lambda f: f is None }})
    

