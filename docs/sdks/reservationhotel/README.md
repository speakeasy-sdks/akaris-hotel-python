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
        o_auth2="",
    ),
)

req = operations.BuildHotelReservationRequest(
    reservation_query_build_wrapper=shared.ReservationQueryBuildWrapper(
        reservation_query_build=shared.ReservationQueryBuild(
            at_type='Northwest',
            reservation_build=shared.ReservationBuild(
                at_type='ReservationBuildFromCatalogOfferings',
                accounting=shared.AccountingID(
                    at_type='Accounting',
                    accounting_ref='behalf male',
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    id='<ID>',
                ),
                document_overrides=[
                    shared.DocumentOverridesID(
                        at_type='DocumentOverrides',
                        document_overrides_ref='hideous which',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        id='<ID>',
                    ),
                ],
                form_of_payment=[
                    shared.FormOfPaymentID(
                        at_type='FormOfPaymentPaymentCard',
                        form_of_payment_ref='Gender',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        id='<ID>',
                    ),
                ],
                payment=[
                    shared.PaymentID(
                        at_type='Payment',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        payment_ref='Usability Copper digital',
                        id='<ID>',
                    ),
                ],
                preference=[
                    shared.PreferenceID(
                        at_type='Preference',
                        id='<ID>',
                    ),
                ],
                primary_contact=[
                    shared.PrimaryContactID(
                        at_type='PrimaryContact',
                        id='<ID>',
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
                        'Paradigm',
                    ],
                    product_ref='monetize',
                    receipt_ref='6773 2389 2239 2832',
                    segment_sequence_list=[
                        759187,
                    ],
                    date_time=dateutil.parser.isoparse('2021-06-18T16:01:27.959Z'),
                    id='3493289238',
                ),
                reservation_comment=[
                    shared.ReservationCommentID(
                        at_type='ReservationComment',
                        id='<ID>',
                    ),
                ],
                special_service=[
                    shared.SpecialServiceID(
                        at_type='SpecialService',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        id='<ID>',
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
                        value='flip',
                    ),
                    profile_name=[
                        'Cotton',
                    ],
                    travel_organization_ref='TravelAgency_1',
                    id='2',
                    organization_type=shared.OrganizationTypeEnum.ID_DOCUMENT_ISSUER,
                ),
                traveler=[
                    shared.TravelerID(
                        at_type='TravelerDetail',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        traveler_ref='aboard',
                        id='<ID>',
                    ),
                ],
            ),
        ),
    ),
    trace_id='South navigate',
    xauth_travelport_accessgroup='facilis Account',
)

res = s.reservation_hotel.build_hotel_reservation(req)

if res.reservation_response_wrapper is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.BuildHotelReservationRequest](../../models/operations/buildhotelreservationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.BuildHotelReservationResponse](../../models/operations/buildhotelreservationresponse.md)**


## cancel_hotel_offer

Cancel an Offer by modifying the Reservation

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="",
    ),
)

req = operations.CancelHotelOfferRequest(
    trace_id='mature',
    xauth_travelport_accessgroup='Country male',
    offer_id='deposit virtual',
    reservation_identifier='JBOD',
    supplier_locator='Southwest',
)

res = s.reservation_hotel.cancel_hotel_offer(req)

if res.reservation_response_wrapper is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CancelHotelOfferRequest](../../models/operations/cancelhotelofferrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CancelHotelOfferResponse](../../models/operations/cancelhotelofferresponse.md)**


## create_hotel_reservation

Create a reservation on the core or with the vendor/provider.

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

req = operations.CreateHotelReservationRequest(
    reservation_detail_wrapper=shared.ReservationDetailWrapper(
        reservation_detail=shared.ReservationDetail(
            at_type='Reservation',
            accounting=shared.Accounting(
                at_type='Accounting',
                accounting_ref='Gorgeous',
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
                id='<ID>',
                template='Internal Finance template',
            ),
            agency_service_fee=[
                shared.AgencyServiceFee(
                    at_type='AgencyServiceFee',
                    amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        currency_source=shared.CurrencySourceEnum.REQUESTED,
                        minor_unit=2,
                        value=124.56,
                    ),
                    description='Flight reservation service fee',
                    expiry_date=dateutil.parser.isoparse('2021-04-23T03:29:10.557Z'),
                    offer_ref='Rubber orange',
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
                            included_in_base=shared.YesNoUnknownEnum.UNKNOWN,
                            purpose='Fuel',
                            reporting_authority='JFK1',
                            tax_code='7702',
                            value=12.2,
                        ),
                    ],
                    traveler_ref='Cadillac not Courts',
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
                            at_type='Mazda Car',
                            apply_to=shared.CommissionApplyEnum.BASE,
                            commission=shared.Commission(
                                at_type='Commission',
                                application=shared.CommissionEnum.FULL,
                            ),
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    description='Sharable 5th generation website',
                                    id='<ID>',
                                    name='Tactics Ann',
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                    value='besides',
                                ),
                            ],
                        ),
                    ],
                    destination_purpose=[
                        shared.DestinationPurpose(
                            at_type='DestinationPurpose',
                            destination=shared.DestinationEnum.MIDDLE_EAST_WESTERN_ASIA,
                            purpose=shared.PurposeEnum.BUSINESS,
                        ),
                    ],
                    document_overrides_ref='generate',
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
                            at_type='Corporate withdrawal Oshkosh',
                            document_type=shared.DocumentTypeEnum.TICKET,
                            restriction=[
                                'solidly',
                            ],
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    description='Enhanced national access',
                                    id='<ID>',
                                    name='deposit',
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                    value='Awesome Volkswagen',
                                ),
                            ],
                        ),
                    ],
                    ticket_designators=[
                        shared.TicketDesignators(
                            at_type='Intuitive',
                            ticket_designator='program carefully cyan',
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    description='Total 3rd generation portal',
                                    id='<ID>',
                                    name='online',
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                    value='Checking',
                                ),
                            ],
                        ),
                    ],
                    tour_codes=[
                        shared.TourCodes(
                            at_type='TourCodes',
                            tour_code=shared.TourCode(
                                tour_code_type=shared.TourCodeTypeEnum.INCLUSIVE_TOUR,
                                value='till Tennessee parsing',
                            ),
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    description='Streamlined secondary ability',
                                    id='<ID>',
                                    name='emulation Dynamic',
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                    value='Southeast Hattiesburg Ball',
                                ),
                            ],
                        ),
                    ],
                    id='<ID>',
                ),
            ],
            form_of_payment=[
                shared.FormOfPaymentID(
                    at_type='FormOfPaymentPaymentCard',
                    form_of_payment_ref='bypass Accounts Latin',
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    id='<ID>',
                ),
            ],
            group_name='payment',
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
                            at_type='Fresh Indiana THX',
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
                                        amount=7021.35,
                                        currency_code=shared.CurrencyCode(
                                            code_authority='ISO 4217',
                                            decimal_authority='ISO 4217',
                                            decimal_place=4,
                                            value='USD',
                                        ),
                                        tax_breakdown=[
                                            shared.TaxBreakdown(
                                                airport_code='MIA',
                                                amount=5274.96,
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
                            currency_source=shared.CurrencySourceEnum.CHARGED,
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
                            expiry_date=dateutil.parser.isoparse('2023-08-19T02:31:42.966Z'),
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
                                            text_format=shared.TextFormatEnum.PLAIN_TEXT,
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
                    offer_ref='Loaf Sausages',
                    parent_offer=shared.ParentOffer(
                        at_type='ParentOffer',
                        offer_ref='Ohio',
                        product_ref='4th',
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
                    id='<ID>',
                ),
            ],
            payment=[
                shared.Payment(
                    at_type='Payment',
                    agency_service_fee_identifier=[
                        shared.AgencyServiceFeeIdentifier(
                            id='<ID>',
                        ),
                    ],
                    amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        currency_source=shared.CurrencySourceEnum.REQUESTED,
                        minor_unit=2,
                        value=124.56,
                    ),
                    base_amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        currency_source=shared.CurrencySourceEnum.REQUESTED,
                        minor_unit=2,
                        value=124.56,
                    ),
                    extended_payment=shared.ExtendedPayment(
                        first_installment=100,
                        number_of_installments=6,
                        otato_code='Borders',
                        remaining_amount=50,
                    ),
                    fees=shared.Fees(
                        at_type='FeesDetail',
                        total_fees=111.11,
                    ),
                    form_of_payment_identifier=shared.FormOfPaymentIdentifier(
                        at_type='FormOfPaymentPaymentCash',
                        form_of_payment_ref='Dynamic Salad Coupe',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        id='<ID>',
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
                    payment_ref='Soap',
                    taxes=shared.Taxes(
                        at_type='TaxesDetail',
                        tax_info=[
                            shared.TaxInfo(
                                amount=8668.43,
                                currency_code=shared.CurrencyCode(
                                    code_authority='ISO 4217',
                                    decimal_authority='ISO 4217',
                                    decimal_place=4,
                                    value='USD',
                                ),
                                tax_breakdown=[
                                    shared.TaxBreakdown(
                                        airport_code='MIA',
                                        amount=5376.38,
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
                            description='Profit-focused empowering secured line',
                            id='<ID>',
                            name='yogurt',
                            passenger_type_code='ADT',
                            uris=[
                                'google.com',
                            ],
                            value='after withdrawal',
                        ),
                    ],
                    deposit_ind=False,
                    guarantee_ind=False,
                    id='<ID>',
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
                    traveler_ref='USB',
                    id='<ID>',
                ),
                id='<ID>',
            ),
            primary_contact=[
                shared.PrimaryContact(
                    at_type='PrimaryContact',
                    email=shared.Email(
                        comment='The Apollotech B340 is an affordable wireless mouse with reliable connectivity, 12 months battery life and modern design',
                        email_type='Work',
                        id='exampledomain@example.com',
                        opt_in_date=dateutil.parser.isoparse('2023-01-07T21:36:36.012Z'),
                        opt_in_status=shared.OptInStatusEnum.OPTED_OUT,
                        opt_out_date=dateutil.parser.isoparse('2023-04-15T22:08:57.944Z'),
                        opt_out_ind=shared.YesNoInheritEnum.NO,
                        preferred_format='text/html',
                        provisioned_ind=True,
                        share_marketing=shared.YesNoInheritEnum.NO,
                        share_sync=shared.YesNoInheritEnum.NO,
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
                        traveler_ref='drat Refined',
                        id='<ID>',
                    ),
                    contact_information_refused_ind=True,
                    id='<ID>',
                    share_with=shared.ShareWithEnum.SUPPLIER,
                    share_with_supplier=[
                        'Kentucky',
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
                        'systems',
                    ],
                    product_ref='South copy Hilpert',
                    receipt_ref='6773 2389 2239 2832',
                    date_time=dateutil.parser.isoparse('2022-01-30T08:20:32.032Z'),
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
                    comment_source=shared.CommentSourceEnum.SUPPLIER,
                    id='<ID>',
                    share_with=shared.ShareWithEnum.AGENCY,
                    share_with_supplier=[
                        'Islands',
                    ],
                ),
            ],
            reservation_display_sequence=shared.ReservationDisplaySequence(
                at_type='Multigender in',
                display_sequence=[
                    shared.DisplaySequence(
                        at_type='copy',
                        offer_ref='Tasty',
                        product_ref='online Crew',
                        sequence=1,
                        display_sequence='1',
                    ),
                ],
                auto_delete_date_sequence=53061,
            ),
            shopping_cart=shared.ShoppingCart(
                at_type='Product Krone',
                product=[
                    shared.ProductAir(
                        at_type='ProductAir',
                        flight_segment=[
                            shared.FlightSegment(
                                at_type='FlightSegment',
                                co2_actual=shared.Measurement(
                                    measurement_type=shared.MeasurementTypeEnum.DEPTH,
                                    unit=shared.UnitOfMeasureEnum.GALLONS,
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
                                            brand_ref='whoa SUV',
                                            identifier=shared.Identifier(
                                                authority='TVPT',
                                                value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                                            ),
                                            id='<ID>',
                                        ),
                                        class_of_service_availability=[
                                            shared.ClassOfServiceAvailability(
                                                number=2,
                                                status=shared.AvailabilityStatusEnum.REMOVE_CLOSE_ONLY,
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
                                        fare_qualifier=shared.FareQualifierENUM(
                                            value=shared.FareQualifierENUMBase.VIST_FRIENDS_AND_RELATIVES,
                                        ),
                                        cabin=shared.CabinAirEnum.ECONOMY,
                                        car_code='P1234',
                                        class_of_service='F',
                                        fare_basis_code='HKG  SU  X/MOW  SU  KGD  598.78',
                                        fare_type=shared.FareTypeEnum.AIRLINE_PRIVATE_FARE,
                                        fare_type_code='ERU',
                                        segment_sequence=[
                                            939621,
                                        ],
                                        stopover_priced=shared.YesNoUnknownEnum.NO,
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
                    service_animal_type='Beauty male',
                    status=shared.Status(
                        supplier_text='Active/In-active',
                        value=shared.ConfirmationStatusEnum.CONFIRMED,
                    ),
                    traveler_identifier=shared.TravelerIdentifier(
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        traveler_ref='yowza Lubowitz',
                        id='<ID>',
                    ),
                    id='<ID>',
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
                    value='monitoring',
                ),
                profile_name=[
                    'Markets',
                ],
                travel_organization_ref='TravelAgency_1',
                id='2',
                organization_type=shared.OrganizationTypeEnum.REGULATORY,
            ),
            traveler=[
                shared.Traveler(
                    at_type='TravelerDetail',
                    address=[
                        shared.Address(
                            at_type='AddressDetail',
                            address_line=[
                                'emigrate',
                            ],
                            addressee='Consultant Account Frozen',
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
                                        'blue',
                                    ],
                                    addressee='reciprocal',
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
                                    comment='The slim & simple Maple Gaming Keyboard from Dev Byte comes with a sleek body and 7- Color RGB LED Back-lighting for smart functionality',
                                    email_type='Work',
                                    id='exampledomain@example.com',
                                    opt_in_date=dateutil.parser.isoparse('2022-08-15T09:41:37.589Z'),
                                    opt_in_status=shared.OptInStatusEnum.OPTED_IN,
                                    opt_out_date=dateutil.parser.isoparse('2021-12-06T22:12:55.985Z'),
                                    opt_out_ind=shared.YesNoInheritEnum.INHERIT,
                                    preferred_format='text/html',
                                    provisioned_ind=True,
                                    share_marketing=shared.YesNoInheritEnum.INHERIT,
                                    share_sync=shared.YesNoInheritEnum.NO,
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
                            id='<ID>',
                            relation='Mother',
                        ),
                    ],
                    comments=shared.Comments(
                        at_type='Loan',
                        comment=[
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
                            comment='The Football Is Good For Training And Recreational Purposes',
                            email_type='Work',
                            id='exampledomain@example.com',
                            opt_in_date=dateutil.parser.isoparse('2022-10-18T13:23:26.822Z'),
                            opt_in_status=shared.OptInStatusEnum.OPTED_IN,
                            opt_out_date=dateutil.parser.isoparse('2022-01-07T12:02:56.265Z'),
                            opt_out_ind=shared.YesNoInheritEnum.NO,
                            preferred_format='text/html',
                            provisioned_ind=True,
                            share_marketing=shared.YesNoInheritEnum.YES,
                            share_sync=shared.YesNoInheritEnum.NO,
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
                            gender=shared.GenderEnum.FEMALE,
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
                    traveler_ref='Tasty',
                    accompanied_by_infant_ind=True,
                    birth_date=dateutil.parser.parse('2021-06-05').date(),
                    gender=shared.GenderEnum.MALE,
                    id='<ID>',
                    nationality='AL',
                    passenger_type_code='CHD',
                ),
            ],
            traveler_product=[
                shared.TravelerProduct(
                    at_type='TravelerProduct',
                    confirmation_status_enum=shared.ConfirmationStatusEnum.PENDING,
                    offer_ref='female',
                    product_ref='generate Synchronised Bronze',
                    traveler_ref='Bicycle Unbranded bandwidth',
                    id='<ID>',
                ),
            ],
            auto_delete_date=dateutil.parser.parse('2022-05-23').date(),
            id='REF12873',
            notification_date=dateutil.parser.parse('2022-09-13').date(),
        ),
    ),
    trace_id='Sedan',
    xauth_travelport_accessgroup='lavender',
)

res = s.reservation_hotel.create_hotel_reservation(req)

if res.reservation_response_wrapper is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateHotelReservationRequest](../../models/operations/createhotelreservationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.CreateHotelReservationResponse](../../models/operations/createhotelreservationresponse.md)**


## retrieve_hotel_reservation

Retrieve details about a held booking, or PNR. While a PNR refers to a held booking that has not been ticketed, the PNR code persists after ticketing to provide the booking records. Once a PNR has been ticketed, you can still use PNR Retrieve to return both booking and ticketing details. A Ticket Display request can also be used to retrieve any ticketed itinerary.

### Example Usage

```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="",
    ),
)

req = operations.RetrieveHotelReservationRequest(
    identifier='Markets Folding',
    trace_id='off Music',
    xauth_travelport_accessgroup='alias Azusa Hop',
    detail_view_ind=False,
    identifier_type=shared.IdentifierTypeENUM.LOCATOR,
)

res = s.reservation_hotel.retrieve_hotel_reservation(req)

if res.reservation_response_wrapper is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RetrieveHotelReservationRequest](../../models/operations/retrievehotelreservationrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.RetrieveHotelReservationResponse](../../models/operations/retrievehotelreservationresponse.md)**


## update_hotel_reservation

The Modify Reservation request can modify an existing reservation by changing any of the following - dates, payment information, traveler first and/or last name. You can also add comments to an existing reservation. Hotel Modify can be used only for Travelport itineraries at this time. When changing dates Travelport recommends that you first send an availability request for the new dates and look for the same booking code that is on the existing reservation. An availability request is not mandatory, but a modify request will fail if the new dates are not available.

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

req = operations.UpdateHotelReservationRequest(
    identifier='repurpose blanditiis Hip',
    reservation_detail_wrapper=shared.ReservationDetailWrapper(
        reservation_detail=shared.ReservationDetail(
            at_type='Reservation',
            accounting=shared.Accounting(
                at_type='Accounting',
                accounting_ref='Loan',
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
                id='<ID>',
                template='Internal Finance template',
            ),
            agency_service_fee=[
                shared.AgencyServiceFee(
                    at_type='AgencyServiceFee',
                    amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        currency_source=shared.CurrencySourceEnum.SUPPLIER,
                        minor_unit=2,
                        value=124.56,
                    ),
                    description='Flight reservation service fee',
                    expiry_date=dateutil.parser.isoparse('2021-03-20T23:33:15.144Z'),
                    offer_ref='tarnish',
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
                            included_in_base=shared.YesNoUnknownEnum.YES,
                            purpose='Fuel',
                            reporting_authority='JFK1',
                            tax_code='7702',
                            value=12.2,
                        ),
                    ],
                    traveler_ref='jaded Arizona Classical',
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
                            at_type='attitude deposit Security',
                            apply_to=shared.CommissionApplyEnum.BASE,
                            commission=shared.Commission(
                                at_type='Commission',
                                application=shared.CommissionEnum.FULL,
                            ),
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    description='Multi-tiered fault-tolerant concept',
                                    id='<ID>',
                                    name='mobile',
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                    value='Program ASCII Honduras',
                                ),
                            ],
                        ),
                    ],
                    destination_purpose=[
                        shared.DestinationPurpose(
                            at_type='DestinationPurpose',
                            destination=shared.DestinationEnum.CANADA_AND_GREENLAND,
                            purpose=shared.PurposeEnum.PLEASURE,
                        ),
                    ],
                    document_overrides_ref='sunt',
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
                            at_type='with',
                            document_type=shared.DocumentTypeEnum.TICKET,
                            restriction=[
                                'Northwest',
                            ],
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    description='Cross-platform demand-driven success',
                                    id='<ID>',
                                    name='Kentucky Northwest Cadmium',
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                    value='Diesel Avon',
                                ),
                            ],
                        ),
                    ],
                    ticket_designators=[
                        shared.TicketDesignators(
                            at_type='Oriental Audi',
                            ticket_designator='visualize',
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    description='Exclusive leading edge support',
                                    id='<ID>',
                                    name='magnam Helium transmitter',
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                    value='generate methodical Koruna',
                                ),
                            ],
                        ),
                    ],
                    tour_codes=[
                        shared.TourCodes(
                            at_type='TourCodes',
                            tour_code=shared.TourCode(
                                tour_code_type=shared.TourCodeTypeEnum.INCLUSIVE_TOUR,
                                value='Valley Hydrogen architecture',
                            ),
                            traveler_identifier_ref=[
                                shared.TravelerIdentifierRef(
                                    description='Managed foreground project',
                                    id='<ID>',
                                    name='JSON',
                                    passenger_type_code='ADT',
                                    uris=[
                                        'google.com',
                                    ],
                                    value='Applications female',
                                ),
                            ],
                        ),
                    ],
                    id='<ID>',
                ),
            ],
            form_of_payment=[
                shared.FormOfPaymentID(
                    at_type='FormOfPaymentPaymentCard',
                    form_of_payment_ref='Chile morph',
                    identifier=shared.Identifier(
                        authority='TVPT',
                        value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                    ),
                    id='<ID>',
                ),
            ],
            group_name='Soap Liaison',
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
                            at_type='Granite phooey',
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
                                        amount=728.7,
                                        currency_code=shared.CurrencyCode(
                                            code_authority='ISO 4217',
                                            decimal_authority='ISO 4217',
                                            decimal_place=4,
                                            value='USD',
                                        ),
                                        tax_breakdown=[
                                            shared.TaxBreakdown(
                                                airport_code='MIA',
                                                amount=3175.91,
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
                            currency_source=shared.CurrencySourceEnum.REQUESTED,
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
                            expiry_date=dateutil.parser.isoparse('2021-04-18T06:49:26.190Z'),
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
                                            text_format=shared.TextFormatEnum.PLAIN_TEXT,
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
                    offer_ref='yowza',
                    parent_offer=shared.ParentOffer(
                        at_type='ParentOffer',
                        offer_ref='prioritise red',
                        product_ref='Gasoline District',
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
                    id='<ID>',
                ),
            ],
            payment=[
                shared.Payment(
                    at_type='Payment',
                    agency_service_fee_identifier=[
                        shared.AgencyServiceFeeIdentifier(
                            id='<ID>',
                        ),
                    ],
                    amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        currency_source=shared.CurrencySourceEnum.REQUESTED,
                        minor_unit=2,
                        value=124.56,
                    ),
                    base_amount=shared.CurrencyAmount(
                        approximate_ind=True,
                        code='USD',
                        currency_source=shared.CurrencySourceEnum.CHARGED,
                        minor_unit=2,
                        value=124.56,
                    ),
                    extended_payment=shared.ExtendedPayment(
                        first_installment=100,
                        number_of_installments=6,
                        otato_code='Southeast yet overriding',
                        remaining_amount=50,
                    ),
                    fees=shared.Fees(
                        at_type='FeesDetail',
                        total_fees=111.11,
                    ),
                    form_of_payment_identifier=shared.FormOfPaymentIdentifier(
                        at_type='FormOfPaymentPaymentCash',
                        form_of_payment_ref='Strategist Mouse',
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        id='<ID>',
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
                    payment_ref='Factors Southwest',
                    taxes=shared.Taxes(
                        at_type='TaxesDetail',
                        tax_info=[
                            shared.TaxInfo(
                                amount=9456.12,
                                currency_code=shared.CurrencyCode(
                                    code_authority='ISO 4217',
                                    decimal_authority='ISO 4217',
                                    decimal_place=4,
                                    value='USD',
                                ),
                                tax_breakdown=[
                                    shared.TaxBreakdown(
                                        airport_code='MIA',
                                        amount=8539.2,
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
                            description='Down-sized bi-directional software',
                            id='<ID>',
                            name='Senior Manager',
                            passenger_type_code='ADT',
                            uris=[
                                'google.com',
                            ],
                            value='online thoroughly',
                        ),
                    ],
                    deposit_ind=False,
                    guarantee_ind=False,
                    id='<ID>',
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
                    traveler_ref='Australian Realigned boldly',
                    id='<ID>',
                ),
                id='<ID>',
            ),
            primary_contact=[
                shared.PrimaryContact(
                    at_type='PrimaryContact',
                    email=shared.Email(
                        comment='Carbonite web goalkeeper gloves are ergonomically designed to give easy fit',
                        email_type='Work',
                        id='exampledomain@example.com',
                        opt_in_date=dateutil.parser.isoparse('2021-05-12T03:16:38.320Z'),
                        opt_in_status=shared.OptInStatusEnum.OPTED_IN,
                        opt_out_date=dateutil.parser.isoparse('2021-08-12T09:55:51.689Z'),
                        opt_out_ind=shared.YesNoInheritEnum.INHERIT,
                        preferred_format='text/html',
                        provisioned_ind=True,
                        share_marketing=shared.YesNoInheritEnum.NO,
                        share_sync=shared.YesNoInheritEnum.INHERIT,
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
                        traveler_ref='Implementation Electric',
                        id='<ID>',
                    ),
                    contact_information_refused_ind=True,
                    id='<ID>',
                    share_with=shared.ShareWithEnum.TRAVELER,
                    share_with_supplier=[
                        'SSD',
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
                        'UDP',
                    ],
                    product_ref='Indiana turquoise red',
                    receipt_ref='6773 2389 2239 2832',
                    date_time=dateutil.parser.isoparse('2023-02-28T12:27:59.089Z'),
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
                    comment_source=shared.CommentSourceEnum.AGENCY,
                    id='<ID>',
                    share_with=shared.ShareWithEnum.TRAVELER,
                    share_with_supplier=[
                        'Metal',
                    ],
                ),
            ],
            reservation_display_sequence=shared.ReservationDisplaySequence(
                at_type='Metal Gasoline oddly',
                display_sequence=[
                    shared.DisplaySequence(
                        at_type='Cadillac South Cuban',
                        offer_ref='reboot turquoise Tandem',
                        product_ref='Land person',
                        sequence=1,
                        display_sequence='1',
                    ),
                ],
                auto_delete_date_sequence=303317,
            ),
            shopping_cart=shared.ShoppingCart(
                at_type='Cadillac Awesome',
                product=[
                    shared.ProductAir(
                        at_type='ProductAir',
                        flight_segment=[
                            shared.FlightSegment(
                                at_type='FlightSegment',
                                co2_actual=shared.Measurement(
                                    measurement_type=shared.MeasurementTypeEnum.WIDTH,
                                    unit=shared.UnitOfMeasureEnum.KILOWATTS,
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
                                            brand_ref='indigo Sports',
                                            identifier=shared.Identifier(
                                                authority='TVPT',
                                                value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                                            ),
                                            id='<ID>',
                                        ),
                                        class_of_service_availability=[
                                            shared.ClassOfServiceAvailability(
                                                number=2,
                                                status=shared.AvailabilityStatusEnum.OTHER,
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
                                        fare_qualifier=shared.FareQualifierENUM(
                                            value=shared.FareQualifierENUMBase.CONSOLIDATOR,
                                        ),
                                        cabin=shared.CabinAirEnum.ECONOMY,
                                        car_code='P1234',
                                        class_of_service='F',
                                        fare_basis_code='HKG  SU  X/MOW  SU  KGD  598.78',
                                        fare_type=shared.FareTypeEnum.AGENCY_PRIVATE_FARE,
                                        fare_type_code='ERU',
                                        segment_sequence=[
                                            381389,
                                        ],
                                        stopover_priced=shared.YesNoUnknownEnum.NO,
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
                    service_animal_type='forecast',
                    status=shared.Status(
                        supplier_text='Active/In-active',
                        value=shared.ConfirmationStatusEnum.REJECTED,
                    ),
                    traveler_identifier=shared.TravelerIdentifier(
                        identifier=shared.Identifier(
                            authority='TVPT',
                            value='A0656EFF-FAF4-456F-B061-0161008D7C4E',
                        ),
                        traveler_ref='Assistant Jazz',
                        id='<ID>',
                    ),
                    id='<ID>',
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
                    value='azure Frozen',
                ),
                profile_name=[
                    'relationships',
                ],
                travel_organization_ref='TravelAgency_1',
                id='2',
                organization_type=shared.OrganizationTypeEnum.ID_DOCUMENT_ISSUER,
            ),
            traveler=[
                shared.Traveler(
                    at_type='TravelerDetail',
                    address=[
                        shared.Address(
                            at_type='AddressDetail',
                            address_line=[
                                'asymmetric',
                            ],
                            addressee='Hop',
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
                                        'immediately',
                                    ],
                                    addressee='Diesel Female',
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
                                    comment='The Nagasaki Lander is the trademarked name of several series of Nagasaki sport bikes, that started with the 1984 ABC800J',
                                    email_type='Work',
                                    id='exampledomain@example.com',
                                    opt_in_date=dateutil.parser.isoparse('2022-10-05T05:14:02.397Z'),
                                    opt_in_status=shared.OptInStatusEnum.UNKNOWN,
                                    opt_out_date=dateutil.parser.isoparse('2022-10-21T12:28:46.385Z'),
                                    opt_out_ind=shared.YesNoInheritEnum.NO,
                                    preferred_format='text/html',
                                    provisioned_ind=True,
                                    share_marketing=shared.YesNoInheritEnum.YES,
                                    share_sync=shared.YesNoInheritEnum.NO,
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
                            id='<ID>',
                            relation='Mother',
                        ),
                    ],
                    comments=shared.Comments(
                        at_type='FTM',
                        comment=[
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
                            comment='Andy shoes are designed to keeping in mind durability as well as trends, the most stylish range of shoes & sandals',
                            email_type='Work',
                            id='exampledomain@example.com',
                            opt_in_date=dateutil.parser.isoparse('2022-08-11T04:18:31.662Z'),
                            opt_in_status=shared.OptInStatusEnum.OPTED_IN,
                            opt_out_date=dateutil.parser.isoparse('2023-05-16T08:10:36.604Z'),
                            opt_out_ind=shared.YesNoInheritEnum.NO,
                            preferred_format='text/html',
                            provisioned_ind=True,
                            share_marketing=shared.YesNoInheritEnum.YES,
                            share_sync=shared.YesNoInheritEnum.NO,
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
                            gender=shared.GenderEnum.MALE,
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
                    traveler_ref='systems Tandem',
                    accompanied_by_infant_ind=True,
                    birth_date=dateutil.parser.parse('2021-06-05').date(),
                    gender=shared.GenderEnum.FEMALE,
                    id='<ID>',
                    nationality='AL',
                    passenger_type_code='CHD',
                ),
            ],
            traveler_product=[
                shared.TravelerProduct(
                    at_type='TravelerProduct',
                    confirmation_status_enum=shared.ConfirmationStatusEnum.CONFIRMED,
                    offer_ref='Northeast calculating',
                    product_ref='paradigms Smart',
                    traveler_ref='Trans Genderqueer',
                    id='<ID>',
                ),
            ],
            auto_delete_date=dateutil.parser.parse('2022-02-16').date(),
            id='REF12873',
            notification_date=dateutil.parser.parse('2021-04-03').date(),
        ),
    ),
    trace_id='Markets Florida',
    xauth_travelport_accessgroup='viral',
)

res = s.reservation_hotel.update_hotel_reservation(req)

if res.reservation_response_wrapper is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateHotelReservationRequest](../../models/operations/updatehotelreservationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.UpdateHotelReservationResponse](../../models/operations/updatehotelreservationresponse.md)**

