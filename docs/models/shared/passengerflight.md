# PassengerFlight


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `at_type`                                                   | *Optional[str]*                                             | :heavy_minus_sign:                                          | N/A                                                         | PassengerFlight                                             |
| `flight_product`                                            | list[[FlightProduct](../../models/shared/flightproduct.md)] | :heavy_minus_sign:                                          | N/A                                                         |                                                             |
| `passenger_quantity`                                        | *Optional[int]*                                             | :heavy_minus_sign:                                          | Number of passengers of the specified passenger type code   | 416                                                         |
| `passenger_type_code`                                       | *Optional[str]*                                             | :heavy_minus_sign:                                          | Passenger type code                                         | ADT                                                         |