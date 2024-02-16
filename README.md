# tjf - Testo JSON format
This repository contains the schema definitions of the Testo JSON format (tjf).
The tjf is used for app to app (App2App), device to device (Dev2Dev) communication and exports with testo apps and devices.

App2App is included into the following apps:

| App      | Devices |
| --------- | -----|
| SmartProbes | t115i, t405i, t410i, t510i, t549i, t605i, t805i, t905i, t770-3 |
| testo 330i App | t330i |
| testo Combustion App Android | testo 320, testo 324,  testo 327-2, testo 330, testo 335, testo 340, testo 350 (since 2011) |
| testo Combustion App iOS | t330 |
| testo 420 App | t420 |
| testo Refrigeration | t550, t557 (generation since 2015) |
| testo Smart | All devices supported by the app |
| testo 400 | t400 |

Dev2Dev is included into the following apps / devices:

| App / Device     | Devices |
| --------- | -----|
| testo 300 | t300 |
| testo 330i App | t330i |
| testo 400 | t400 |

These apps use a static UDP-Broadcast Port: 53955

Dev2Dev over Bluetooth Low Energy (BLE) is included into the following apps / devices:

| App / Device     | Devices |
| --------- | -----|
| testo 300 | t300 |

For more Information and examples please visit [Testo Interfaces](https://developers.testo.dev/t300/device-to-device/ "Visit developers.testo.dev")

## Inter App Communication / App to App interface (App2App)
Most testo apps can be called via an app to app interface (App2App) and report data back to the caller. This interface is available in the following apps and devices:

| App | Application ID | Android | iOS |
| ---------------- | -------------- | ------- | --- |
| testo Combustion | testot330  | Yes | Yes |
| testo 330i App   | testot330i | Yes | Yes |
| testo 300        | testot330i | Yes | No |
| testo 400        | testosmartprobes | Yes | No |
| testo Smart      | testosmartprobes | Yes | Yes |

For more Information and examples please visit [Testo Interfaces](https://developers.testo.dev/app-to-app/ "Visit developers.testo.dev")

## Questions ?
For questions/comments to the developer please create an issue with the corresponding label! 

