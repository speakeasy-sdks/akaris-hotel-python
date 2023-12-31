"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .nextstepmethodenum import NextStepMethodEnum
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NextStep:
    r"""A URL that describes a step that can be applied to the resource containing the next step structure."""
    action: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action') }})
    r"""The action this next step is intended to achieve"""
    method: NextStepMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    r"""Describes the set of potential methods that can be taken after an operation."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Additional clarification for the next step"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the Next Step"""
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    

