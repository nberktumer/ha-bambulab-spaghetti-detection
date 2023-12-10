"""The Bambu Lab component."""
import logging

import aiohttp
import voluptuous as vol
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant, ServiceCall, ServiceResponse, SupportsResponse
from homeassistant.helpers.network import get_url

DOMAIN = "bambu_lab_p1_spaghetti_detection"
BRAND = "Bambu Lab P1 - Spaghetti Detection"

LOGGER = logging.getLogger(__package__)

PLATFORMS = [Platform.NUMBER, Platform.DATETIME]

SPAGHETTI_DETECTION_SCHEMA = vol.Schema({
    vol.Required("host"): str,
    vol.Required("auth_token"): str,
    vol.Required("image_path"): str,
})


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the Bambu Lab P1 - Spaghetti Detection integration."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    async def spaghetti_detection_handler(call: ServiceCall) -> ServiceResponse:
        """Handle the custom service."""
        host = call.data.get("host", "")
        token = call.data.get("auth_token", "")
        image_path = call.data.get("image_path", "")

        if host.endswith("/"):
            host = host[:-1]

        async with aiohttp.ClientSession() as session:
            async with session.get(f"{host}/p/?img={get_url(hass)}{image_path}",
                                   headers={"Authorization": f"Bearer {token}"}) as response:
                result = await response.json()

        return {"hass_base_url": get_url(hass, prefer_external=True, allow_ip=False), "result": result}

    hass.services.async_register(
        DOMAIN,
        "predict",
        spaghetti_detection_handler,
        schema=SPAGHETTI_DETECTION_SCHEMA,
        supports_response=SupportsResponse.ONLY
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload Bambu Lab P1 - Spaghetti Detection integration."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
