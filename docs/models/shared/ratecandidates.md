# RateCandidates


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `at_type`                                                   | *str*                                                       | :heavy_check_mark:                                          | N/A                                                         | RateCandidates                                              |
| `rate_candidate`                                            | List[[RateCandidate](../../models/shared/ratecandidate.md)] | :heavy_check_mark:                                          | N/A                                                         |                                                             |
| `post_pay_rates_only_ind`                                   | *Optional[bool]*                                            | :heavy_minus_sign:                                          | If true, only postpay rates will be returned                |                                                             |
| `pre_pay_rates_only_ind`                                    | *Optional[bool]*                                            | :heavy_minus_sign:                                          | If true, only prepay rates will be returned                 |                                                             |