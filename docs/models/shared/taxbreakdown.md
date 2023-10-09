# TaxBreakdown


## Fields

| Field                                                                                                                 | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           | Example                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `airport_code`                                                                                                        | *Optional[str]*                                                                                                       | :heavy_check_mark:                                                                                                    | The airport location the tax applies to                                                                               | MIA                                                                                                                   |
| `amount`                                                                                                              | *Optional[float]*                                                                                                     | :heavy_minus_sign:                                                                                                    | The amount of the tax applied                                                                                         |                                                                                                                       |
| `currency_code`                                                                                                       | [Optional[shared.CurrencyCode]](undefined/models/shared/currencycode.md)                                              | :heavy_minus_sign:                                                                                                    | Currency codes are the three-letter alphabetic codes that represent the various currencies used throughout the world. |                                                                                                                       |