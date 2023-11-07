"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .guestcounts import GuestCounts
from .roomamenity import RoomAmenity
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RoomStayCandidate:
    guest_counts: GuestCounts = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('GuestCounts') }})
    room_amenity: Optional[List[RoomAmenity]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RoomAmenity'), 'exclude': lambda f: f is None }})
    

