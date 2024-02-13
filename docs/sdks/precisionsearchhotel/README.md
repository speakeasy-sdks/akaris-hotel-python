# PrecisionSearchHotel
(*precision_search_hotel*)

### Available Operations

* [create_precision](#create_precision) - Precision Search hotels by property ID
* [precision_search_properties](#precision_search_properties) - Search hotels by location

## create_precision

The Hotel Search by ID request searches for hotels by search by one or more property IDs. The response returns a list of properties based on the ID/s sent, and is the same as the Hotel Search by Location response.

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.CreatePrecisionRequest(
    properties_query_specific_precision_property_list_wrapper=shared.PropertiesQuerySpecificPrecisionPropertyListWrapper(),
)

res = s.precision_search_hotel.create_precision(req)

if res.properties_response_wrapper is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreatePrecisionRequest](../../models/operations/createprecisionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreatePrecisionResponse](../../models/operations/createprecisionresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## precision_search_properties

The Hotel Search by Location request searches for hotels by (a) geographic coordinate information (b) city or state/province, and country or (c) IATA airport or city code.The response returns a list of properties using the same structure as the Hotel Search by ID response.

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.PrecisionSearchPropertiesRequest(
    properties_query_precision_search_wrapper=shared.PropertiesQueryPrecisionSearchWrapper(),
)

res = s.precision_search_hotel.precision_search_properties(req)

if res.properties_response_wrapper is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PrecisionSearchPropertiesRequest](../../models/operations/precisionsearchpropertiesrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PrecisionSearchPropertiesResponse](../../models/operations/precisionsearchpropertiesresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |
