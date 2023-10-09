# GeoLocation

Used to specify the geographic coordinates of a location


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `altitude`                                                                               | *Optional[float]*                                                                        | :heavy_minus_sign:                                                                       | The height or an item, typically measured above sea level                                | 5280                                                                                     |
| `altitude_unit_of_distance`                                                              | [Optional[shared.UnitOfDistanceEnum]](undefined/models/shared/unitofdistanceenum.md)     | :heavy_minus_sign:                                                                       | Miles, Kilometers, etc.                                                                  |                                                                                          |
| `format_url`                                                                             | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | The URL to the format for the latitude and longitude for this location.                  | www.destinationmap.com                                                                   |
| `latitude`                                                                               | *Optional[float]*                                                                        | :heavy_check_mark:                                                                       | The measure of the angular distance on a meridan north or south equator                  | 38.8951                                                                                  |
| `longitude`                                                                              | *Optional[float]*                                                                        | :heavy_check_mark:                                                                       | The measure of the angular distance on a meridan east or west equator                    | -77.0364                                                                                 |
| `map_url`                                                                                | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | link for embedded map showing location                                                   | www.destinationmap.com                                                                   |
| `position_accuracy`                                                                      | [Optional[shared.PositionAccuracyEnum]](undefined/models/shared/positionaccuracyenum.md) | :heavy_minus_sign:                                                                       | Specifies the level of accuracy for the position                                         |                                                                                          |