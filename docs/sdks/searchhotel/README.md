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
import dateutil.parser
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="",
    ),
)

req = operations.CreateRequest(
    properties_query_specific_property_list_wrapper=shared.PropertiesQuerySpecificPropertyListWrapper(
        properties_query_specific_property_list=shared.PropertiesQuerySpecificPropertyList(
            at_type='PropertiesQuerySpecificPropertyList',
            property_key=[
                shared.PropertyKey(
                    at_type='Electric pirouette',
                    chain_code='HL',
                    property_code='Sausages ASCII',
                ),
            ],
            rate_candidates=shared.RateCandidates(
                at_type='RateCandidates',
                rate_candidate=[
                    shared.RateCandidate(
                        at_type='RateCandidate',
                        chain_code='HL',
                        priority=754558,
                        property_code='HL12345',
                        rate_category=shared.RateCategoryEnum.LEISURE,
                        rate_code='HL123',
                    ),
                ],
                post_pay_rates_only_ind=False,
                pre_pay_rates_only_ind=False,
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
                                at_type='4th connecting',
                                inclusion=[
                                    'Bespoke',
                                ],
                                name='24 hour Room Service',
                                code='Congo channels AGP',
                                description='WiFi',
                                included_ind=False,
                                quantity=373347,
                                surcharge_ind=False,
                            ),
                        ],
                    ),
                ],
            ),
            checkin_date=dateutil.parser.parse('2022-02-20').date(),
            checkout_date=dateutil.parser.parse('2021-05-08').date(),
            image_size=shared.ImageSizeEnum.SMALL,
            maximum_rate=7587.04,
            minimum_rate=4275.16,
            number_of_guests=418992,
            number_of_rooms=285813,
            requested_currency='mesh',
            return_all_images_ind=False,
        ),
    ),
    trace_id='silver compressing Berkshire',
    xauth_travelport_accessgroup='neque mainstream',
)

res = s.search_hotel.create(req)

if res.properties_response_wrapper is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [operations.CreateRequest](../../models/operations/createrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateResponse](../../models/operations/createresponse.md)**


## get_properties_detail

The optional Hotel Details request retrieves for one specified property a detailed description and additional images after a hotel search.

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="",
    ),
)

req = operations.GetPropertiesDetailRequest(
    image_size=shared.ImageSizeEnum.SMALL,
    trace_id='Barium haptic Lead',
    xauth_travelport_accessgroup='array Diverse Northwest',
    chain_code='payment East ah',
    property_code='transform Rustic',
)

res = s.search_hotel.get_properties_detail(req)

if res.properties_response_wrapper is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetPropertiesDetailRequest](../../models/operations/getpropertiesdetailrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetPropertiesDetailResponse](../../models/operations/getpropertiesdetailresponse.md)**


## get_properties_page

Hotel Search uses pagination by default. The initial search response returns 25 properties, notes the total number of properties found, and includes an identifier to be used for retrieving additional pages. Call the GET pagination endpoint to retrieve each additional page of 25 properties until the end of the list is reached.The identifier used for paging is saved for 30 minutes. A new hotel search request must be performed after it expires.

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="",
    ),
)

req = operations.GetPropertiesPageRequest(
    trace_id='toothbrush',
    xauth_travelport_accessgroup='Cambridgeshire',
    identifier='synergies Executive female',
    page_number='quantifying Tesla',
)

res = s.search_hotel.get_properties_page(req)

if res.properties_response_wrapper is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetPropertiesPageRequest](../../models/operations/getpropertiespagerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetPropertiesPageResponse](../../models/operations/getpropertiespageresponse.md)**


## search_properties

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

req = operations.SearchPropertiesRequest(
    properties_query_search_wrapper=shared.PropertiesQuerySearchWrapper(
        properties_query_search=shared.PropertiesQuerySearch(
            at_type='PropertiesQuerySearch',
            chain_codes=[
                'Communications',
            ],
            check_in_date=dateutil.parser.parse('2022-01-14').date(),
            check_out_date=dateutil.parser.parse('2022-11-04').date(),
            hotel_name='Clarita neural synthesize',
            image_size=shared.ImageSizeEnum.MEDIUM,
            property_amenity_code=[
                'Tricycle',
            ],
            rate_candidates=shared.RateCandidates(
                at_type='RateCandidates',
                rate_candidate=[
                    shared.RateCandidate(
                        at_type='RateCandidate',
                        chain_code='HL',
                        priority=163919,
                        property_code='HL12345',
                        rate_category=shared.RateCategoryEnum.CORPORATE,
                        rate_code='HL123',
                    ),
                ],
                post_pay_rates_only_ind=False,
                pre_pay_rates_only_ind=False,
            ),
            requested_currency='Sharable deploy Sports',
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
                            at_type='Southeast Gloves array',
                            inclusion=[
                                'United',
                            ],
                            name='24 hour Room Service',
                            code='lime',
                            description='WiFi',
                            included_ind=False,
                            quantity=146819,
                            surcharge_ind=False,
                        ),
                    ],
                ),
            ],
            search_by=shared.SearchBy(
                at_type='SearchBy',
                search_radius=shared.Distance(
                    unit_of_distance=shared.UnitOfDistanceEnum.KILOMETERS,
                    value=25,
                ),
            ),
            sort_order=shared.HotelSortOrderEnum.STAR_RATING,
            return_all_images_ind=False,
        ),
    ),
    trace_id='South',
    xauth_travelport_accessgroup='Wooden',
)

res = s.search_hotel.search_properties(req)

if res.properties_response_wrapper is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.SearchPropertiesRequest](../../models/operations/searchpropertiesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.SearchPropertiesResponse](../../models/operations/searchpropertiesresponse.md)**

