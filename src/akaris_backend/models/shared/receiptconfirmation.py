"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import confirmation as shared_confirmation
from ..shared import identifier as shared_identifier
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ReceiptConfirmation:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    confirmation: Optional[shared_confirmation.Confirmation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Confirmation'), 'exclude': lambda f: f is None }})
    date_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dateTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""Receipt date time"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The verification number."""
    identifier: Optional[shared_identifier.Identifier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Identifier'), 'exclude': lambda f: f is None }})
    r"""Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database."""
    offer_ref: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('OfferRef'), 'exclude': lambda f: f is None }})
    r"""List of offers which links with the receipt"""
    product_ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ProductRef'), 'exclude': lambda f: f is None }})
    r"""Reference of product"""
    receipt_ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ReceiptRef'), 'exclude': lambda f: f is None }})
    segment_sequence_list: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('SegmentSequenceList'), 'exclude': lambda f: f is None }})
    r"""The segmentSequenceList the ReceiptConfirmation applies to"""
    

