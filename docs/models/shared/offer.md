# Offer


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                         | Example                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `at_type`                                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                  | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                 | Offer                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `identifier`                                                                                                                                                                                                                                                                                                                                                                                                                        | [Optional[shared.Identifier]](undefined/models/shared/identifier.md)                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                  | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `price`                                                                                                                                                                                                                                                                                                                                                                                                                             | [Optional[shared.Price]](undefined/models/shared/price.md)                                                                                                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                  | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `product`                                                                                                                                                                                                                                                                                                                                                                                                                           | list[[shared.ProductID](undefined/models/shared/productid.md)]                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                  | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `terms_and_conditions_full`                                                                                                                                                                                                                                                                                                                                                                                                         | list[[shared.TermsAndConditionsFull](undefined/models/shared/termsandconditionsfull.md)]                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                  | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `id`                                                                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                  | Local indentifier within a given message for this object.                                                                                                                                                                                                                                                                                                                                                                           | offer_1                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `offer_ref`                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                  | Used to reference another instance of this object in the same message                                                                                                                                                                                                                                                                                                                                                               | offer_1                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `parent_offer_ref`                                                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                  | A reference to the Offer this offer is sold in conjunction with                                                                                                                                                                                                                                                                                                                                                                     | offer_1                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `passive_offer_ind`                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                  | If true, the Offer is passive for booking purposes.                                                                                                                                                                                                                                                                                                                                                                                 | true                                                                                                                                                                                                                                                                                                                                                                                                                                |