"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from akaris_backend import utils
from akaris_backend._hooks import HookContext
from akaris_backend.models import errors, operations, shared
from typing import Optional

class PrecisionSearchHotel:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def create_precision(self, request: operations.CreatePrecisionRequest) -> operations.CreatePrecisionResponse:
        r"""Precision Search hotels by property ID
        The Hotel Search by ID request searches for hotels by search by one or more property IDs. The response returns a list of properties based on the ID/s sent, and is the same as the Hotel Search by Location response.
        """
        hook_ctx = HookContext(operation_id='CreatePrecision', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/search/properties/precision'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request), **headers }
        req_content_type, data, form = utils.serialize_request_body(request, operations.CreatePrecisionRequest, "properties_query_specific_precision_property_list_wrapper", False, False, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['400','401','402','403','404','4XX','500','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        
        res = operations.CreatePrecisionResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[shared.PropertiesResponseWrapper])
                res.properties_response_wrapper = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 402, 403, 404, 500]:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.BaseResponse)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def precision_search_properties(self, request: operations.PrecisionSearchPropertiesRequest) -> operations.PrecisionSearchPropertiesResponse:
        r"""Search hotels by location
        The Hotel Search by Location request searches for hotels by (a) geographic coordinate information (b) city or state/province, and country or (c) IATA airport or city code.The response returns a list of properties using the same structure as the Hotel Search by ID response.
        """
        hook_ctx = HookContext(operation_id='PrecisionSearchProperties', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/search/properties/precision/location'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request), **headers }
        req_content_type, data, form = utils.serialize_request_body(request, operations.PrecisionSearchPropertiesRequest, "properties_query_precision_search_wrapper", False, False, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['400','401','402','403','404','4XX','500','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        
        res = operations.PrecisionSearchPropertiesResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[shared.PropertiesResponseWrapper])
                res.properties_response_wrapper = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 402, 403, 404, 500]:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.BaseResponse)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    