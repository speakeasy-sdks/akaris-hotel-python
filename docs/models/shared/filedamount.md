# FiledAmount

The base amount of a ticket price or net price that is filed in local currency


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `code_authority`                                     | *str*                                                | :heavy_check_mark:                                   | Filed amount currency code authority                 | Australian Dollar                                    |
| `currency_code`                                      | *Optional[str]*                                      | :heavy_minus_sign:                                   | Filed amount currency code                           | USD                                                  |
| `decimal_authority`                                  | *Optional[str]*                                      | :heavy_minus_sign:                                   | ISO 4217 standard decimal authority                  | ISO 4217                                             |
| `decimal_place`                                      | *int*                                                | :heavy_check_mark:                                   | ISO 4217 standard has a different number of decimals | 3                                                    |
| `value`                                              | *Optional[float]*                                    | :heavy_minus_sign:                                   | Filed amount value                                   | 43.3422                                              |