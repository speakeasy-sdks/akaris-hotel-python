# BuildFromCatalogOfferingsRequest


## Fields

| Field                                                                                                                                                      | Type                                                                                                                                                       | Required                                                                                                                                                   | Description                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `offer_query_build_from_catalog_offerings_hospitality_wrapper`                                                                                             | [Optional[shared.OfferQueryBuildFromCatalogOfferingsHospitalityWrapper]](undefined/models/shared/offerquerybuildfromcatalogofferingshospitalitywrapper.md) | :heavy_check_mark:                                                                                                                                         | N/A                                                                                                                                                        |
| `trace_id`                                                                                                                                                 | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | Identifier used to correlate API invocations across long-running or multi-call business flows.                                                             |
| `travelport_plus_session_id`                                                                                                                               | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | Travelport Plus Session ID used to maintain an established agency session                                                                                  |
| `xauth_travelport_accessgroup`                                                                                                                             | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | Identifies the Travelport access group with which the caller is associated                                                                                 |