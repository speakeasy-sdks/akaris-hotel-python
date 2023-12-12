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
import dateutil.parser
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.BuildHotelReservationRequest(
    reservation_query_build_wrapper=shared.ReservationQueryBuildWrapper(
        reservation_query_build=shared.ReservationQueryBuild(
            reservation_build=shared.ReservationBuild(
                at_type='ReservationBuildFromCatalogOfferings',
                accounting=shared.AccountingID(
                    at_type='Accounting',
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                ),
                document_overrides=[
                    shared.DocumentOverridesID(
                        at_type='DocumentOverrides',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                    ),
                ],
                form_of_payment=[
                    shared.FormOfPaymentID(
                        at_type='FormOfPaymentPaymentCard',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                    ),
                ],
                payment=[
                    shared.PaymentID(
                        at_type='Payment',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                    ),
                ],
                preference=[
                    shared.PreferenceID(
                        at_type='Preference',
                    ),
                ],
                primary_contact=[
                    shared.PrimaryContactID(
                        at_type='PrimaryContact',
                    ),
                ],
                receipt_confirmation=shared.ReceiptConfirmation(
                    at_type='ReceiptConfirmation',
                    confirmation=shared.Confirmation(
                        at_type='ConfirmationHold',
                    ),
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    offer_ref=[
                        'string',
                    ],
                    receipt_ref='6773 2389 2239 2832',
                    segment_sequence_list=[
                        248317,
                    ],
                    id='3493289238',
                ),
                reservation_comment=[
                    shared.ReservationCommentID(
                        at_type='ReservationComment',
                    ),
                ],
                special_service=[
                    shared.SpecialServiceID(
                        at_type='SpecialService',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                    ),
                ],
                travel_agency=shared.TravelAgency(
                    at_type='TravelAgencyDetail',
                    corporate_code='Air Agency',
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    organization_name=shared.CompanyName(
                        code='AI',
                        code_context='ISO',
                        department='Adventure department',
                        division='Travel Division',
                        id='2',
                        short_name='Aventure Inc',
                        system_of_record=[
                            '["1G","1V","MB","HZ"]',
                        ],
                    ),
                    profile_name=[
                        'string',
                    ],
                    travel_organization_ref='TravelAgency_1',
                    id='2',
                ),
                traveler=[
                    shared.TravelerID(
                        at_type='TravelerDetail',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                    ),
                ],
            ),
        ),
    ),
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
| errors.SDKError         | 400-600                 | */*                     |

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
    reservation_identifier='string',
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
| errors.SDKError         | 400-600                 | */*                     |

## create_hotel_reservation

Create a reservation on the core or with the vendor/provider.

### Example Usage

```python
import akaris_backend
import dateutil.parser
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.CreateHotelReservationRequest(
    reservation_detail_wrapper=shared.ReservationDetailWrapper(
        reservation_detail=shared.ReservationDetail(
            at_type='Reservation',
            accounting=shared.Accounting(
                at_type='Accounting',
                identifier=shared.Identifier(
                    authority='TVPT',
                    value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                ),
                name_value_pair=[
                    shared.NameValuePair(
                        id='6',
                        name='Day1',
                        value='Sunday',
                    ),
                ],
                data_type='DateTime',
                template='Internal Finance template',
            ),
            agency_service_fee=[
                shared.AgencyServiceFee(
                    at_type='AgencyServiceFee',
                    amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        minor_unit=2,
                        value=124.56,
                    ),
                    description='Flight reservation service fee',
                    related_document_number=shared.DocumentNumber(
                        document_issuer='BA',
                        document_type=shared.DocumentTypeEnum.TICKET,
                        value='1259900123456',
                    ),
                    tax=[
                        shared.Tax(
                            code_authority='ISO',
                            currency_code='USD',
                            decimal_authority='ISO',
                            decimal_place=2,
                            description='Additional details.',
                            exempt_ind=True,
                            purpose='Fuel',
                            reporting_authority='JFK1',
                            tax_code='7702',
                            value=12.2,
                        ),
                    ],
                    id='AgencyServiceFee_1',
                ),
            ],
            document_overrides=[
                shared.DocumentOverrides(
                    at_type='DocumentOverrides',
                    change_fee_collection_method=shared.ChangeFeeCollectionMethod(
                        change_fee_issued_separately_ind=True,
                        code='f2142',
                        description='Change fee collection method',
                        sub_code='631b',
                        tax_included_in_base_amount_ind=True,
                        value=shared.ChangeFeeMethodEnum(
                            value=shared.ChangeFeeMethodEnumBase.EMD,
                        ),
                    ),
                    commissions=[
                        shared.Commissions(
                            apply_to=shared.CommissionApplyEnum.BASE,
                            commission=shared.Commission(
                                at_type='Commission',
                            ),
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                ),
                            ],
                        ),
                    ],
                    destination_purpose=[
                        shared.DestinationPurpose(
                            at_type='DestinationPurpose',
                            destination=shared.DestinationEnum.ISLANDS_AND_COUNTRIES_OF_THE_CARIBBEAN,
                            purpose=shared.PurposeEnum.BUSINESS,
                        ),
                    ],
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    net_remit_info=shared.NetRemitInfo(
                        at_type='NetRemitInfo',
                        actual_selling_fare=100.5,
                        car_code='ACAR',
                        net_base_amount=shared.FiledAmount(
                            code_authority='Australian Dollar',
                            currency_code='USD',
                            decimal_authority='ISO 4217',
                            decimal_place=3,
                            value=43.3422,
                        ),
                        value_code='D1000',
                    ),
                    offer_identifier=shared.OfferIdentifier(
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        id='offer_1',
                        offer_ref='offer_1',
                    ),
                    product_identifier=shared.ProductIdentifier(
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        id='product_1',
                        product_ref='product_1',
                    ),
                    restrictions=[
                        shared.Restrictions(
                            document_type=shared.DocumentTypeEnum.TICKET,
                            restriction=[
                                'string',
                            ],
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                ),
                            ],
                        ),
                    ],
                    ticket_designators=[
                        shared.TicketDesignators(
                            at_type='string',
                            ticket_designator='string',
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                ),
                            ],
                        ),
                    ],
                    tour_codes=[
                        shared.TourCodes(
                            at_type='TourCodes',
                            tour_code=shared.TourCode(),
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            form_of_payment=[
                shared.FormOfPaymentID(
                    at_type='FormOfPaymentPaymentCard',
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                ),
            ],
            identifier=shared.Identifier(
                authority='TVPT',
                value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
            ),
            offer=[
                shared.Offer(
                    at_type='Offer',
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    price=shared.Price(
                        at_type='PriceDetail',
                        base=20.2,
                        currency_code=shared.CurrencyCode(
                            code_authority='ISO 4217',
                            decimal_authority='ISO 4217',
                            decimal_place=4,
                            value='USD',
                        ),
                        total_fees=201,
                        total_price=34,
                        total_taxes=34.4,
                        vendor_currency_total=shared.VendorCurrencyTotal(
                            base=120.2,
                            currency_code=shared.CurrencyCode(
                                code_authority='ISO 4217',
                                decimal_authority='ISO 4217',
                                decimal_place=4,
                                value='USD',
                            ),
                            fees=shared.Fees(
                                at_type='FeesDetail',
                                total_fees=111.11,
                            ),
                            taxes=shared.Taxes(
                                at_type='TaxesDetail',
                                tax_info=[
                                    shared.TaxInfo(
                                        amount=2234.1,
                                        currency_code=shared.CurrencyCode(
                                            code_authority='ISO 4217',
                                            decimal_authority='ISO 4217',
                                            decimal_place=4,
                                            value='USD',
                                        ),
                                        tax_breakdown=[
                                            shared.TaxBreakdown(
                                                airport_code='MIA',
                                                currency_code=shared.CurrencyCode(
                                                    code_authority='ISO 4217',
                                                    decimal_authority='ISO 4217',
                                                    decimal_place=4,
                                                    value='USD',
                                                ),
                                            ),
                                        ],
                                        tax_code='XF',
                                    ),
                                ],
                                total_taxes=330.1,
                            ),
                            total=30.13,
                            approximate_ind=True,
                        ),
                        id='2',
                    ),
                    product=[
                        shared.ProductID(
                            at_type='ProductAir',
                            identifier=shared.Identifier(
                                authority='TVPT',
                                value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                            ),
                            id='product_1',
                            product_ref='product_1',
                        ),
                    ],
                    terms_and_conditions_full=[
                        shared.TermsAndConditionsFull(
                            at_type='TermsAndConditionsFullAir',
                            customer_loyalty=[
                                shared.CustomerLoyalty(
                                    card_holder_name='John Smith',
                                    id='Loyalty_1',
                                    priority=2,
                                    program_id='United',
                                    program_name='Mileage Plus',
                                    share_with_supplier=[
                                        'LH NH SQ',
                                    ],
                                    supplier='UA',
                                    supplier_type='Airline',
                                    tier='Silver',
                                    validated_ind=True,
                                    value='132456',
                                ),
                            ],
                            identifier=shared.Identifier(
                                authority='TVPT',
                                value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                            ),
                            text_block=[
                                shared.TextBlock(
                                    at_type='TextBlockDetail',
                                    text_formatted=[
                                        shared.TextFormatted(
                                            language='English',
                                            value='Formatted text',
                                        ),
                                    ],
                                    id='2',
                                    title='Baggage Details',
                                ),
                            ],
                            id='TC_1',
                            terms_and_conditions_ref='TC_1',
                        ),
                    ],
                    id='offer_1',
                    offer_ref='offer_1',
                    parent_offer_ref='offer_1',
                    passive_offer_ind=True,
                ),
            ],
            offer_link=[
                shared.OfferLink(
                    at_type='OfferLink',
                    parent_offer=shared.ParentOffer(
                        at_type='ParentOffer',
                    ),
                ),
            ],
            organization_loyalty_program=[
                shared.OrganizationLoyaltyProgram(
                    at_type='OrganizationLoyaltyProgramID',
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    loyalty_identifier='LP029381',
                    supplier='Air canada',
                ),
            ],
            payment=[
                shared.Payment(
                    at_type='Payment',
                    agency_service_fee_identifier=[
                        shared.AgencyServiceFeeIdentifier(),
                    ],
                    amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        minor_unit=2,
                        value=124.56,
                    ),
                    base_amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        minor_unit=2,
                        value=124.56,
                    ),
                    extended_payment=shared.ExtendedPayment(
                        first_installment=100,
                        number_of_installments=6,
                        remaining_amount=50,
                    ),
                    fees=shared.Fees(
                        at_type='FeesDetail',
                        total_fees=111.11,
                    ),
                    form_of_payment_identifier=shared.FormOfPaymentIdentifier(
                        at_type='FormOfPaymentPaymentCash',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                    ),
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    offer_identifier=[
                        shared.OfferIdentifier(
                            identifier=shared.Identifier(
                                authority='TVPT',
                                value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                            ),
                            id='offer_1',
                            offer_ref='offer_1',
                        ),
                    ],
                    taxes=shared.Taxes(
                        at_type='TaxesDetail',
                        tax_info=[
                            shared.TaxInfo(
                                amount=2635.47,
                                currency_code=shared.CurrencyCode(
                                    code_authority='ISO 4217',
                                    decimal_authority='ISO 4217',
                                    decimal_place=4,
                                    value='USD',
                                ),
                                tax_breakdown=[
                                    shared.TaxBreakdown(
                                        airport_code='MIA',
                                        currency_code=shared.CurrencyCode(
                                            code_authority='ISO 4217',
                                            decimal_authority='ISO 4217',
                                            decimal_place=4,
                                            value='USD',
                                        ),
                                    ),
                                ],
                                tax_code='XF',
                            ),
                        ],
                        total_taxes=330.1,
                    ),
                    traveler_identifier_ref=[
                        shared.TravelerIdentifierRef(
                            passenger_type_code='ADT',
                            uris=[
                                'google.com',
                            ],
                        ),
                    ],
                ),
            ],
            preference=shared.Preference(
                at_type='Preference',
                applies_to=shared.AppliesTo(
                    at_type='AppliesToOffer',
                ),
                traveler_identifier=shared.TravelerIdentifier(
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                ),
            ),
            primary_contact=[
                shared.PrimaryContact(
                    at_type='PrimaryContact',
                    email=shared.Email(
                        email_type='Work',
                        id='exampledomain@example.com',
                        preferred_format='text/html',
                        provisioned_ind=True,
                        valid_ind=True,
                        value='exampledomain@example.com',
                    ),
                    telephone=shared.Telephone(
                        at_type='Telephone',
                        area_city_code='972',
                        city_code='DEN',
                        country_access_code='1',
                        extension='234',
                        id='3',
                        phone_number='972-000-787',
                        role=shared.EnumTelephoneRole.MOBILE,
                    ),
                    traveler_identifier=shared.TravelerIdentifier(
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                    ),
                    contact_information_refused_ind=True,
                    share_with_supplier=[
                        'string',
                    ],
                ),
            ],
            receipt=[
                shared.Receipt(
                    at_type='ReceiptConfirmation',
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    offer_ref=[
                        'string',
                    ],
                    receipt_ref='6773 2389 2239 2832',
                    id='3493289238',
                ),
            ],
            reservation_comment=[
                shared.ReservationComment(
                    at_type='ReservationComment',
                    applies_to=[
                        shared.AppliesTo(
                            at_type='AppliesToOffer',
                        ),
                    ],
                    comment=[
                        shared.Comment(
                            id='comment_1',
                            language='EN',
                            name='Comment name',
                            value='Additional comments',
                        ),
                    ],
                    share_with_supplier=[
                        'string',
                    ],
                ),
            ],
            reservation_display_sequence=shared.ReservationDisplaySequence(
                display_sequence=[
                    shared.DisplaySequence(
                        offer_ref='string',
                        sequence=1,
                        display_sequence='1',
                    ),
                ],
            ),
            shopping_cart=shared.ShoppingCart(
                product=[
                    shared.ProductAir(
                        at_type='ProductAir',
                        flight_segment=[
                            shared.FlightSegment(
                                at_type='FlightSegment',
                                co2_actual=shared.Measurement(
                                    value=2.22,
                                ),
                                flight=shared.FlightID(
                                    at_type='FlightDetail',
                                    flight_ref='pln0845',
                                    identifier=shared.Identifier(
                                        authority='TVPT',
                                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                                    ),
                                    id='126',
                                ),
                                operational_status=shared.OperationalStatusENUM(
                                    value=shared.OperationalStatusENUMBase.FLIGHT_BOARDING,
                                ),
                                bound_flights_ind=True,
                                connection_duration='60',
                                id='2304',
                                sequence=65,
                            ),
                        ],
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        passenger_flight=[
                            shared.PassengerFlight(
                                at_type='PassengerFlight',
                                flight_product=[
                                    shared.FlightProduct(
                                        at_type='FlightProduct',
                                        brand=shared.BrandID(
                                            at_type='BrandID',
                                            identifier=shared.Identifier(
                                                authority='TVPT',
                                                value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                                            ),
                                        ),
                                        class_of_service_availability=[
                                            shared.ClassOfServiceAvailability(
                                                number=2,
                                                value='F',
                                            ),
                                        ],
                                        customer_loyalty_credit=[
                                            shared.CustomerLoyaltyCredit(
                                                at_type='CustomerLoyaltyCredit',
                                                customer_loyalty=shared.CustomerLoyalty(
                                                    card_holder_name='John Smith',
                                                    id='Loyalty_1',
                                                    priority=2,
                                                    program_id='United',
                                                    program_name='Mileage Plus',
                                                    share_with_supplier=[
                                                        'LH NH SQ',
                                                    ],
                                                    supplier='UA',
                                                    supplier_type='Airline',
                                                    tier='Silver',
                                                    validated_ind=True,
                                                    value='132456',
                                                ),
                                                earned='500',
                                                status='gold',
                                            ),
                                        ],
                                        fare_qualifier=shared.FareQualifierENUM(),
                                        cabin=shared.CabinAirEnum.ECONOMY,
                                        car_code='P1234',
                                        class_of_service='F',
                                        fare_basis_code='HKG  SU  X/MOW  SU  KGD  598.78',
                                        fare_type_code='ERU',
                                        segment_sequence=[
                                            23,
                                            45,
                                            67,
                                            89,
                                        ],
                                        ticket_designator='BB5662Y',
                                        value_code='365',
                                    ),
                                ],
                                passenger_quantity=416,
                                passenger_type_code='ADT',
                            ),
                        ],
                        quantity=2,
                        id='product_1',
                        product_ref='product_1',
                        total_duration='3245',
                    ),
                ],
            ),
            special_service=[
                shared.SpecialService(
                    at_type='SpecialService',
                    applies_to=shared.AppliesTo(
                        at_type='AppliesToOffer',
                    ),
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    status=shared.Status(
                        supplier_text='Active/In-active',
                    ),
                    traveler_identifier=shared.TravelerIdentifier(
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                    ),
                ),
            ],
            travel_agency=shared.TravelAgency(
                at_type='TravelAgencyDetail',
                corporate_code='Air Agency',
                identifier=shared.Identifier(
                    authority='TVPT',
                    value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                ),
                organization_name=shared.CompanyName(
                    code='AI',
                    code_context='ISO',
                    department='Adventure department',
                    division='Travel Division',
                    id='2',
                    short_name='Aventure Inc',
                    system_of_record=[
                        '["1G","1V","MB","HZ"]',
                    ],
                ),
                profile_name=[
                    'string',
                ],
                travel_organization_ref='TravelAgency_1',
                id='2',
            ),
            traveler=[
                shared.Traveler(
                    at_type='TravelerDetail',
                    address=[
                        shared.Address(
                            at_type='AddressDetail',
                            address_line=[
                                'S',
                                ' ',
                                'H',
                                'a',
                                'v',
                                'a',
                                'n',
                                'a',
                                ',',
                                'O',
                                'p',
                                'p',
                                'o',
                                's',
                                'i',
                                't',
                                'e',
                                ' ',
                                't',
                                'o',
                                ' ',
                                'U',
                                'S',
                                'P',
                                'S',
                            ],
                            bldg_room=shared.AddressBldgRoom(
                                bulding_ind=True,
                                value='Moore House, Room 101, 23 ABC Street, Windsor, Berkshire, United Kingdom, SL6 51A',
                            ),
                            city='Windsor',
                            country=shared.Country(
                                code_context='IATA',
                                id='23',
                                name='United States',
                                value='USA',
                            ),
                            county='Berkshire',
                            number=shared.AddressStreetNumber(
                                po_box='1001',
                                rural_route_nmbr='76',
                                street_direction='NW',
                                street_nmbr_suffix='B',
                                value='23B ABC Street, Windsor, Berkshire, United Kingdom, SL6 51A',
                            ),
                            postal_code='Sl6 1AB',
                            state_prov=shared.StateProv(
                                name='California',
                                value='CA',
                            ),
                            street='ABC Street',
                            id='Address_1',
                            role=shared.EnumAddressRole.DELIVERY,
                        ),
                    ],
                    alternate_contact=[
                        shared.AlternateContact(
                            at_type='AlternateContact',
                            address=[
                                shared.Address(
                                    at_type='AddressDetail',
                                    address_line=[
                                        'S',
                                        ' ',
                                        'H',
                                        'a',
                                        'v',
                                        'a',
                                        'n',
                                        'a',
                                        ',',
                                        'O',
                                        'p',
                                        'p',
                                        'o',
                                        's',
                                        'i',
                                        't',
                                        'e',
                                        ' ',
                                        't',
                                        'o',
                                        ' ',
                                        'U',
                                        'S',
                                        'P',
                                        'S',
                                    ],
                                    bldg_room=shared.AddressBldgRoom(
                                        bulding_ind=True,
                                        value='Moore House, Room 101, 23 ABC Street, Windsor, Berkshire, United Kingdom, SL6 51A',
                                    ),
                                    city='Windsor',
                                    country=shared.Country(
                                        code_context='IATA',
                                        id='23',
                                        name='United States',
                                        value='USA',
                                    ),
                                    county='Berkshire',
                                    number=shared.AddressStreetNumber(
                                        po_box='1001',
                                        rural_route_nmbr='76',
                                        street_direction='NW',
                                        street_nmbr_suffix='B',
                                        value='23B ABC Street, Windsor, Berkshire, United Kingdom, SL6 51A',
                                    ),
                                    postal_code='Sl6 1AB',
                                    state_prov=shared.StateProv(
                                        name='California',
                                        value='CA',
                                    ),
                                    street='ABC Street',
                                    id='Address_1',
                                    role=shared.EnumAddressRole.DELIVERY,
                                ),
                            ],
                            email=[
                                shared.Email(
                                    email_type='Work',
                                    id='exampledomain@example.com',
                                    preferred_format='text/html',
                                    provisioned_ind=True,
                                    valid_ind=True,
                                    value='exampledomain@example.com',
                                ),
                            ],
                            person_name=shared.PersonName(
                                at_type='PersonNameDetail',
                                given='John',
                                middle='Erick',
                                prefix='Mr',
                                surname='Smith',
                            ),
                            telephone=[
                                shared.Telephone(
                                    at_type='Telephone',
                                    area_city_code='972',
                                    city_code='DEN',
                                    country_access_code='1',
                                    extension='234',
                                    id='3',
                                    phone_number='972-000-787',
                                    role=shared.EnumTelephoneRole.MOBILE,
                                ),
                            ],
                            contact_type='Relative',
                            default_ind=True,
                            emergency_ind=True,
                            relation='Mother',
                        ),
                    ],
                    comments=shared.Comments(
                        comment=[
                            shared.Comment(
                                id='comment_1',
                                language='EN',
                                name='Comment name',
                                value='Additional comments',
                            ),
                            shared.Comment(
                                id='comment_1',
                                language='EN',
                                name='Comment name',
                                value='Additional comments',
                            ),
                        ],
                    ),
                    customer_loyalty=[
                        shared.CustomerLoyalty(
                            card_holder_name='John Smith',
                            id='Loyalty_1',
                            priority=2,
                            program_id='United',
                            program_name='Mileage Plus',
                            share_with_supplier=[
                                'LH NH SQ',
                            ],
                            supplier='UA',
                            supplier_type='Airline',
                            tier='Silver',
                            validated_ind=True,
                            value='132456',
                        ),
                    ],
                    email=[
                        shared.Email(
                            email_type='Work',
                            id='exampledomain@example.com',
                            preferred_format='text/html',
                            provisioned_ind=True,
                            valid_ind=True,
                            value='exampledomain@example.com',
                        ),
                    ],
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    person_name=shared.PersonName(
                        at_type='PersonNameDetail',
                        given='John',
                        middle='Erick',
                        prefix='Mr',
                        surname='Smith',
                    ),
                    rail_discount_card=[
                        shared.RailDiscountCard(
                            reference_number='134256',
                            supplier_code='Enco',
                            value='20 Perecnt',
                        ),
                    ],
                    telephone=[
                        shared.Telephone(
                            at_type='Telephone',
                            area_city_code='972',
                            city_code='DEN',
                            country_access_code='1',
                            extension='234',
                            id='3',
                            phone_number='972-000-787',
                            role=shared.EnumTelephoneRole.MOBILE,
                        ),
                    ],
                    travel_document=[
                        shared.TravelDocument(
                            at_type='TravelDocumentDetail',
                            gender=shared.GenderEnum.UNDISCLOSED,
                            nationality='BR',
                            person_name=shared.PersonName(
                                at_type='PersonNameDetail',
                                given='John',
                                middle='Erick',
                                prefix='Mr',
                                surname='Smith',
                            ),
                            birth_country='AR',
                            birth_date=dateutil.parser.parse('1995-04-22').date(),
                            birth_place='Ontario',
                            doc_number='B37201',
                            doc_type=shared.DocTypeCodeEnum.PASSPORT,
                            expire_date=dateutil.parser.parse('2002-11-13').date(),
                            id='34',
                            issue_country='CA',
                            issue_date=dateutil.parser.parse('2002-10-13').date(),
                            place_of_issue='Birmingham',
                            residence='1st section 8th st',
                            state_prov_code='44',
                        ),
                    ],
                    accompanied_by_infant_ind=True,
                    birth_date=dateutil.parser.parse('2021-06-05').date(),
                    nationality='AL',
                    passenger_type_code='CHD',
                ),
            ],
            traveler_product=[
                shared.TravelerProduct(
                    at_type='TravelerProduct',
                ),
            ],
            id='REF12873',
        ),
    ),
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
| errors.SDKError         | 400-600                 | */*                     |

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
    identifier='string',
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
| errors.SDKError         | 400-600                 | */*                     |

## update_hotel_reservation

The Modify Reservation request can modify an existing reservation by changing any of the following - dates, payment information, traveler first and/or last name. You can also add comments to an existing reservation. Hotel Modify can be used only for Travelport itineraries at this time. When changing dates Travelport recommends that you first send an availability request for the new dates and look for the same booking code that is on the existing reservation. An availability request is not mandatory, but a modify request will fail if the new dates are not available.

### Example Usage

```python
import akaris_backend
import dateutil.parser
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.UpdateHotelReservationRequest(
    identifier='string',
    reservation_detail_wrapper=shared.ReservationDetailWrapper(
        reservation_detail=shared.ReservationDetail(
            at_type='Reservation',
            accounting=shared.Accounting(
                at_type='Accounting',
                identifier=shared.Identifier(
                    authority='TVPT',
                    value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                ),
                name_value_pair=[
                    shared.NameValuePair(
                        id='6',
                        name='Day1',
                        value='Sunday',
                    ),
                ],
                data_type='DateTime',
                template='Internal Finance template',
            ),
            agency_service_fee=[
                shared.AgencyServiceFee(
                    at_type='AgencyServiceFee',
                    amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        minor_unit=2,
                        value=124.56,
                    ),
                    description='Flight reservation service fee',
                    related_document_number=shared.DocumentNumber(
                        document_issuer='BA',
                        document_type=shared.DocumentTypeEnum.TICKET,
                        value='1259900123456',
                    ),
                    tax=[
                        shared.Tax(
                            code_authority='ISO',
                            currency_code='USD',
                            decimal_authority='ISO',
                            decimal_place=2,
                            description='Additional details.',
                            exempt_ind=True,
                            purpose='Fuel',
                            reporting_authority='JFK1',
                            tax_code='7702',
                            value=12.2,
                        ),
                    ],
                    id='AgencyServiceFee_1',
                ),
            ],
            document_overrides=[
                shared.DocumentOverrides(
                    at_type='DocumentOverrides',
                    change_fee_collection_method=shared.ChangeFeeCollectionMethod(
                        change_fee_issued_separately_ind=True,
                        code='f2142',
                        description='Change fee collection method',
                        sub_code='631b',
                        tax_included_in_base_amount_ind=True,
                        value=shared.ChangeFeeMethodEnum(
                            value=shared.ChangeFeeMethodEnumBase.EMD,
                        ),
                    ),
                    commissions=[
                        shared.Commissions(
                            apply_to=shared.CommissionApplyEnum.BASE,
                            commission=shared.Commission(
                                at_type='Commission',
                            ),
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                ),
                            ],
                        ),
                    ],
                    destination_purpose=[
                        shared.DestinationPurpose(
                            at_type='DestinationPurpose',
                            destination=shared.DestinationEnum.ASIA,
                            purpose=shared.PurposeEnum.BUSINESS,
                        ),
                    ],
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    net_remit_info=shared.NetRemitInfo(
                        at_type='NetRemitInfo',
                        actual_selling_fare=100.5,
                        car_code='ACAR',
                        net_base_amount=shared.FiledAmount(
                            code_authority='Australian Dollar',
                            currency_code='USD',
                            decimal_authority='ISO 4217',
                            decimal_place=3,
                            value=43.3422,
                        ),
                        value_code='D1000',
                    ),
                    offer_identifier=shared.OfferIdentifier(
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        id='offer_1',
                        offer_ref='offer_1',
                    ),
                    product_identifier=shared.ProductIdentifier(
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        id='product_1',
                        product_ref='product_1',
                    ),
                    restrictions=[
                        shared.Restrictions(
                            document_type=shared.DocumentTypeEnum.TICKET,
                            restriction=[
                                'string',
                            ],
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                ),
                            ],
                        ),
                    ],
                    ticket_designators=[
                        shared.TicketDesignators(
                            at_type='string',
                            ticket_designator='string',
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                ),
                            ],
                        ),
                    ],
                    tour_codes=[
                        shared.TourCodes(
                            at_type='TourCodes',
                            tour_code=shared.TourCode(),
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            form_of_payment=[
                shared.FormOfPaymentID(
                    at_type='FormOfPaymentPaymentCard',
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                ),
            ],
            identifier=shared.Identifier(
                authority='TVPT',
                value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
            ),
            offer=[
                shared.Offer(
                    at_type='Offer',
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    price=shared.Price(
                        at_type='PriceDetail',
                        base=20.2,
                        currency_code=shared.CurrencyCode(
                            code_authority='ISO 4217',
                            decimal_authority='ISO 4217',
                            decimal_place=4,
                            value='USD',
                        ),
                        total_fees=201,
                        total_price=34,
                        total_taxes=34.4,
                        vendor_currency_total=shared.VendorCurrencyTotal(
                            base=120.2,
                            currency_code=shared.CurrencyCode(
                                code_authority='ISO 4217',
                                decimal_authority='ISO 4217',
                                decimal_place=4,
                                value='USD',
                            ),
                            fees=shared.Fees(
                                at_type='FeesDetail',
                                total_fees=111.11,
                            ),
                            taxes=shared.Taxes(
                                at_type='TaxesDetail',
                                tax_info=[
                                    shared.TaxInfo(
                                        amount=7022.39,
                                        currency_code=shared.CurrencyCode(
                                            code_authority='ISO 4217',
                                            decimal_authority='ISO 4217',
                                            decimal_place=4,
                                            value='USD',
                                        ),
                                        tax_breakdown=[
                                            shared.TaxBreakdown(
                                                airport_code='MIA',
                                                currency_code=shared.CurrencyCode(
                                                    code_authority='ISO 4217',
                                                    decimal_authority='ISO 4217',
                                                    decimal_place=4,
                                                    value='USD',
                                                ),
                                            ),
                                        ],
                                        tax_code='XF',
                                    ),
                                ],
                                total_taxes=330.1,
                            ),
                            total=30.13,
                            approximate_ind=True,
                        ),
                        id='2',
                    ),
                    product=[
                        shared.ProductID(
                            at_type='ProductAir',
                            identifier=shared.Identifier(
                                authority='TVPT',
                                value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                            ),
                            id='product_1',
                            product_ref='product_1',
                        ),
                    ],
                    terms_and_conditions_full=[
                        shared.TermsAndConditionsFull(
                            at_type='TermsAndConditionsFullAir',
                            customer_loyalty=[
                                shared.CustomerLoyalty(
                                    card_holder_name='John Smith',
                                    id='Loyalty_1',
                                    priority=2,
                                    program_id='United',
                                    program_name='Mileage Plus',
                                    share_with_supplier=[
                                        'LH NH SQ',
                                    ],
                                    supplier='UA',
                                    supplier_type='Airline',
                                    tier='Silver',
                                    validated_ind=True,
                                    value='132456',
                                ),
                            ],
                            identifier=shared.Identifier(
                                authority='TVPT',
                                value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                            ),
                            text_block=[
                                shared.TextBlock(
                                    at_type='TextBlockDetail',
                                    text_formatted=[
                                        shared.TextFormatted(
                                            language='English',
                                            value='Formatted text',
                                        ),
                                    ],
                                    id='2',
                                    title='Baggage Details',
                                ),
                            ],
                            id='TC_1',
                            terms_and_conditions_ref='TC_1',
                        ),
                    ],
                    id='offer_1',
                    offer_ref='offer_1',
                    parent_offer_ref='offer_1',
                    passive_offer_ind=True,
                ),
            ],
            offer_link=[
                shared.OfferLink(
                    at_type='OfferLink',
                    parent_offer=shared.ParentOffer(
                        at_type='ParentOffer',
                    ),
                ),
            ],
            organization_loyalty_program=[
                shared.OrganizationLoyaltyProgram(
                    at_type='OrganizationLoyaltyProgramID',
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    loyalty_identifier='LP029381',
                    supplier='Air canada',
                ),
            ],
            payment=[
                shared.Payment(
                    at_type='Payment',
                    agency_service_fee_identifier=[
                        shared.AgencyServiceFeeIdentifier(),
                    ],
                    amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        minor_unit=2,
                        value=124.56,
                    ),
                    base_amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        minor_unit=2,
                        value=124.56,
                    ),
                    extended_payment=shared.ExtendedPayment(
                        first_installment=100,
                        number_of_installments=6,
                        remaining_amount=50,
                    ),
                    fees=shared.Fees(
                        at_type='FeesDetail',
                        total_fees=111.11,
                    ),
                    form_of_payment_identifier=shared.FormOfPaymentIdentifier(
                        at_type='FormOfPaymentPaymentCash',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                    ),
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    offer_identifier=[
                        shared.OfferIdentifier(
                            identifier=shared.Identifier(
                                authority='TVPT',
                                value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                            ),
                            id='offer_1',
                            offer_ref='offer_1',
                        ),
                    ],
                    taxes=shared.Taxes(
                        at_type='TaxesDetail',
                        tax_info=[
                            shared.TaxInfo(
                                amount=5625.77,
                                currency_code=shared.CurrencyCode(
                                    code_authority='ISO 4217',
                                    decimal_authority='ISO 4217',
                                    decimal_place=4,
                                    value='USD',
                                ),
                                tax_breakdown=[
                                    shared.TaxBreakdown(
                                        airport_code='MIA',
                                        currency_code=shared.CurrencyCode(
                                            code_authority='ISO 4217',
                                            decimal_authority='ISO 4217',
                                            decimal_place=4,
                                            value='USD',
                                        ),
                                    ),
                                ],
                                tax_code='XF',
                            ),
                        ],
                        total_taxes=330.1,
                    ),
                    traveler_identifier_ref=[
                        shared.TravelerIdentifierRef(
                            passenger_type_code='ADT',
                            uris=[
                                'google.com',
                            ],
                        ),
                    ],
                ),
            ],
            preference=shared.Preference(
                at_type='Preference',
                applies_to=shared.AppliesTo(
                    at_type='AppliesToOffer',
                ),
                traveler_identifier=shared.TravelerIdentifier(
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                ),
            ),
            primary_contact=[
                shared.PrimaryContact(
                    at_type='PrimaryContact',
                    email=shared.Email(
                        email_type='Work',
                        id='exampledomain@example.com',
                        preferred_format='text/html',
                        provisioned_ind=True,
                        valid_ind=True,
                        value='exampledomain@example.com',
                    ),
                    telephone=shared.Telephone(
                        at_type='Telephone',
                        area_city_code='972',
                        city_code='DEN',
                        country_access_code='1',
                        extension='234',
                        id='3',
                        phone_number='972-000-787',
                        role=shared.EnumTelephoneRole.MOBILE,
                    ),
                    traveler_identifier=shared.TravelerIdentifier(
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                    ),
                    contact_information_refused_ind=True,
                    share_with_supplier=[
                        'string',
                    ],
                ),
            ],
            receipt=[
                shared.Receipt(
                    at_type='ReceiptConfirmation',
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    offer_ref=[
                        'string',
                    ],
                    receipt_ref='6773 2389 2239 2832',
                    id='3493289238',
                ),
            ],
            reservation_comment=[
                shared.ReservationComment(
                    at_type='ReservationComment',
                    applies_to=[
                        shared.AppliesTo(
                            at_type='AppliesToOffer',
                        ),
                    ],
                    comment=[
                        shared.Comment(
                            id='comment_1',
                            language='EN',
                            name='Comment name',
                            value='Additional comments',
                        ),
                    ],
                    share_with_supplier=[
                        'string',
                    ],
                ),
            ],
            reservation_display_sequence=shared.ReservationDisplaySequence(
                display_sequence=[
                    shared.DisplaySequence(
                        offer_ref='string',
                        sequence=1,
                        display_sequence='1',
                    ),
                ],
            ),
            shopping_cart=shared.ShoppingCart(
                product=[
                    shared.ProductAir(
                        at_type='ProductAir',
                        flight_segment=[
                            shared.FlightSegment(
                                at_type='FlightSegment',
                                co2_actual=shared.Measurement(
                                    value=2.22,
                                ),
                                flight=shared.FlightID(
                                    at_type='FlightDetail',
                                    flight_ref='pln0845',
                                    identifier=shared.Identifier(
                                        authority='TVPT',
                                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                                    ),
                                    id='126',
                                ),
                                operational_status=shared.OperationalStatusENUM(
                                    value=shared.OperationalStatusENUMBase.FLIGHT_BOARDING,
                                ),
                                bound_flights_ind=True,
                                connection_duration='60',
                                id='2304',
                                sequence=65,
                            ),
                        ],
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        passenger_flight=[
                            shared.PassengerFlight(
                                at_type='PassengerFlight',
                                flight_product=[
                                    shared.FlightProduct(
                                        at_type='FlightProduct',
                                        brand=shared.BrandID(
                                            at_type='BrandID',
                                            identifier=shared.Identifier(
                                                authority='TVPT',
                                                value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                                            ),
                                        ),
                                        class_of_service_availability=[
                                            shared.ClassOfServiceAvailability(
                                                number=2,
                                                value='F',
                                            ),
                                        ],
                                        customer_loyalty_credit=[
                                            shared.CustomerLoyaltyCredit(
                                                at_type='CustomerLoyaltyCredit',
                                                customer_loyalty=shared.CustomerLoyalty(
                                                    card_holder_name='John Smith',
                                                    id='Loyalty_1',
                                                    priority=2,
                                                    program_id='United',
                                                    program_name='Mileage Plus',
                                                    share_with_supplier=[
                                                        'LH NH SQ',
                                                    ],
                                                    supplier='UA',
                                                    supplier_type='Airline',
                                                    tier='Silver',
                                                    validated_ind=True,
                                                    value='132456',
                                                ),
                                                earned='500',
                                                status='gold',
                                            ),
                                        ],
                                        fare_qualifier=shared.FareQualifierENUM(),
                                        cabin=shared.CabinAirEnum.ECONOMY,
                                        car_code='P1234',
                                        class_of_service='F',
                                        fare_basis_code='HKG  SU  X/MOW  SU  KGD  598.78',
                                        fare_type_code='ERU',
                                        segment_sequence=[
                                            23,
                                            45,
                                            67,
                                            89,
                                        ],
                                        ticket_designator='BB5662Y',
                                        value_code='365',
                                    ),
                                ],
                                passenger_quantity=416,
                                passenger_type_code='ADT',
                            ),
                        ],
                        quantity=2,
                        id='product_1',
                        product_ref='product_1',
                        total_duration='3245',
                    ),
                ],
            ),
            special_service=[
                shared.SpecialService(
                    at_type='SpecialService',
                    applies_to=shared.AppliesTo(
                        at_type='AppliesToOffer',
                    ),
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    status=shared.Status(
                        supplier_text='Active/In-active',
                    ),
                    traveler_identifier=shared.TravelerIdentifier(
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                    ),
                ),
            ],
            travel_agency=shared.TravelAgency(
                at_type='TravelAgencyDetail',
                corporate_code='Air Agency',
                identifier=shared.Identifier(
                    authority='TVPT',
                    value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                ),
                organization_name=shared.CompanyName(
                    code='AI',
                    code_context='ISO',
                    department='Adventure department',
                    division='Travel Division',
                    id='2',
                    short_name='Aventure Inc',
                    system_of_record=[
                        '["1G","1V","MB","HZ"]',
                    ],
                ),
                profile_name=[
                    'string',
                ],
                travel_organization_ref='TravelAgency_1',
                id='2',
            ),
            traveler=[
                shared.Traveler(
                    at_type='TravelerDetail',
                    address=[
                        shared.Address(
                            at_type='AddressDetail',
                            address_line=[
                                'S',
                                ' ',
                                'H',
                                'a',
                                'v',
                                'a',
                                'n',
                                'a',
                                ',',
                                'O',
                                'p',
                                'p',
                                'o',
                                's',
                                'i',
                                't',
                                'e',
                                ' ',
                                't',
                                'o',
                                ' ',
                                'U',
                                'S',
                                'P',
                                'S',
                            ],
                            bldg_room=shared.AddressBldgRoom(
                                bulding_ind=True,
                                value='Moore House, Room 101, 23 ABC Street, Windsor, Berkshire, United Kingdom, SL6 51A',
                            ),
                            city='Windsor',
                            country=shared.Country(
                                code_context='IATA',
                                id='23',
                                name='United States',
                                value='USA',
                            ),
                            county='Berkshire',
                            number=shared.AddressStreetNumber(
                                po_box='1001',
                                rural_route_nmbr='76',
                                street_direction='NW',
                                street_nmbr_suffix='B',
                                value='23B ABC Street, Windsor, Berkshire, United Kingdom, SL6 51A',
                            ),
                            postal_code='Sl6 1AB',
                            state_prov=shared.StateProv(
                                name='California',
                                value='CA',
                            ),
                            street='ABC Street',
                            id='Address_1',
                            role=shared.EnumAddressRole.DELIVERY,
                        ),
                    ],
                    alternate_contact=[
                        shared.AlternateContact(
                            at_type='AlternateContact',
                            address=[
                                shared.Address(
                                    at_type='AddressDetail',
                                    address_line=[
                                        'S',
                                        ' ',
                                        'H',
                                        'a',
                                        'v',
                                        'a',
                                        'n',
                                        'a',
                                        ',',
                                        'O',
                                        'p',
                                        'p',
                                        'o',
                                        's',
                                        'i',
                                        't',
                                        'e',
                                        ' ',
                                        't',
                                        'o',
                                        ' ',
                                        'U',
                                        'S',
                                        'P',
                                        'S',
                                    ],
                                    bldg_room=shared.AddressBldgRoom(
                                        bulding_ind=True,
                                        value='Moore House, Room 101, 23 ABC Street, Windsor, Berkshire, United Kingdom, SL6 51A',
                                    ),
                                    city='Windsor',
                                    country=shared.Country(
                                        code_context='IATA',
                                        id='23',
                                        name='United States',
                                        value='USA',
                                    ),
                                    county='Berkshire',
                                    number=shared.AddressStreetNumber(
                                        po_box='1001',
                                        rural_route_nmbr='76',
                                        street_direction='NW',
                                        street_nmbr_suffix='B',
                                        value='23B ABC Street, Windsor, Berkshire, United Kingdom, SL6 51A',
                                    ),
                                    postal_code='Sl6 1AB',
                                    state_prov=shared.StateProv(
                                        name='California',
                                        value='CA',
                                    ),
                                    street='ABC Street',
                                    id='Address_1',
                                    role=shared.EnumAddressRole.DELIVERY,
                                ),
                            ],
                            email=[
                                shared.Email(
                                    email_type='Work',
                                    id='exampledomain@example.com',
                                    preferred_format='text/html',
                                    provisioned_ind=True,
                                    valid_ind=True,
                                    value='exampledomain@example.com',
                                ),
                            ],
                            person_name=shared.PersonName(
                                at_type='PersonNameDetail',
                                given='John',
                                middle='Erick',
                                prefix='Mr',
                                surname='Smith',
                            ),
                            telephone=[
                                shared.Telephone(
                                    at_type='Telephone',
                                    area_city_code='972',
                                    city_code='DEN',
                                    country_access_code='1',
                                    extension='234',
                                    id='3',
                                    phone_number='972-000-787',
                                    role=shared.EnumTelephoneRole.MOBILE,
                                ),
                            ],
                            contact_type='Relative',
                            default_ind=True,
                            emergency_ind=True,
                            relation='Mother',
                        ),
                    ],
                    comments=shared.Comments(
                        comment=[
                            shared.Comment(
                                id='comment_1',
                                language='EN',
                                name='Comment name',
                                value='Additional comments',
                            ),
                            shared.Comment(
                                id='comment_1',
                                language='EN',
                                name='Comment name',
                                value='Additional comments',
                            ),
                        ],
                    ),
                    customer_loyalty=[
                        shared.CustomerLoyalty(
                            card_holder_name='John Smith',
                            id='Loyalty_1',
                            priority=2,
                            program_id='United',
                            program_name='Mileage Plus',
                            share_with_supplier=[
                                'LH NH SQ',
                            ],
                            supplier='UA',
                            supplier_type='Airline',
                            tier='Silver',
                            validated_ind=True,
                            value='132456',
                        ),
                    ],
                    email=[
                        shared.Email(
                            email_type='Work',
                            id='exampledomain@example.com',
                            preferred_format='text/html',
                            provisioned_ind=True,
                            valid_ind=True,
                            value='exampledomain@example.com',
                        ),
                    ],
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    person_name=shared.PersonName(
                        at_type='PersonNameDetail',
                        given='John',
                        middle='Erick',
                        prefix='Mr',
                        surname='Smith',
                    ),
                    rail_discount_card=[
                        shared.RailDiscountCard(
                            reference_number='134256',
                            supplier_code='Enco',
                            value='20 Perecnt',
                        ),
                    ],
                    telephone=[
                        shared.Telephone(
                            at_type='Telephone',
                            area_city_code='972',
                            city_code='DEN',
                            country_access_code='1',
                            extension='234',
                            id='3',
                            phone_number='972-000-787',
                            role=shared.EnumTelephoneRole.MOBILE,
                        ),
                    ],
                    travel_document=[
                        shared.TravelDocument(
                            at_type='TravelDocumentDetail',
                            gender=shared.GenderEnum.UNKNOWN,
                            nationality='BR',
                            person_name=shared.PersonName(
                                at_type='PersonNameDetail',
                                given='John',
                                middle='Erick',
                                prefix='Mr',
                                surname='Smith',
                            ),
                            birth_country='AR',
                            birth_date=dateutil.parser.parse('1995-04-22').date(),
                            birth_place='Ontario',
                            doc_number='B37201',
                            doc_type=shared.DocTypeCodeEnum.PASSPORT,
                            expire_date=dateutil.parser.parse('2002-11-13').date(),
                            id='34',
                            issue_country='CA',
                            issue_date=dateutil.parser.parse('2002-10-13').date(),
                            place_of_issue='Birmingham',
                            residence='1st section 8th st',
                            state_prov_code='44',
                        ),
                    ],
                    accompanied_by_infant_ind=True,
                    birth_date=dateutil.parser.parse('2021-06-05').date(),
                    nationality='AL',
                    passenger_type_code='CHD',
                ),
            ],
            traveler_product=[
                shared.TravelerProduct(
                    at_type='TravelerProduct',
                ),
            ],
            id='REF12873',
        ),
    ),
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
| errors.SDKError         | 400-600                 | */*                     |
