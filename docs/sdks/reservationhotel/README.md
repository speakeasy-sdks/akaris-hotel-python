# ReservationHotel
(*reservation_hotel*)

### Available Operations

* [build_hotel_reservation](#build_hotel_reservation) - Single payload booking request
* [cancel_hotel_offer](#cancel_hotel_offer) - Cancel an Offer within a Reservation
* [create_hotel_reservation](#create_hotel_reservation) - Create a reservation
* [retrieve_hotel_reservation](#retrieve_hotel_reservation) - Retrieve a Reservation
* [update_hotel_reservation](#update_hotel_reservation) - Update a reservation

## build_hotel_reservation

This full payload book request allows your to reference a hotel availability response and build the Reservation in a single API call.

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.BuildHotelReservationRequest(
    reservation_query_build_wrapper=shared.ReservationQueryBuildWrapper(),
)

res = s.reservation_hotel.build_hotel_reservation(req)

if res.reservation_response_wrapper is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.BuildHotelReservationRequest](../../models/operations/buildhotelreservationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.BuildHotelReservationResponse](../../models/operations/buildhotelreservationresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## cancel_hotel_offer

Cancel an Offer by modifying the Reservation

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.CancelHotelOfferRequest(
    reservation_identifier='<value>',
)

res = s.reservation_hotel.cancel_hotel_offer(req)

if res.reservation_response_wrapper is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CancelHotelOfferRequest](../../models/operations/cancelhotelofferrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CancelHotelOfferResponse](../../models/operations/cancelhotelofferresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## create_hotel_reservation

Create a reservation on the core or with the vendor/provider.

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.CreateHotelReservationRequest(
    reservation_detail_wrapper=shared.ReservationDetailWrapper(),
)

res = s.reservation_hotel.create_hotel_reservation(req)

if res.reservation_response_wrapper is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateHotelReservationRequest](../../models/operations/createhotelreservationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.CreateHotelReservationResponse](../../models/operations/createhotelreservationresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## retrieve_hotel_reservation

Retrieve details about a held booking, or PNR. While a PNR refers to a held booking that has not been ticketed, the PNR code persists after ticketing to provide the booking records. Once a PNR has been ticketed, you can still use PNR Retrieve to return both booking and ticketing details. A Ticket Display request can also be used to retrieve any ticketed itinerary.

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.RetrieveHotelReservationRequest(
    identifier='<value>',
    identifier_type=shared.IdentifierTypeENUM.LOCATOR,
)

res = s.reservation_hotel.retrieve_hotel_reservation(req)

if res.reservation_response_wrapper is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RetrieveHotelReservationRequest](../../models/operations/retrievehotelreservationrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.RetrieveHotelReservationResponse](../../models/operations/retrievehotelreservationresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## update_hotel_reservation

The Modify Reservation request can modify an existing reservation by changing any of the following - dates, payment information, traveler first and/or last name. You can also add comments to an existing reservation. Hotel Modify can be used only for Travelport itineraries at this time. When changing dates Travelport recommends that you first send an availability request for the new dates and look for the same booking code that is on the existing reservation. An availability request is not mandatory, but a modify request will fail if the new dates are not available.

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.UpdateHotelReservationRequest(
    identifier='<value>',
    reservation_detail_wrapper=shared.ReservationDetailWrapper(),
)

res = s.reservation_hotel.update_hotel_reservation(req)

if res.reservation_response_wrapper is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateHotelReservationRequest](../../models/operations/updatehotelreservationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.UpdateHotelReservationResponse](../../models/operations/updatehotelreservationresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.BaseResponse     | 400,401,402,403,404,500 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |
