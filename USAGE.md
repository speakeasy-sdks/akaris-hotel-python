<!-- Start SDK Example Usage [usage] -->
```python
import akaris_backend
from akaris_backend.models import operations, shared

s = akaris_backend.AkarisBackend(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.CreateHotelAvailabilityRequest(
    catalog_offerings_query_request_hospitality_wrapper=shared.CatalogOfferingsQueryRequestHospitalityWrapper(),
)

res = s.hotel_availability.create_hotel_availability(req)

if res.catalog_offerings_hospitality_response_wrapper is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->