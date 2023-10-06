"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass

from .utils.retries import RetryConfig


SERVERS = [
    'https://api.pp.travelport.com/11/hotel',
    'https://api.travelport.com/11/hotel',
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests.Session
    security_client: requests.Session
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = '11.11.0'
    sdk_version: str = '0.1.0'
    gen_version: str = '2.147.0'
    user_agent: str = 'speakeasy-sdk/python 0.1.0 2.147.0 11.11.0 akaris-backend'
    retry_config: RetryConfig = None

    def get_server_details(self) -> tuple[str, dict[str, str]]:
        if self.server_url:
            return self.server_url.removesuffix('/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}
