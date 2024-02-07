<!-- Start SDK Example Usage [usage] -->
```python
import akaris_backend
import dateutil.parser
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.CreateHotelAvailabilityRequest(
    catalog_offerings_query_request_hospitality_wrapper=shared.CatalogOfferingsQueryRequestHospitalityWrapper(
        catalog_offerings_query_request=shared.CatalogOfferingsQueryRequest(
            at_type='CatalogOfferingsRequestHospitality',
            catalog_offerings_request=[
                shared.CatalogOfferingsRequestHospitality(
                    stay_dates=shared.DateOrDateWindows(
                        duration='P1D',
                        end=dateutil.parser.parse('2023-03-03').date(),
                        specific=dateutil.parser.parse('2023-03-03').date(),
                        start=dateutil.parser.parse('2023-03-03').date(),
                    ),
                    at_type='CatalogOfferingsRequestHospitality',
                    hotel_search_criterion=shared.HotelSearchCriterion(
                        property_request=[
                            shared.PropertyRequest(
                                property_key=shared.PropertyKey(
                                    chain_code='HL',
                                    property_code='string',
                                ),
                                at_type='PropertyRequest',
                            ),
                        ],
                        at_type='HotelSearchCriterion',
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
                                        guest_count=[
                                            shared.GuestCount(
                                                at_type='GuestCount',
                                                age=21,
                                                age_qualifying_code='10',
                                                count=2,
                                            ),
                                        ],
                                        at_type='GuestCounts',
                                    ),
                                    room_amenity=[
                                        shared.RoomAmenity(
                                            inclusion=[
                                                'string',
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
<!-- End SDK Example Usage [usage] -->