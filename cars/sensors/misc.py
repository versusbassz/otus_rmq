from __future__ import annotations
from typing import TypeAlias

import asyncio
from dataclasses import dataclass
import random

from .id_generator import generate_car_id
from .sending import MessageSender, Report

Second: TypeAlias = float

STYLE_CALM: str = 'calm'
STYLE_CRAZY: str = 'crazy'


async def run_car(car: Car, time_manager: TimeManager):
    await car.sender.connect()
    try:
        async for report in track_car(car, time_manager):
            print(report)
            await car.sender.send(report)
    finally:
        await car.sender.disconnect()


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
    sender: MessageSender | None = None

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
        sender = MessageSender(region)
        return Car(cid=cid_, region=region, style=style, max_time=max_time, sender=sender)
