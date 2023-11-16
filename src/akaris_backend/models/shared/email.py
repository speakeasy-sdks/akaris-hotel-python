"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .optinstatusenum import OptInStatusEnum
from .yesnoinheritenum import YesNoInheritEnum
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Email:
    r"""Electronic email addresses, in IETF specified format."""
    comment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comment'), 'exclude': lambda f: f is None }})
    r"""Assigned Type: c-1100:StringText"""
    email_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailType'), 'exclude': lambda f: f is None }})
    r"""Type of the e-mail"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Electronic email addresses, in IETF specified format."""
    opt_in_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('optInDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The datetime of receiving the opt in notice"""
    opt_in_status: Optional[OptInStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('optInStatus'), 'exclude': lambda f: f is None }})
    r"""Used to indicate marketing preferences, OptIn, OptOut"""
    opt_out_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('optOutDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The datetime the opt out notice was received"""
    opt_out_ind: Optional[YesNoInheritEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('optOutInd'), 'exclude': lambda f: f is None }})
    r"""Used to indicate marketing preferences, Yes, No, Inherit"""
    preferred_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('preferredFormat'), 'exclude': lambda f: f is None }})
    r"""Mime media type"""
    provisioned_ind: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provisionedInd'), 'exclude': lambda f: f is None }})
    r"""If true then the email address came from the provisioning process"""
    share_marketing: Optional[YesNoInheritEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shareMarketing'), 'exclude': lambda f: f is None }})
    r"""Used to indicate marketing preferences, Yes, No, Inherit"""
    share_sync: Optional[YesNoInheritEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shareSync'), 'exclude': lambda f: f is None }})
    r"""Used to indicate marketing preferences, Yes, No, Inherit"""
    valid_ind: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validInd'), 'exclude': lambda f: f is None }})
    r"""If true, this is a valid email address that has been system verified via a successful email transmission."""
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    

