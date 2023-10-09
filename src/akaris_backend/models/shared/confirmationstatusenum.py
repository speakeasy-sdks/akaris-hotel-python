"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class ConfirmationStatusEnum(str, Enum):
    r"""Status returned in a response for a two or more phase commitment process"""
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    CANCELLED = 'Cancelled'
    REJECTED = 'Rejected'