"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import propertiesqueryspecificpropertylistwrapper as shared_propertiesqueryspecificpropertylistwrapper
from ...models.shared import propertiesresponsewrapper as shared_propertiesresponsewrapper
from typing import Optional


@dataclasses.dataclass
class CreateRequest:
    properties_query_specific_property_list_wrapper: shared_propertiesqueryspecificpropertylistwrapper.PropertiesQuerySpecificPropertyListWrapper = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    trace_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'TraceId', 'style': 'simple', 'explode': False }})
    r"""Identifier used to correlate API invocations across long-running or multi-call business flows."""
    xauth_travelport_accessgroup: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'XAUTH_TRAVELPORT_ACCESSGROUP', 'style': 'simple', 'explode': False }})
    r"""Identifies the Travelport access group with which the caller is associated"""
    



@dataclasses.dataclass
class CreateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    properties_response_wrapper: Optional[shared_propertiesresponsewrapper.PropertiesResponseWrapper] = dataclasses.field(default=None)
    r"""Created - 201"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

