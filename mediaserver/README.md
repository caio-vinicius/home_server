# Docker Jellyfin + Ombi/Sonarr/Radarr/Jackett/Deluge

docker-based jellyfin with ombi, sonarr, radarr, jackett and deluge

## Motivation

- require minimal configuration and setup

## Features

- [JellyFin](https://jellyfin.org/) Jellyfin is the volunteer-built media solution that puts you in control of your media. Stream to any device from your own server, with no strings attached. Your media, your server, your way. 
- [Ombi](https://ombi.io/) is a self-hosted web application that automatically gives your shared Plex or Emby users the ability to request content by themselves.
- [Sonarr](https://sonarr.tv/) (formerly NZBdrone) is a PVR for usenet and bittorrent users. It can monitor multiple RSS feeds for new episodes of your favorite shows and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.
- [Radarr](https://radarr.video/) - A fork of Sonarr to work with movies à la Couchpotato.
- [Jackett](https://github.com/Jackett/Jackett) - Jackett works as a proxy server: it translates queries from apps (Sonarr, Radarr, SickRage, CouchPotato, Mylar, Lidarr, DuckieTV, qBittorrent, Nefarious etc.) into tracker-site-specific http queries, parses the html response, then sends results back to the requesting software.
- [Deluge](https://deluge-torrent.org/) - Deluge is a lightweight, Free Software, cross-platform BitTorrent client. 

## Requirements

- [docker](https://docs.docker.com/install/linux/docker-ce/debian/) and [docker-compose](https://docs.docker.com/compose/install/#install-compose)

## Configuration

Copy `env.sample` to `.env` and populate all fields.

## Deployment

Deploy containers with docker-compose.

```bash
docker-compose up -d
```

## Author

Caio Souza <https://github.com/caio-vinicius>

Fork and inspiration, basically all heavy lift from these guys:

Kyle Harding <https://klutchell.dev> [Buy he a beer](https://buymeacoffee.com/klutchell) https://github.com/klutchell/mediaserver

PARC6502 <https://github.com/PARC6502> https://github.com/PARC6502/docker-media-server
