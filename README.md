[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

# Bambu Lab P1 - Spaghetti Detection

A Home Assistant Integration for Bambu Lab P1 printers to add spaghetti detection capability

## Contribution

Want to contribute to ha-bambulab-spaghetti-detection? Great!  We have a few small asks though!

- Please do not fork and PR against the `main` branch
- Use the `develop` branch, this is our working area. Anything in the `main` branch should be considered live, released
  code.
- Please name your commits accordingly, and add some context as to what you have added.

## Prerequisites

- Spaghetti detection functionality depends on [Bambu Lab Integration](https://github.com/greghesp/ha-bambulab). This
  integration must be installed first.
- A server with 4GB ram, which supports [Obico](https://www.obico.io/docs/server-guides/hardware-requirements/)
  requirements.

> **_NOTE:_**  The following devices are not supported

| Device                   | Can run? | 
|--------------------------|----------|
| Raspberry Pi (Any Model) | :x:      |
| Home Assistant Green     | :x:      |
| Home Assistant Yellow    | :x:      |
| Latte Panda              | :x:      |
| Jetson Nano 2gb          | :x:      |

## Setup

1. Install Obico ML server
    1. Home Assistant Addon
    2. Standalone with Docker
2. Install `Bambu Lab P1 - Spaghetti Detection` Home Assistant Integration
3. Install HA blueprint
4. Activate HA blueprint

## 1. Install Obico ML Server

___

### i. Install Obico ML server as Home Assistant Addon

1. To install Obico ML server as a Home Assistant Add-on you have 2 options:

    1. Click the **Add Add-On Repository** button below, click **Add → Close** (You might need to enter the **internal
       IP address** of your Home Assistant instance first).

       [![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https://github.com/nberktumer/ha-bambulab-spaghetti-detection)

    2. Add the repository URL under **Settings → Add-ons → ADD-ON STORE** and click **⋮ → Repositories**:

           https://github.com/nberktumer/ha-bambulab-spaghetti-detection

2. After adding the Add-on repository, go to **Settings → Add-ons → Bambu Lab P1 - Spaghetti Detection → Bambu Lab P1 -
   Spaghetti Detection** anc click **Install**.

### ii. Install Obico ML server as a standalone Docker container

TODO

## 2. Install `Bambu Lab P1 - Spaghetti Detection` Home Assistant Integration

___

### HACS

Click the **Open HACS Repository** button below, and then click **Download** button.

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=nberktumer&repository=ha-bambulab-spaghetti-detection&category=Integration)

Go to **Settings → Devices & services → Add Integration** and add **Bambu Lab P1 - Spaghetti Detection** integration.

### Manual

Copy contents of custom_components folder to your Home Assistant config/custom_components folder. Restart Home
Assistant, and then the integration can be added and configured through the native integration setup. If you don't see
it in the native integrations list, press Ctrl+F5 to refresh the browser while you're on that page and retry.

## 3. Install HA Blueprint

___
Clink the link below to import the Spaghetti Detection blueprint

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://github.com/nberktumer/ha-bambulab-spaghetti-detection/blob/main/blueprints/spaghetti_detection.yaml)

## 4. Configure HA blueprint

___
asd
