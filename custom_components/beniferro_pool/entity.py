from homeassistant.helpers.update_coordinator import CoordinatorEntity
class BeniferroEntity(CoordinatorEntity):
    _attr_has_entity_name=True
    def __init__(self,coordinator,key,name):
        super().__init__(coordinator)
        self.key=key
        self._attr_name=name
        self._attr_unique_id=f"{coordinator.host}_{key}"
    @property
    def device_info(self):
        return {"identifiers":{("beniferro_pool",self.coordinator.host)},"name":"Beniferro Pool"}
