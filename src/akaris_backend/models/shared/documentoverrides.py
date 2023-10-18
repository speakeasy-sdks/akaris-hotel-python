"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import changefeecollectionmethod as shared_changefeecollectionmethod
from ..shared import commissions as shared_commissions
from ..shared import destinationpurpose as shared_destinationpurpose
from ..shared import identifier as shared_identifier
from ..shared import netremitinfo as shared_netremitinfo
from ..shared import offeridentifier as shared_offeridentifier
from ..shared import productidentifier as shared_productidentifier
from ..shared import restrictions as shared_restrictions
from ..shared import ticketdesignators as shared_ticketdesignators
from ..shared import tourcodes as shared_tourcodes
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DocumentOverrides:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    change_fee_collection_method: Optional[shared_changefeecollectionmethod.ChangeFeeCollectionMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ChangeFeeCollectionMethod'), 'exclude': lambda f: f is None }})
    commissions: Optional[List[shared_commissions.Commissions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Commissions'), 'exclude': lambda f: f is None }})
    destination_purpose: Optional[List[shared_destinationpurpose.DestinationPurpose]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DestinationPurpose'), 'exclude': lambda f: f is None }})
    document_overrides_ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DocumentOverridesRef'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The reporting number."""
    identifier: Optional[shared_identifier.Identifier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Identifier'), 'exclude': lambda f: f is None }})
    r"""Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database."""
    net_remit_info: Optional[shared_netremitinfo.NetRemitInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('NetRemitInfo'), 'exclude': lambda f: f is None }})
    offer_identifier: Optional[shared_offeridentifier.OfferIdentifier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('OfferIdentifier'), 'exclude': lambda f: f is None }})
    product_identifier: Optional[shared_productidentifier.ProductIdentifier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ProductIdentifier'), 'exclude': lambda f: f is None }})
    restrictions: Optional[List[shared_restrictions.Restrictions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Restrictions'), 'exclude': lambda f: f is None }})
    ticket_designators: Optional[List[shared_ticketdesignators.TicketDesignators]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TicketDesignators'), 'exclude': lambda f: f is None }})
    tour_codes: Optional[List[shared_tourcodes.TourCodes]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TourCodes'), 'exclude': lambda f: f is None }})
    

