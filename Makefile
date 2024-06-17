@:
	@ echo "No default command"
	@ false

d.up:
	@ docker compose up -d

d.start:
	@ docker compose start

d.stop:
	@ docker compose stop

d.prune:
	@ docker compose down -v  --remove-orphans
	@ rm -rf ./data/volumes/rmq_*
