# akaris-backend

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/akaris-hotel-python.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/akaris-hotel-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/akaris-hotel-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
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
                                    property_code='Philippines North',
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
                                                'yowza',
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
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [hotel_availability](docs/sdks/hotelavailability/README.md)

* [create_hotel_availability](docs/sdks/hotelavailability/README.md#create_hotel_availability) - Request hotel availability
* [hotel_availability_from_properties](docs/sdks/hotelavailability/README.md#hotel_availability_from_properties) - Request hotel availability from precision search response

### [hotel_rules](docs/sdks/hotelrules/README.md)

* [build_from_catalog_offerings](docs/sdks/hotelrules/README.md#build_from_catalog_offerings) - To be deprecated and replaced with buildfromcatalogoffering
* [build_hotel_rules_from_catalog_offering](docs/sdks/hotelrules/README.md#build_hotel_rules_from_catalog_offering) - Available January 2023. Build rules by referenceing availability response
* [create_hotel_rules](docs/sdks/hotelrules/README.md#create_hotel_rules) - Full Payload hotel rules request

### [precision_search_hotel](docs/sdks/precisionsearchhotel/README.md)

* [create_precision](docs/sdks/precisionsearchhotel/README.md#create_precision) - Precision Search hotels by property ID
* [precision_search_properties](docs/sdks/precisionsearchhotel/README.md#precision_search_properties) - Search hotels by location

### [reservation_hotel](docs/sdks/reservationhotel/README.md)

* [build_hotel_reservation](docs/sdks/reservationhotel/README.md#build_hotel_reservation) - Single payload booking request
* [cancel_hotel_offer](docs/sdks/reservationhotel/README.md#cancel_hotel_offer) - Cancel an Offer within a Reservation
* [create_hotel_reservation](docs/sdks/reservationhotel/README.md#create_hotel_reservation) - Create a reservation
* [retrieve_hotel_reservation](docs/sdks/reservationhotel/README.md#retrieve_hotel_reservation) - Retrieve a Reservation
* [update_hotel_reservation](docs/sdks/reservationhotel/README.md#update_hotel_reservation) - Update a reservation

### [search_hotel](docs/sdks/searchhotel/README.md)

* [create](docs/sdks/searchhotel/README.md#create) - Search hotels by property ID
* [get_properties_detail](docs/sdks/searchhotel/README.md#get_properties_detail) - Request hotel details
* [get_properties_page](docs/sdks/searchhotel/README.md#get_properties_page) - Return additional search results (pagination)
* [search_properties](docs/sdks/searchhotel/README.md#search_properties) - Search hotels by location
<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->

<!-- End Dev Containers -->

<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
