## TODO

- [x] data generator (`gen`)
- [ ] receivers queues + shovel/federation to the central queue
- [ ] dockerized (compose)
- [ ] xxx
- [ ] xxx
- [ ] xxx
- [ ] cluster
- [ ] MQTT in cars <-> receivers
- [ ] xxx
- [ ] xxx

## How to run

```shell
python -m venv .venv
source .venv/bin/activate

python ./apps/cars/main.py
```


## The message format

```JSON
{
  "cid": "К544ХМ197",
  "speed": 89.0
}
```
