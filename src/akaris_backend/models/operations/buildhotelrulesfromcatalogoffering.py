"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import offerhospitalityresponsewrapper as shared_offerhospitalityresponsewrapper
from ..shared import offerquerybuildfromcatalogofferingwrapper as shared_offerquerybuildfromcatalogofferingwrapper
from typing import Optional



@dataclasses.dataclass
class BuildHotelRulesFromCatalogOfferingRequest:
    offer_query_build_from_catalog_offering_wrapper: shared_offerquerybuildfromcatalogofferingwrapper.OfferQueryBuildFromCatalogOfferingWrapper = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    trace_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'TraceId', 'style': 'simple', 'explode': False }})
    r"""Identifier used to correlate API invocations across long-running or multi-call business flows."""
    xauth_travelport_accessgroup: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'XAUTH_TRAVELPORT_ACCESSGROUP', 'style': 'simple', 'explode': False }})
    r"""Identifies the Travelport access group with which the caller is associated"""
    




@dataclasses.dataclass
class BuildHotelRulesFromCatalogOfferingResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    offer_hospitality_response_wrapper: Optional[shared_offerhospitalityresponsewrapper.OfferHospitalityResponseWrapper] = dataclasses.field(default=None)
    r"""Created - 201"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

