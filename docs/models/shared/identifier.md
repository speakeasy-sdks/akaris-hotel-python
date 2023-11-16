# Identifier

Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `authority`                                             | *Optional[str]*                                         | :heavy_minus_sign:                                      | Name of the authoritative system that created this Guid | TVPT                                                    |
| `value`                                                 | *Optional[str]*                                         | :heavy_minus_sign:                                      | N/A                                                     | A0656EFF-FAF4-456F-B061-0161008D7C4E                    |