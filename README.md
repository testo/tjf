# tjf - Testo JSON format
This repository contains the schema definitions of the Testo JSON format (tjf).
The tjf is used for App to App (App2App) and the Device to Device (Dev2Dev) communication.

App2App is included into the following Apps:
| App      | Devices |
| --------- | -----|
| SmartProbes | t115i, t405i, t410i, t510i, t549i, t605i, t805i, t905i, t770-3 |
| testo 330i App | t330i |
| testo Combustion App Android | testo 320, testo 324,  testo 327-2, testo 330, testo 335, testo 340, testo 350 (since 2011) |
| testo Combustion App iOS | t330 |
| testo 420 App | t420 |
| testo Refrigeration | t550, t557 (generation since 2015) |

Dev2Dev is included into the following Apps / Devcies:
| App / Device     | Devices |
| --------- | -----|
| testo 300 | t300 |
| testo 330i App | t330i |

## Extended schema
The extended schema is designed to hold all possibly necessary data a measurement can contain.

### Changelog

#### 1.0.5 (07/2019)
- Added optional property "id" to the measurement type.
- Added optional property "id" to the measurement property type.
- xmlid, description are now marked optional

#### 1.0.4 (12/2017)
- Added property `errors`

#### 1.0.3 (10/2017)
Added optional properties `xmlid`
- `channelunit` : add optional property `xmlid`
  - an optional property `xmlid` has been added to `channelunit`
    which contains a mapping from the `channelunit` property `name` to XML ID Unit  
- `channeltype` : add optional property `xmlid`
  - an optional property `xmlid` has been added to `channeltype`
    which contains a mapping from the `channeltype` property `name` to XML ID Channel Name

#### 1.0.2
- the 'value' property of measurementvalue now allows null values, indicating an invalid value.


#### 1.0.1
- the definition of the channeltype has been changed in the following way:
  - an additional property 'description' has been added, which now contains the value from 'name' but (possibly) translated into the current application language
  - 'name' will now never be a translated string
- the documentation of properties of measurementvalue has been enhanced to reflect that in case the 'value' property contains an invalid value the 'description' property will contain a string like '----' or similar
- the 'value' property of measurementpropertyvalue can now be a number or a string 


#### 1.0.0
- initial version of the schema


## Slim schema
The slim schema is designed to hold a big amount of data, this means it omits a lot of meta data and redundant information.

### Changelog
#### v1.0.6
First publicly available version of the schema.