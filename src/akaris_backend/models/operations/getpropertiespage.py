"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import propertiesresponsewrapper as shared_propertiesresponsewrapper
from typing import Optional



@dataclasses.dataclass
class GetPropertiesPageRequest:
    identifier: str = dataclasses.field(metadata={'path_param': { 'field_name': 'identifier', 'style': 'simple', 'explode': False }})
    r"""The Identifier of the Properties from which a page is to be returned"""
    page_number: str = dataclasses.field(metadata={'query_param': { 'field_name': 'pageNumber', 'style': 'form', 'explode': True }})
    r"""The page number to be returned"""
    trace_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'TraceId', 'style': 'simple', 'explode': False }})
    r"""Identifier used to correlate API invocations across long-running or multi-call business flows."""
    xauth_travelport_accessgroup: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'XAUTH_TRAVELPORT_ACCESSGROUP', 'style': 'simple', 'explode': False }})
    r"""Identifies the Travelport access group with which the caller is associated"""
    




@dataclasses.dataclass
class GetPropertiesPageResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    properties_response_wrapper: Optional[shared_propertiesresponsewrapper.PropertiesResponseWrapper] = dataclasses.field(default=None)
    r"""OK - Successful Response - 200"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
