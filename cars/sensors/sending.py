from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

import aio_pika
from aio_pika.abc import AbstractRobustConnection, AbstractRobustExchange
from aio_pika import ExchangeType

from .id_generator import REGION_MSK, REGION_SPB


_AUTH = 'guest:guest'
_HOSTS_DOCKER: dict[str, str] = {
    REGION_MSK: 'rmq_sensors_msk:5672',
    REGION_SPB: 'rmq_sensors_spb:5672',
}
_HOSTS: dict[str, str] = {
    REGION_MSK: '127.0.0.1:11001',
    REGION_SPB: '127.0.0.1:12001',
}


@dataclass
class Report:
    """
    {"cid": "К544ХМ197", "speed": 90.0}
    """
    cid: str  # "car id"
    speed: float
    region: str

    def json(self):
        data: dict[str, Any] = {'cid': self.cid, 'speed': self.speed, 'region': self.region}
        return json.dumps(data)


class MessageSender:
    connection: AbstractRobustConnection | None = None
    exchange: AbstractRobustExchange | None = None

    def __init__(self, region: str) -> None:
        self.region: str = region

    async def connect(self) -> None:
        url = f'amqp://{_AUTH}@{_HOSTS[self.region]}/'
        self.connection = await aio_pika.connect_robust(url)
        channel = await self.connection.channel()

        self.exchange = await channel.declare_exchange('test_exchange', type=ExchangeType.FANOUT, durable=True)

        queue = await channel.declare_queue('test_queue', durable=True)
        await queue.bind(self.exchange, '')

    async def send(self, msg: Report) -> None:
        msg = aio_pika.Message(body=msg.json().encode())
        await self.exchange.publish(msg, routing_key='')

    async def disconnect(self) -> None:
        await self.connection.close()
        self.connection = None
        self.exchange = None
