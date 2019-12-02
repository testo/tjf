# tjf - Testo JSON format
This repository contains the schema definitions of the Testo JSON format.

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