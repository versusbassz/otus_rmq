# Otus. RabbitMQ. The final project.

Description: Система страхового скоринга и раннего оповещения для страховой компании работающих с автопарками.
Repo: https://github.com/versusbassz/otus_rmq


## How to run

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

make d.up
ansible-playbook -vv -i deployment/hosts.ini deployment/01-sensors.yml
ansible-playbook -vv -i deployment/hosts.ini deployment/02-cluster.yml

python ./app-sensors.py

make d.prune
```


## Links

### RabbitMQ management UIs
- sensors MQ SPB: http://127.0.0.1:11002
- sensors MQ MSK: http://127.0.0.1:12002
- cluster node 1: http://127.0.0.1:21002
- cluster node 2: http://127.0.0.1:22002
- cluster node 3: http://127.0.0.1:23002

### App - "sensors"

```shell
# TODO
```


## The message format

```JSON
{
  "cid": "К544ХМ197",
  "speed": 89.0,
  "region": "spb"
}
```
