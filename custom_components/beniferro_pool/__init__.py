from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN
from .coordinator import BeniferroCoordinator

PLATFORMS=["sensor","binary_sensor","switch"]

async def async_setup_entry(hass:HomeAssistant,entry:ConfigEntry):
    coor=BeniferroCoordinator(hass,entry.data["host"])
    await coor.async_config_entry_first_refresh()
    hass.data.setdefault(DOMAIN,{})[entry.entry_id]=coor
    await hass.config_entries.async_forward_entry_setups(entry,PLATFORMS)
    return True
