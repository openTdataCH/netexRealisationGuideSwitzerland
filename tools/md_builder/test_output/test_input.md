# test_input

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | StopPlace | ignored | 1..1 | unknown |  |  |
| <> | [Centroid](Centroid.md) | expected | 1..1 | unknown |  |  |
| > | Name | mandatory | 1..1 | unknown | The name of the StopPlace | The name of the StopPlace |
| > | PrivateCode | mandatory | 1..1 | unknown | DiDok number | DiDok number |
| > | Quays | expected | 1..1 | unknown |  |  |
| <>> | [Quay](QuayDetail.md) | expected | 1..1 | unknown |  |  |
