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
        o_auth2="",
    ),
)

req = operations.BuildFromCatalogOfferingsRequest(
    offer_query_build_from_catalog_offerings_hospitality_wrapper=shared.OfferQueryBuildFromCatalogOfferingsHospitalityWrapper(
        offer_query_build_from_catalog_offerings_hospitality=shared.OfferQueryBuildFromCatalogOfferingsHospitality(
            at_type='OfferQueryBuildFromCatalogOfferingsHospitality',
            build_from_catalog_offerings_request=shared.BuildFromCatalogOfferingsRequest(
                at_type='BuildFromCatalogOfferingsRequestAir',
                ancillary_offering_identifier=[
                    shared.AncillaryOfferingIdentifier(
                        ancillary_offering_ref='AN1',
                        catalog_offering_ref='CO1',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        id='AN1',
                    ),
                ],
                catalog_offering_identifier=shared.CatalogOfferingIdentifier(
                    catalog_offering_ref='co1',
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    id='co1',
                ),
                catalog_offerings_identifier=shared.CatalogOfferingsIdentifier(
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    id='CatalogOfferings_1',
                ),
                product_identifier=[
                    shared.ProductIdentifier(
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        id='product_1',
                        product_ref='product_1',
                    ),
                    shared.ProductIdentifier(
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        id='product_1',
                        product_ref='product_1',
                    ),
                ],
            ),
        ),
    ),
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


## build_hotel_rules_from_catalog_offering

Available January 2023. Build rules by referenceing availability response

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="",
    ),
)

req = operations.BuildHotelRulesFromCatalogOfferingRequest(
    offer_query_build_from_catalog_offering_wrapper=shared.OfferQueryBuildFromCatalogOfferingWrapper(
        offer_query_build_from_catalog_offering=shared.OfferQueryBuildFromCatalogOffering(
            at_type='OfferQueryBuildFromCatalogOffering',
            build_from_catalog_offering_hospitality=shared.BuildFromCatalogOfferingHospitality(
                at_type='BuildFromCatalogOfferingHospitality',
                catalog_offering_identifier=shared.Identifier(
                    authority='TVPT',
                    value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                ),
                number_of_rooms=1,
            ),
        ),
    ),
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


## create_hotel_rules

Full Payload hotel rules request

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

req = operations.CreateHotelRulesRequest(
    offer_query_hospitality_request_wrapper=shared.OfferQueryHospitalityRequestWrapper(
        offer_query_hospitality_request=shared.OfferQueryHospitalityRequest(
            at_type='OfferQueryHospitalityRequest',
            property_key=shared.PropertyKey(
                chain_code='HL',
                property_code='Islands harness programming',
            ),
            rate_candidate=shared.RateCandidate(
                at_type='RateCandidate',
                chain_code='HL',
                property_code='HL12345',
                rate_code='HL123',
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
                                    'joyously',
                                ],
                                name='24 hour Room Service',
                                description='WiFi',
                            ),
                        ],
                    ),
                ],
            ),
            checkin_date=dateutil.parser.parse('2023-05-22').date(),
            checkout_date=dateutil.parser.parse('2023-09-14').date(),
            number_of_guests=105598,
        ),
    ),
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

