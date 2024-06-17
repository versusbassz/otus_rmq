## TODO

- [x] data generator (`gen`)
- [ ] ansible deployment
- [ ] shovel/federation to the central cluster
- [ ] central cluster
- [ ] xxx
- [ ] security - separate users
- [ ] security - roles, permissions
- [ ] MQTT in cars <-> receivers
- [ ] dockerized (compose)

- [ ] xxx


## Development

```shell
pip install -r requirements.in
pip freeze > requirements.txt
```


## Dependencies

### aio_pika
- https://aio-pika.readthedocs.io/en/latest/index.html
- https://github.com/mosquito/aio-pika


## Misc

course repo: https://github.com/OtusTeam/RabbitMQ


### RabbitMQ (in general)

- https://www.rabbitmq.com/docs/uri-spec


### Ansible for docker (in general)

ansible for rmq
- docs: https://docs.ansible.com/ansible/latest/collections/community/rabbitmq/index.html
- galaxy page: https://galaxy.ansible.com/ui/repo/published/community/rabbitmq/
- repo: https://github.com/ansible-collections/community.rabbitmq

docker connection plugin
- https://docs.ansible.com/ansible/latest/collections/community/docker/docker_connection.html
- https://stackoverflow.com/questions/43807120/how-to-use-the-docker-connection-plugin-of-ansible

adding python to docker containers for ansible
- https://docs.docker.com/compose/compose-file/build/

### Shovel

https://www.rabbitmq.com/docs/shovel

how to setup shovel via ansible
- https://docs.ansible.com/ansible/latest/collections/community/rabbitmq/rabbitmq_parameter_module.html
- https://github.com/ansible-collections/community.rabbitmq/issues/153
