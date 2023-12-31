"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomerLoyalty:
    r"""Specifies the ID for the membership program."""
    card_holder_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cardHolderName'), 'exclude': lambda f: f is None }})
    r"""The card holder name"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Customer Loyality Id"""
    priority: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('priority'), 'exclude': lambda f: f is None }})
    r"""Numeric Priority Code"""
    program_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('programId'), 'exclude': lambda f: f is None }})
    r"""Specifies an identifier to indicate the company owner of the loyalty program"""
    program_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('programName'), 'exclude': lambda f: f is None }})
    r"""Supplier's loyalty program name such as Frontier-EarlyReturns"""
    share_with_supplier: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shareWithSupplier'), 'exclude': lambda f: f is None }})
    r"""The list of suppliers that the CustomerLoyalty number is shared."""
    supplier: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplier'), 'exclude': lambda f: f is None }})
    r"""Supplier of a loyalty program"""
    supplier_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplierType'), 'exclude': lambda f: f is None }})
    r"""The kind of supplier of a loyalty program"""
    tier: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tier'), 'exclude': lambda f: f is None }})
    r"""Customer Loyalty tier level"""
    validated_ind: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validatedInd'), 'exclude': lambda f: f is None }})
    r"""Customer loyalty number has been validated by the supplier"""
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    

