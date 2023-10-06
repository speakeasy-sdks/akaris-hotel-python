# Error


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `at_type`                                            | *Optional[str]*                                      | :heavy_check_mark:                                   | N/A                                                  | Error                                                |
| `message`                                            | *Optional[str]*                                      | :heavy_minus_sign:                                   | The Travelport standardized error or warning message |                                                      |
| `name_value_pair`                                    | list[*errors.NameValuePair*]                         | :heavy_minus_sign:                                   | N/A                                                  |                                                      |
| `status_code`                                        | *Optional[int]*                                      | :heavy_minus_sign:                                   | Http standard response code                          |                                                      |