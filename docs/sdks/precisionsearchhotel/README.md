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
import dateutil.parser
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="",
    ),
)

req = operations.CreatePrecisionRequest(
    properties_query_specific_precision_property_list_wrapper=shared.PropertiesQuerySpecificPrecisionPropertyListWrapper(
        properties_query_specific_precision_property_list=shared.PropertiesQuerySpecificPrecisionPropertyList(
            at_type='PropertiesQuerySpecificPropertyList',
            commissionable_ind=False,
            meals_included=shared.MealsIncluded(
                breakfast_ind=False,
                dinner_ind=False,
                lunch_ind=False,
            ),
            property_key=[
                shared.PropertyKey(
                    at_type='City',
                    chain_code='HL',
                    property_code='Northeast',
                ),
            ],
            rate_candidates=shared.RateCandidates(
                at_type='RateCandidates',
                rate_candidate=[
                    shared.RateCandidate(
                        at_type='RateCandidate',
                        chain_code='HL',
                        priority=694488,
                        property_code='HL12345',
                        rate_category=shared.RateCategoryEnum.MULTI_DAY_PACKAGE,
                        rate_code='HL123',
                    ),
                ],
                post_pay_rates_only_ind=False,
                pre_pay_rates_only_ind=False,
            ),
            refundable_ind=False,
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
                                at_type='orchid',
                                inclusion=[
                                    'intangible',
                                ],
                                name='24 hour Room Service',
                                code='lavender naive',
                                description='WiFi',
                                included_ind=False,
                                quantity=380645,
                                surcharge_ind=False,
                            ),
                        ],
                    ),
                ],
            ),
            smoking_ind=False,
            checkin_date=dateutil.parser.parse('2021-12-06').date(),
            checkout_date=dateutil.parser.parse('2023-05-08').date(),
            image_size=shared.ImageSizeEnum.THUMBNAIL,
            maximum_rate=3578.82,
            minimum_rate=6203.38,
            number_of_guests=123772,
            number_of_rooms=905681,
            requested_currency='synthesize Brand',
            return_all_images_ind=False,
        ),
    ),
    trace_id='kilogram longingly Cambridgeshire',
    xauth_travelport_accessgroup='Integration',
)

res = s.precision_search_hotel.create_precision(req)

if res.properties_response_wrapper is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreatePrecisionRequest](../../models/operations/createprecisionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreatePrecisionResponse](../../models/operations/createprecisionresponse.md)**


## precision_search_properties

The Hotel Search by Location request searches for hotels by (a) geographic coordinate information (b) city or state/province, and country or (c) IATA airport or city code.The response returns a list of properties using the same structure as the Hotel Search by ID response.

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

req = operations.PrecisionSearchPropertiesRequest(
    properties_query_precision_search_wrapper=shared.PropertiesQueryPrecisionSearchWrapper(
        properties_query_search=shared.PropertiesQueryPrecisionSearch(
            at_type='PropertiesQuerySearch',
            chain_codes=[
                'Northwest',
            ],
            check_in_date=dateutil.parser.parse('2022-03-27').date(),
            check_out_date=dateutil.parser.parse('2022-02-02').date(),
            commissionable_ind=False,
            hotel_name='Gender',
            image_size=shared.ImageSizeEnum.SMALL,
            meals_included=shared.MealsIncluded(
                breakfast_ind=False,
                dinner_ind=False,
                lunch_ind=False,
            ),
            property_amenity_code=[
                'female',
            ],
            rate_candidates=shared.RateCandidates(
                at_type='RateCandidates',
                rate_candidate=[
                    shared.RateCandidate(
                        at_type='RateCandidate',
                        chain_code='HL',
                        priority=943883,
                        property_code='HL12345',
                        rate_category=shared.RateCategoryEnum.VIP,
                        rate_code='HL123',
                    ),
                ],
                post_pay_rates_only_ind=False,
                pre_pay_rates_only_ind=False,
            ),
            refundable_ind=False,
            requested_currency='Fundamental copy defect',
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
                            at_type='male Cambridgeshire',
                            inclusion=[
                                'bulk',
                            ],
                            name='24 hour Room Service',
                            code='Cotton',
                            description='WiFi',
                            included_ind=False,
                            quantity=204092,
                            surcharge_ind=False,
                        ),
                    ],
                ),
            ],
            search_by=shared.SearchBy(
                at_type='SearchBy',
                search_radius=shared.Distance(
                    unit_of_distance=shared.UnitOfDistanceEnum.MILES,
                    value=25,
                ),
            ),
            smoking_ind=False,
            sort_order=shared.HotelSortOrderEnum.PROXIMITY,
            return_all_images_ind=False,
        ),
    ),
    trace_id='oddly system Customer',
    xauth_travelport_accessgroup='glistening Blues',
)

res = s.precision_search_hotel.precision_search_properties(req)

if res.properties_response_wrapper is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PrecisionSearchPropertiesRequest](../../models/operations/precisionsearchpropertiesrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PrecisionSearchPropertiesResponse](../../models/operations/precisionsearchpropertiesresponse.md)**

