from homeassistant.components.sensor import SensorEntity, SensorStateClass
from .entity import BeniferroEntity
from .const import DOMAIN

UNIT_MAP={"rx":"mV","temperature":"°C","pressure":"bar"}
ICON_MAP={"ph":"mdi:flask","rx":"mdi:flash","temperature":"mdi:thermometer","pressure":"mdi:gauge"}

async def async_setup_entry(hass,entry,async_add_entities):
    c=hass.data[DOMAIN][entry.entry_id]
    async_add_entities([BeniferroSensor(c,k,v.get("name",k)) for k,v in c.data.get("measurements",{}).items()])

class BeniferroSensor(BeniferroEntity,SensorEntity):
    _attr_state_class=SensorStateClass.MEASUREMENT
    def __init__(self,c,k,n):
        super().__init__(c,k,n)
        self._attr_native_unit_of_measurement=self._get_unit()
        self._attr_icon=self._get_icon()
    def _get_unit(self):
        for k,v in UNIT_MAP.items():
            if k in self.key: return v
        return None
    def _get_icon(self):
        for k,v in ICON_MAP.items():
            if k in self.key: return v
        return "mdi:water"
    @property
    def native_value(self):
        return self.coordinator.data.get("measurements",{}).get(self.key,{}).get("value")
