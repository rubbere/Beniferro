from homeassistant.components.binary_sensor import BinarySensorEntity
from .entity import BeniferroEntity
from .const import DOMAIN
KEYS=["flowswitch","levelswitch_1","levelswitch_2","levelswitch_3"]
async def async_setup_entry(hass,entry,add):
    c=hass.data[DOMAIN][entry.entry_id]
    add([BeniferroBinarySensor(c,k,k) for k in KEYS])
class BeniferroBinarySensor(BeniferroEntity,BinarySensorEntity):
    @property
    def is_on(self):
        return self.coordinator.data.get("measurements",{}).get(self.key,{}).get("value")==1
