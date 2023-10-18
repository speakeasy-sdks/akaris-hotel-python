"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import reservationquerybuildwrapper as shared_reservationquerybuildwrapper
from ..shared import reservationresponsewrapper as shared_reservationresponsewrapper
from typing import Optional


@dataclasses.dataclass
class BuildHotelReservationRequest:
    reservation_query_build_wrapper: shared_reservationquerybuildwrapper.ReservationQueryBuildWrapper = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    trace_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'TraceId', 'style': 'simple', 'explode': False }})
    r"""Identifier used to correlate API invocations across long-running or multi-call business flows."""
    xauth_travelport_accessgroup: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'XAUTH_TRAVELPORT_ACCESSGROUP', 'style': 'simple', 'explode': False }})
    r"""Identifies the Travelport access group with which the caller is associated"""
    



@dataclasses.dataclass
class BuildHotelReservationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    reservation_response_wrapper: Optional[shared_reservationresponsewrapper.ReservationResponseWrapper] = dataclasses.field(default=None)
    r"""Created - 201"""
    

