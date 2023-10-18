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
import dateutil.parser
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="",
    ),
)

req = operations.CreateHotelAvailabilityRequest(
    catalog_offerings_query_request_hospitality_wrapper=shared.CatalogOfferingsQueryRequestHospitalityWrapper(
        catalog_offerings_query_request=shared.CatalogOfferingsQueryRequest(
            at_type='CatalogOfferingsRequestHospitality',
            catalog_offerings_request=[
                shared.CatalogOfferingsRequestHospitality(
                    at_type='CatalogOfferingsRequestHospitality',
                    hotel_search_criterion=shared.HotelSearchCriterion(
                        at_type='HotelSearchCriterion',
                        property_request=[
                            shared.PropertyRequest(
                                at_type='PropertyRequest',
                                property_key=shared.PropertyKey(
                                    chain_code='HL',
                                    property_code='female',
                                ),
                            ),
                        ],
                        rate_candidates=shared.RateCandidates(
                            at_type='RateCandidates',
                            rate_candidate=[
                                shared.RateCandidate(
                                    at_type='RateCandidate',
                                    chain_code='HL',
                                    property_code='HL12345',
                                    rate_code='HL123',
                                ),
                            ],
                        ),
                        room_stay_candidates=shared.RoomStayCandidates(
                            room_stay_candidate=[
                                shared.RoomStayCandidate(
                                    guest_counts=shared.GuestCounts(
                                        at_type='GuestCounts',
                                        guest_count=[
                                            shared.GuestCount(
                                                at_type='GuestCount',
                                                age=21,
                                                age_qualifying_code='10',
                                                count=2,
                                            ),
                                        ],
                                    ),
                                    room_amenity=[
                                        shared.RoomAmenity(
                                            inclusion=[
                                                'South',
                                            ],
                                            name='24 hour Room Service',
                                            description='WiFi',
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    maximum_amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        minor_unit=2,
                        value=124.56,
                    ),
                    minimum_amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        minor_unit=2,
                        value=124.56,
                    ),
                    search_control_console_channel_id=shared.SearchControlConsoleChannelID(
                        value='2',
                    ),
                    stay_dates=shared.DateOrDateWindows(
                        duration='P1D',
                        end=dateutil.parser.parse('2023-03-03').date(),
                        specific=dateutil.parser.parse('2023-03-03').date(),
                        start=dateutil.parser.parse('2023-03-03').date(),
                    ),
                ),
            ],
        ),
    ),
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


## hotel_availability_from_properties

Hotel Availability returns room types and rates available at one or more specified properties on specified dates.

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="",
    ),
)

req = operations.HotelAvailabilityFromPropertiesRequest(
    catalog_offerings_query_build_from_properties_wrapper=shared.CatalogOfferingsQueryBuildFromPropertiesWrapper(
        catalog_offerings_query_build_from_properties=shared.CatalogOfferingsQueryBuildFromProperties(
            build_from_catalog_offering_hospitality=shared.BuildFromProperties(
                propert_info_ids=[
                    'O',
                    'N',
                    '-',
                    '6',
                    '0',
                    '1',
                    '0',
                    '6',
                ],
                properties_identifier=shared.Identifier(
                    authority='TVPT',
                    value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                ),
            ),
        ),
    ),
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

