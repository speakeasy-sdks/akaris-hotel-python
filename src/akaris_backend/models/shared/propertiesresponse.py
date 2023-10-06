"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import currencyrateconversion as shared_currencyrateconversion
from ..shared import identifier as shared_identifier
from ..shared import nextsteps as shared_nextsteps
from ..shared import properties as shared_properties
from ..shared import referencelist as shared_referencelist
from ..shared import result as shared_result
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PropertiesResponse:
    currency_rate_conversion: Optional[list[shared_currencyrateconversion.CurrencyRateConversion]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CurrencyRateConversion'), 'exclude': lambda f: f is None }})
    identifier: Optional[shared_identifier.Identifier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Identifier'), 'exclude': lambda f: f is None }})
    r"""Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database."""
    next_steps: Optional[shared_nextsteps.NextSteps] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('NextSteps'), 'exclude': lambda f: f is None }})
    properties: Optional[shared_properties.Properties] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Properties'), 'exclude': lambda f: f is None }})
    reference_list: Optional[list[shared_referencelist.ReferenceList]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ReferenceList'), 'exclude': lambda f: f is None }})
    result: Optional[shared_result.Result] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Result'), 'exclude': lambda f: f is None }})
    trace_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('traceId'), 'exclude': lambda f: f is None }})
    r"""Optional ID for internal child transactions created for processing a single request (single transaction). Should be a 128 bit GUID format. Also known as ChildTrackingId."""
    transaction_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactionId'), 'exclude': lambda f: f is None }})
    r"""Unique transaction, correlation or tracking id for a single request and reply i.e. for a single transaction. Should be a 128 bit GUID format. Also know as E2ETrackingId."""
    

