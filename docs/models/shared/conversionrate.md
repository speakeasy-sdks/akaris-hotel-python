# ConversionRate

A conversion metric from standard to another with the contextual authority such as IATA, OAG, ISO, etc.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `rate_as_of`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Rate as of                                                           |                                                                      |
| `rate_authority`                                                     | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Rate authority                                                       | ISO 4217                                                             |
| `value`                                                              | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |