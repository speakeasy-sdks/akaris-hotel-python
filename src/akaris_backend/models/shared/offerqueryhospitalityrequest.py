"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .hotelaggregatorenum import HotelAggregatorEnum
from .propertykey import PropertyKey
from .ratecandidate import RateCandidate
from .roomstaycandidates import RoomStayCandidates
from akaris_backend import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OfferQueryHospitalityRequest:
    at_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type') }})
    property_key: PropertyKey = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('PropertyKey') }})
    checkin_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('checkinDate'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    checkout_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('checkoutDate'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    number_of_guests: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfGuests') }})
    r"""The number of guests"""
    hotel_aggregator: Optional[HotelAggregatorEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('HotelAggregator'), 'exclude': lambda f: f is None }})
    rate_candidate: Optional[RateCandidate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RateCandidate'), 'exclude': lambda f: f is None }})
    room_stay_candidates: Optional[RoomStayCandidates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RoomStayCandidates'), 'exclude': lambda f: f is None }})
    booking_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bookingCode'), 'exclude': lambda f: f is None }})
    r"""The booking code"""
    requested_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestedCurrency'), 'exclude': lambda f: f is None }})
    r"""You can use requested currency to request conversion rate information. The response will return the currencyRateConversion object which will contain conversion rate of the requested currency."""
    stored_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storedAmount'), 'exclude': lambda f: f is None }})
    r"""stored amount"""
    stored_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storedCurrency'), 'exclude': lambda f: f is None }})
    r"""stored currency"""
    

