"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import reservationdetail as shared_reservationdetail
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ReservationDetailWrapper:
    reservation_detail: Optional[shared_reservationdetail.ReservationDetail] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ReservationDetail'), 'exclude': lambda f: f is None }})
    

