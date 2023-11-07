"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .hotelsortorderenum import HotelSortOrderEnum
from .imagesizeenum import ImageSizeEnum
from .mealsincluded import MealsIncluded
from .ratecandidates import RateCandidates
from .roomstaycandidate import RoomStayCandidate
from .searchby import SearchBy
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PropertiesQueryPrecisionSearch:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    check_in_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CheckInDate'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""Check In Date"""
    check_out_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CheckOutDate'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""Check Out Date"""
    search_by: SearchBy = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('SearchBy') }})
    chain_codes: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ChainCodes'), 'exclude': lambda f: f is None }})
    r"""The permitted property chain code(s) to be returned for this request"""
    commissionable_ind: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CommissionableInd'), 'exclude': lambda f: f is None }})
    r"""If true, return Properties with at least one commissionable rate."""
    hotel_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('HotelName'), 'exclude': lambda f: f is None }})
    r"""The preferred name of the property"""
    image_size: Optional[ImageSizeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ImageSize'), 'exclude': lambda f: f is None }})
    r"""Indicates the size of the image. Hospitality APIs no longer support thumbnail"""
    meals_included: Optional[MealsIncluded] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('MealsIncluded'), 'exclude': lambda f: f is None }})
    r"""Indicates if a meal is included"""
    property_amenity_code: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('PropertyAmenityCode'), 'exclude': lambda f: f is None }})
    rate_candidates: Optional[RateCandidates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RateCandidates'), 'exclude': lambda f: f is None }})
    refundable_ind: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RefundableInd'), 'exclude': lambda f: f is None }})
    r"""If true, return Properties with at least one refundable rate."""
    requested_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RequestedCurrency'), 'exclude': lambda f: f is None }})
    r"""You can use requested currency to request conversion rate information. The response will return the currencyRateConversion object which will contain conversion rate of the requested currency."""
    return_all_images_ind: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('returnAllImagesInd'), 'exclude': lambda f: f is None }})
    r"""If true, all property images of the size requested will be returned. If blank or false the best single property image will be returned."""
    room_stay_candidate: Optional[List[RoomStayCandidate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RoomStayCandidate'), 'exclude': lambda f: f is None }})
    smoking_ind: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('SmokingInd'), 'exclude': lambda f: f is None }})
    r"""If true, return Properties with at least one rate for a smoking room."""
    sort_order: Optional[HotelSortOrderEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('SortOrder'), 'exclude': lambda f: f is None }})
    r"""The method to be used in sorting hotel properties"""
    

