# HotelAvailability
(*hotel_availability*)

### Available Operations

* [create_hotel_availability](#create_hotel_availability) - Request hotel availability
* [hotel_availability_from_properties](#hotel_availability_from_properties) - Request hotel availability from precision search response

## create_hotel_availability

Hotel Availability returns room types and rates available at one or more specified properties on specified dates.

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.CreateHotelAvailabilityRequest(
    catalog_offerings_query_request_hospitality_wrapper=shared.CatalogOfferingsQueryRequestHospitalityWrapper(),
)

res = s.hotel_availability.create_hotel_availability(req)

if res.catalog_offerings_hospitality_response_wrapper is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateHotelAvailabilityRequest](../../models/operations/createhotelavailabilityrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.CreateHotelAvailabilityResponse](../../models/operations/createhotelavailabilityresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## hotel_availability_from_properties

Hotel Availability returns room types and rates available at one or more specified properties on specified dates.

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.HotelAvailabilityFromPropertiesRequest(
    catalog_offerings_query_build_from_properties_wrapper=shared.CatalogOfferingsQueryBuildFromPropertiesWrapper(),
)

res = s.hotel_availability.hotel_availability_from_properties(req)

if res.catalog_offerings_hospitality_response_wrapper is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.HotelAvailabilityFromPropertiesRequest](../../models/operations/hotelavailabilityfrompropertiesrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.HotelAvailabilityFromPropertiesResponse](../../models/operations/hotelavailabilityfrompropertiesresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |
