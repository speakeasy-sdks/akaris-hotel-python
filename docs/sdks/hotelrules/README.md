# HotelRules
(*hotel_rules*)

### Available Operations

* [build_from_catalog_offerings](#build_from_catalog_offerings) - To be deprecated and replaced with buildfromcatalogoffering
* [build_hotel_rules_from_catalog_offering](#build_hotel_rules_from_catalog_offering) - Available January 2023. Build rules by referenceing availability response
* [create_hotel_rules](#create_hotel_rules) - Full Payload hotel rules request

## build_from_catalog_offerings

To be deprecated and replaced with buildfromcatalogoffering

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.BuildFromCatalogOfferingsRequest(
    offer_query_build_from_catalog_offerings_hospitality_wrapper=shared.OfferQueryBuildFromCatalogOfferingsHospitalityWrapper(),
)

res = s.hotel_rules.build_from_catalog_offerings(req)

if res.offer_hospitality_response_wrapper is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.BuildFromCatalogOfferingsRequest](../../models/operations/buildfromcatalogofferingsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.BuildFromCatalogOfferingsResponse](../../models/operations/buildfromcatalogofferingsresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## build_hotel_rules_from_catalog_offering

Available January 2023. Build rules by referenceing availability response

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.BuildHotelRulesFromCatalogOfferingRequest(
    offer_query_build_from_catalog_offering_wrapper=shared.OfferQueryBuildFromCatalogOfferingWrapper(),
)

res = s.hotel_rules.build_hotel_rules_from_catalog_offering(req)

if res.offer_hospitality_response_wrapper is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.BuildHotelRulesFromCatalogOfferingRequest](../../models/operations/buildhotelrulesfromcatalogofferingrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.BuildHotelRulesFromCatalogOfferingResponse](../../models/operations/buildhotelrulesfromcatalogofferingresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## create_hotel_rules

Full Payload hotel rules request

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.CreateHotelRulesRequest(
    offer_query_hospitality_request_wrapper=shared.OfferQueryHospitalityRequestWrapper(),
)

res = s.hotel_rules.create_hotel_rules(req)

if res.offer_hospitality_response_wrapper is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateHotelRulesRequest](../../models/operations/createhotelrulesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateHotelRulesResponse](../../models/operations/createhotelrulesresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |
