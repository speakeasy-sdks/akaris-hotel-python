# MeetingRoom


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `at_type`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  | MeetingRoom                                                          |
| `capacity`                                                           | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `codes`                                                              | list[*str*]                                                          | :heavy_minus_sign:                                                   | OTA code for this room type.                                         |                                                                      |
| `name`                                                               | *Optional[str]*                                                      | :heavy_check_mark:                                                   | The name of the meeting room                                         |                                                                      |
| `size`                                                               | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `unit_of_size`                                                       | [Optional[shared.UnitOfSize]](undefined/models/shared/unitofsize.md) | :heavy_minus_sign:                                                   | List of units of size i.e Square Feet, Square Meters                 |                                                                      |