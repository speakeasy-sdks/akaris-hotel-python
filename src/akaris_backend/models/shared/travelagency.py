"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import companyname as shared_companyname
from ..shared import identifier as shared_identifier
from ..shared import organizationtypeenum as shared_organizationtypeenum
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TravelAgency:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    organization_name: shared_companyname.CompanyName = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('OrganizationName') }})
    r"""Identifies a company by name."""
    corporate_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CorporateCode'), 'exclude': lambda f: f is None }})
    r"""A reference assigned by the Travel Agency to identify the corporate organization"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Simple xsd id, not for external use"""
    identifier: Optional[shared_identifier.Identifier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Identifier'), 'exclude': lambda f: f is None }})
    r"""Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database."""
    organization_type: Optional[shared_organizationtypeenum.OrganizationTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organizationType'), 'exclude': lambda f: f is None }})
    r"""The type of organization such as an Agency, Branch, Company, Supplier, Provider"""
    profile_name: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ProfileName'), 'exclude': lambda f: f is None }})
    travel_organization_ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TravelOrganizationRef'), 'exclude': lambda f: f is None }})
    r"""An organization that has a name and a structure and members and directly works in the travel industry"""
    

