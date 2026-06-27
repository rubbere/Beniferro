from homeassistant.components.switch import SwitchEntity
from .entity import BeniferroEntity
from .const import DOMAIN
async def async_setup_entry(hass,entry,add):
    c=hass.data[DOMAIN][entry.entry_id]
    add([BeniferroRelay(c,i) for i in c.data.get("relays",{})])
class BeniferroRelay(BeniferroEntity,SwitchEntity):
    def __init__(self,c,i):
        super().__init__(c,f"relay_{i}",f"Relay {i}")
        self.i=i
    @property
    def is_on(self):
        return self.coordinator.data.get("relays",{}).get(self.i,{}).get("power")
