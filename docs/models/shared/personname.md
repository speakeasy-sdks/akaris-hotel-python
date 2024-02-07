# PersonName


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `at_type`                                                | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      | PersonNameDetail                                         |
| `surname`                                                | *str*                                                    | :heavy_check_mark:                                       | Family name, last name.                                  | Smith                                                    |
| `given`                                                  | *Optional[str]*                                          | :heavy_minus_sign:                                       | Given name, first name or names.                         | John                                                     |
| `middle`                                                 | *Optional[str]*                                          | :heavy_minus_sign:                                       | The middle name of the person name.                      | Erick                                                    |
| `prefix`                                                 | *Optional[str]*                                          | :heavy_minus_sign:                                       | Salutation of honorific (e.g. Mr., Mrs., Ms., Miss, Dr.) | Mr                                                       |