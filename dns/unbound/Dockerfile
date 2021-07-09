FROM	debian:buster-slim

RUN	apt-get update && apt-get install unbound -y

COPY	pi-hole.conf /etc/unbound/unbound.conf.d

COPY	docker-entrypoint.sh .

ENTRYPOINT ["sh", "docker-entrypoint.sh"] 
