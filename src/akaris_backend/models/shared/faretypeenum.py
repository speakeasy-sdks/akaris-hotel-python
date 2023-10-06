"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class FareTypeEnum(str, Enum):
    r"""Defines the type of fares to return (Only public fares, Only private fares, Only agency private fares, Only"""
    PUBLIC_FARE = 'PublicFare'
    AGENCY_PRIVATE_FARE = 'AgencyPrivateFare'
    AIRLINE_PRIVATE_FARE = 'AirlinePrivateFare'
    NET_FARE = 'NetFare'
