# VehicleType

Used currently mainly for the relevant accessibility elements that can be expressed currently

*Table: VehicleType*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | ShortName | expected | 0..* | MultilingualString | Short Name for service | Will be defined in mapping excel |
|  | LowFloor | optional | 0..1 | xsd:boolean | Whether Vehicle is low floor to facilitate access by the mobility impaired. |  |
|  | HasLiftOrRamp | optional | 0..1 | xsd:boolean | Whether vehicle has lift or ramp to facilitate wheelchair access. |  |
|  | HasHoist | optional | 0..1 | xsd:boolean | Whether vehicle has hoist for wheelchair access. |  |
