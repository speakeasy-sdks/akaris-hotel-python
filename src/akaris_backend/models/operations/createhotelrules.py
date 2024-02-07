"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import offerhospitalityresponsewrapper as shared_offerhospitalityresponsewrapper
from ...models.shared import offerqueryhospitalityrequestwrapper as shared_offerqueryhospitalityrequestwrapper
from typing import Optional


@dataclasses.dataclass
class CreateHotelRulesRequest:
    offer_query_hospitality_request_wrapper: shared_offerqueryhospitalityrequestwrapper.OfferQueryHospitalityRequestWrapper = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    trace_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'TraceId', 'style': 'simple', 'explode': False }})
    r"""Identifier used to correlate API invocations across long-running or multi-call business flows."""
    xauth_travelport_accessgroup: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'XAUTH_TRAVELPORT_ACCESSGROUP', 'style': 'simple', 'explode': False }})
    r"""Identifies the Travelport access group with which the caller is associated"""
    



@dataclasses.dataclass
class CreateHotelRulesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    offer_hospitality_response_wrapper: Optional[shared_offerhospitalityresponsewrapper.OfferHospitalityResponseWrapper] = dataclasses.field(default=None)
    r"""Created - 201"""
    

