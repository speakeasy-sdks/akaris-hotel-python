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
                                    at_type='Philippines North',
                                    chain_code='HL',
                                    property_code='male Locks',
                                ),
                                more_rates_token='whereas',
                            ),
                        ],
                        rate_candidates=shared.RateCandidates(
                            at_type='RateCandidates',
                            rate_candidate=[
                                shared.RateCandidate(
                                    at_type='RateCandidate',
                                    chain_code='HL',
                                    priority=219354,
                                    property_code='HL12345',
                                    rate_category=shared.RateCategoryEnum.OTHER,
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
                                            at_type='buckwheat HEX eius',
                                            inclusion=[
                                                'Screen',
                                            ],
                                            name='24 hour Room Service',
                                            code='Paradigm East',
                                            description='WiFi',
                                            included_ind=False,
                                            quantity=561488,
                                            surcharge_ind=False,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        number_of_rooms=747350,
                    ),
                    maximum_amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        currency_source=shared.CurrencySourceEnum.SUPPLIER,
                        minor_unit=2,
                        value=124.56,
                    ),
                    minimum_amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        currency_source=shared.CurrencySourceEnum.SUPPLIER,
                        minor_unit=2,
                        value=124.56,
                    ),
                    search_control_console_channel_id=shared.SearchControlConsoleChannelID(
                        scc_type='multimedia Pop',
                        value='2',
                    ),
                    stay_dates=shared.DateOrDateWindows(
                        duration='P1D',
                        duration_unit=shared.DurationUnitEnum.HOURS,
                        end=dateutil.parser.parse('2023-03-03').date(),
                        specific=dateutil.parser.parse('2023-03-03').date(),
                        start=dateutil.parser.parse('2023-03-03').date(),
                    ),
                    max_response_wait_time=37199,
                    requested_currency='ROI',
                    verbose_response_ind=False,
                ),
            ],
        ),
    ),
    trace_id='Folk Washington female',
    xauth_travelport_accessgroup='phooey poorly male',
)

res = s.hotel_availability.create_hotel_availability(req)

if res.catalog_offerings_hospitality_response_wrapper is not None:
    # handle response
```
<!-- End SDK Example Usage -->