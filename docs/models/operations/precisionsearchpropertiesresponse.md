# PrecisionSearchPropertiesResponse


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                     | *Optional[str]*                                                                                    | :heavy_check_mark:                                                                                 | HTTP response content type for this operation                                                      |
| `properties_response_wrapper`                                                                      | [Optional[shared.PropertiesResponseWrapper]](undefined/models/shared/propertiesresponsewrapper.md) | :heavy_minus_sign:                                                                                 | OK - Successful Response - 200                                                                     |
| `status_code`                                                                                      | *Optional[int]*                                                                                    | :heavy_check_mark:                                                                                 | HTTP response status code for this operation                                                       |
| `raw_response`                                                                                     | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)              | :heavy_minus_sign:                                                                                 | Raw HTTP response; suitable for custom response parsing                                            |