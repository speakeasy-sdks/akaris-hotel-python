"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import reservationbuild as shared_reservationbuild
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReservationQueryBuild:
    reservation_build: shared_reservationbuild.ReservationBuild = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ReservationBuild') }})
    at_type: Optional[str] = dataclasses.field(default='ReservationQueryBuild', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type'), 'exclude': lambda f: f is None }})
    

