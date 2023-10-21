"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..errors import nextstep as errors_nextstep
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NextSteps:
    base_uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('baseURI') }})
    r"""The base portion of the uri in order to shorten the uri's in the individual steps"""
    next_step: List[errors_nextstep.NextStep] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('NextStep') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Optional internally referenced id"""
    

