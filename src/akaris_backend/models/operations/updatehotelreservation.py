"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import reservationdetailwrapper as shared_reservationdetailwrapper
from ...models.shared import reservationresponsewrapper as shared_reservationresponsewrapper
from typing import Optional


@dataclasses.dataclass
class UpdateHotelReservationRequest:
    identifier: str = dataclasses.field(metadata={'path_param': { 'field_name': 'Identifier', 'style': 'simple', 'explode': False }})
    r"""Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database."""
    reservation_detail_wrapper: shared_reservationdetailwrapper.ReservationDetailWrapper = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    trace_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'TraceId', 'style': 'simple', 'explode': False }})
    r"""Identifier used to correlate API invocations across long-running or multi-call business flows."""
    xauth_travelport_accessgroup: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'XAUTH_TRAVELPORT_ACCESSGROUP', 'style': 'simple', 'explode': False }})
    r"""Identifies the Travelport access group with which the caller is associated"""
    



@dataclasses.dataclass
class UpdateHotelReservationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    reservation_response_wrapper: Optional[shared_reservationresponsewrapper.ReservationResponseWrapper] = dataclasses.field(default=None)
    r"""OK - Successful Response - 200"""
    

