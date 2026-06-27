import aiohttp, asyncio, logging
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import DOMAIN, DEFAULT_SCAN_INTERVAL

_LOGGER=logging.getLogger(__name__)

class BeniferroCoordinator(DataUpdateCoordinator):
    def __init__(self,hass,host):
        super().__init__(hass,_LOGGER,name=DOMAIN,update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL))
        self.host=host

    async def _async_update_data(self):
        for attempt in range(3):
            try:
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
                    m=await self._fetch(session,"/api/measurements")
                    r=await self._fetch(session,"/api/relays")
                    return {"measurements":m.get("measurements",{}),"relays":r.get("relays",{})}
            except Exception as e:
                if attempt==2:
                    raise UpdateFailed(e)
                await asyncio.sleep(2)

    async def _fetch(self,s,e):
        async with s.get(f"http://{self.host}{e}") as resp:
            resp.raise_for_status()
            return await resp.json()
