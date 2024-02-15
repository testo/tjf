# tjf - schema definitions

The schemas nested within folders are remnants of a legacy system, retained primarily for compatibility reasons. However, for the majority of users, these schemas serve little purpose in the modern context and can be safely disregarded.

## measurementCollection
The schema represents a structured collection of individual measurements like defined in [slim-schema](#slim-schema), each independent of the others. These measurements are further enriched with additional features such as images, comments, and information about the organization and customer associated with the data.

## slim-schema
The schema delineates a comprehensive data structure exported by Testo applications. It encompasses various components, including measurements, device channels, customer and organization details, measuring point information, and measurement properties.

It mandates adherence to a specific schema version and outlines stringent formatting rules for each component. For instance, it requires channels to be described in an array, with each item conforming to a predefined structure.

Moreover, it enforces the presence of essential information such as timestamps, measurement types, and customer details. Additionally, it allows for optional elements like additional measurement information and images, providing flexibility in data representation.

In summary, the schema serves as a blueprint for ensuring the consistency, integrity, and interoperability of exported data across different systems and applications.
