# Restaurant


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           | Example                                               |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `at_type`                                             | *Optional[str]*                                       | :heavy_minus_sign:                                    | N/A                                                   | Restaurant                                            |
| `distance`                                            | [Optional[Distance]](../../models/shared/distance.md) | :heavy_minus_sign:                                    | A search radius                                       |                                                       |
| `cuisine_codes`                                       | list[*str*]                                           | :heavy_minus_sign:                                    | An OTA code to define the cuisine type                | 12                                                    |
| `name`                                                | *str*                                                 | :heavy_check_mark:                                    | The name of the restaurant                            |                                                       |
| `proximity_code`                                      | *Optional[str]*                                       | :heavy_minus_sign:                                    | An OTA proximity code                                 |                                                       |