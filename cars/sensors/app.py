from __future__ import annotations

import asyncio

from .id_generator import REGION_MSK, REGION_SPB
from .misc import Car, TimeManager, run_car, STYLE_CALM, STYLE_CRAZY


async def main():
    time_manager = TimeManager(sending_interval=3.0, timescale=1.0)

    car1 = Car.build(region=REGION_MSK, style=STYLE_CALM, max_time=15.0)
    car2 = Car.build(region=REGION_SPB, style=STYLE_CRAZY, max_time=30.0)

    car1_task = asyncio.create_task(run_car(car1, time_manager))
    car2_task = asyncio.create_task(run_car(car2, time_manager))

    await asyncio.wait([car1_task, car2_task])

    print('Command finished')
