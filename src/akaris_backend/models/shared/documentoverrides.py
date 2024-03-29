"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .changefeecollectionmethod import ChangeFeeCollectionMethod
from .commissions import Commissions
from .destinationpurpose import DestinationPurpose
from .identifier import Identifier
from .netremitinfo import NetRemitInfo
from .offeridentifier import OfferIdentifier
from .productidentifier import ProductIdentifier
from .restrictions import Restrictions
from .ticketdesignators import TicketDesignators
from .tourcodes import TourCodes
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DocumentOverrides:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    change_fee_collection_method: Optional[ChangeFeeCollectionMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ChangeFeeCollectionMethod'), 'exclude': lambda f: f is None }})
    commissions: Optional[List[Commissions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Commissions'), 'exclude': lambda f: f is None }})
    destination_purpose: Optional[List[DestinationPurpose]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DestinationPurpose'), 'exclude': lambda f: f is None }})
    document_overrides_ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DocumentOverridesRef'), 'exclude': lambda f: f is None }})
    identifier: Optional[Identifier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Identifier'), 'exclude': lambda f: f is None }})
    r"""Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database."""
    net_remit_info: Optional[NetRemitInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('NetRemitInfo'), 'exclude': lambda f: f is None }})
    offer_identifier: Optional[OfferIdentifier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('OfferIdentifier'), 'exclude': lambda f: f is None }})
    product_identifier: Optional[ProductIdentifier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ProductIdentifier'), 'exclude': lambda f: f is None }})
    restrictions: Optional[List[Restrictions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Restrictions'), 'exclude': lambda f: f is None }})
    ticket_designators: Optional[List[TicketDesignators]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TicketDesignators'), 'exclude': lambda f: f is None }})
    tour_codes: Optional[List[TourCodes]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TourCodes'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The reporting number."""
    

