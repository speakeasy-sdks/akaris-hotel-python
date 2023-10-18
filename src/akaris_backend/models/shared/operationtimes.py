"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import dayofweekenum as shared_dayofweekenum
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OperationTimes:
    at_type: Optional[str] = dataclasses.field(default='OperationTimes', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type'), 'exclude': lambda f: f is None }})
    close_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('closeTime'), 'exclude': lambda f: f is None }})
    days_of_week: Optional[List[shared_dayofweekenum.DayOfWeekEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('daysOfWeek'), 'exclude': lambda f: f is None }})
    open_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('openTime'), 'exclude': lambda f: f is None }})
    

