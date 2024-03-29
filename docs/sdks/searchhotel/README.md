# SearchHotel
(*search_hotel*)

### Available Operations

* [create](#create) - Search hotels by property ID
* [get_properties_detail](#get_properties_detail) - Request hotel details
* [get_properties_page](#get_properties_page) - Return additional search results (pagination)
* [search_properties](#search_properties) - Search hotels by location

## create

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

req = operations.CreateRequest(
    properties_query_specific_property_list_wrapper=shared.PropertiesQuerySpecificPropertyListWrapper(),
)

res = s.search_hotel.create(req)

if res.properties_response_wrapper is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [operations.CreateRequest](../../models/operations/createrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateResponse](../../models/operations/createresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## get_properties_detail

The optional Hotel Details request retrieves for one specified property a detailed description and additional images after a hotel search.

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.GetPropertiesDetailRequest(
    chain_code='<value>',
    property_code='<value>',
)

res = s.search_hotel.get_properties_detail(req)

if res.properties_response_wrapper is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetPropertiesDetailRequest](../../models/operations/getpropertiesdetailrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetPropertiesDetailResponse](../../models/operations/getpropertiesdetailresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## get_properties_page

Hotel Search uses pagination by default. The initial search response returns 25 properties, notes the total number of properties found, and includes an identifier to be used for retrieving additional pages. Call the GET pagination endpoint to retrieve each additional page of 25 properties until the end of the list is reached.The identifier used for paging is saved for 30 minutes. A new hotel search request must be performed after it expires.

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.GetPropertiesPageRequest(
    identifier='<value>',
    page_number='<value>',
)

res = s.search_hotel.get_properties_page(req)

if res.properties_response_wrapper is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetPropertiesPageRequest](../../models/operations/getpropertiespagerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetPropertiesPageResponse](../../models/operations/getpropertiespageresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## search_properties

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

req = operations.SearchPropertiesRequest(
    properties_query_search_wrapper=shared.PropertiesQuerySearchWrapper(),
)

res = s.search_hotel.search_properties(req)

if res.properties_response_wrapper is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.SearchPropertiesRequest](../../models/operations/searchpropertiesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.SearchPropertiesResponse](../../models/operations/searchpropertiesresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |
