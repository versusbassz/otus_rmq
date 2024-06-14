from __future__ import annotations
from typing import Awaitable, TypeAlias
import random
from dataclasses import dataclass
import asyncio

from id_generator import generate_car_id, REGION_MSK, REGION_SPB


Second: TypeAlias = float

STYLE_CALM: str = 'calm'
STYLE_CRAZY: str = 'crazy'


async def main():
    time_manager = TimeManager(sending_interval=3.0, timescale=1.0)

    car1 = Car.build(region=REGION_MSK, style=STYLE_CALM, max_time=15.0)
    car2 = Car.build(region=REGION_SPB, style=STYLE_CRAZY, max_time=30.0)

    car1_task = asyncio.create_task(run_car(car1, time_manager))
    car2_task = asyncio.create_task(run_car(car2, time_manager))
    await car1_task
    await car2_task

    print('Command finished')


async def run_car(car: Car, time_manager: TimeManager):
    async for report in track_car(car, time_manager):
        print(report)


async def track_car(car: Car, time_manager: TimeManager):
    time_on_road: float = 0.0

    while True:
        if time_on_road >= car.max_time:
            yield Report(cid=car.cid, region=car.region, speed=0)
            return

        new_speed = float(random.randint(0, car.max_speed))
        report = Report(cid=car.cid, region=car.region, speed=new_speed)
        yield report

        time_on_road += time_manager.sending_interval
        await asyncio.sleep(time_manager.real_interval)


@dataclass
class TimeManager:
    sending_interval: Second
    timescale: float = 1.0

    @property
    def real_interval(self) -> Second:
        return self.sending_interval * self.timescale


@dataclass
class Car:
    cid: str
    region: str
    style: str
    max_time: Second = 30.0

    @property
    def max_speed(self) -> int:
        if self.style == STYLE_CALM:
            return 110
        elif self.style == STYLE_CRAZY:
            return 190
        else:
            raise ValueError(f'incorrect Car.style: {self.style}')

    @classmethod
    def build(cls, *, region: str, style: str, max_time: Second, cid: str = '') -> Car:
        cid_ = cid if cid else generate_car_id(region)
        return Car(cid=cid_, region=region, style=style, max_time=max_time)


@dataclass
class Report:
    """
    {"cid": "К544ХМ197", "speed": 90.0}
    """
    cid: str  # "car id"
    speed: float
    region: str


if __name__ == '__main__':
    asyncio.run(main())
