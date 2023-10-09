"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import imagesizeenum as shared_imagesizeenum
from ..shared import propertykey as shared_propertykey
from ..shared import ratecandidates as shared_ratecandidates
from ..shared import roomstaycandidates as shared_roomstaycandidates
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PropertiesQuerySpecificPropertyList:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    checkin_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('checkinDate'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""Checkin date"""
    checkout_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('checkoutDate'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""Checkout date"""
    number_of_guests: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfGuests') }})
    r"""Number of travelers. Must be a numeric value between 1 and 9."""
    property_key: list[shared_propertykey.PropertyKey] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('PropertyKey') }})
    image_size: Optional[shared_imagesizeenum.ImageSizeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imageSize'), 'exclude': lambda f: f is None }})
    r"""Indicates the size of the image. Hospitality APIs no longer support thumbnail"""
    maximum_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maximumRate'), 'exclude': lambda f: f is None }})
    r"""Maximum rate"""
    minimum_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimumRate'), 'exclude': lambda f: f is None }})
    r"""Minimum rate"""
    number_of_rooms: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfRooms'), 'exclude': lambda f: f is None }})
    r"""Number of rooms"""
    rate_candidates: Optional[shared_ratecandidates.RateCandidates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RateCandidates'), 'exclude': lambda f: f is None }})
    requested_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestedCurrency'), 'exclude': lambda f: f is None }})
    r"""You can use requested currency to request conversion rate information. The response will return the currencyRateConversion object which will contain conversion rate of the requested currency."""
    return_all_images_ind: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('returnAllImagesInd'), 'exclude': lambda f: f is None }})
    r"""If true, all property images of the size requested will be returned. If blank or false the best single property image will be returned."""
    room_stay_candidates: Optional[shared_roomstaycandidates.RoomStayCandidates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RoomStayCandidates'), 'exclude': lambda f: f is None }})
    
