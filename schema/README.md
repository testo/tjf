# tjf - schema definitions

The schemas nested within folders are remnants of a legacy system, retained primarily for compatibility reasons. However, for the majority of users, these schemas serve little purpose in the modern context and can be safely disregarded.

## measurementCollection
The schema represents a structured collection of individual measurements like defined in [slim-schema](#slim-schema), each independent of the others. This collection is further enriched with some additional features, similar to those in slim-schema but only a small subset.

## slim-schema
The schema delineates a comprehensive data structure exported by Testo applications. It encompasses various components, including measurements, device channels, customer and organization details, measuring point information, and measurement properties.

## measurement-slim
This JSON schema, crucially used by the Testo 300 device when exporting measurement data using a QR code, defines a structured data object.

Additionally, for those interested in delving deeper into the QR code functionality of the Testo 300 device, further information can be found at [this link](https://developers.testo.dev/t300/qrcode/).
