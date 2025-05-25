Welcome to
# nginx-with-docker-basics

This is a set of examples with the basics about NGINX web server + Docker, following the next YouTube tutorial:

- **name:** "NGINX Crash Course: Web Server, Reverse Proxy & Load Balancer".
- **by:** NeuralNine (all exercises credits to this channel).
- **URL:** https://youtu.be/7FpSPSlJj-0?si=EAN9D0ff2_wFsyZQ


**This repo contains the following topics:**

1. Web server basics (static files).
2. Reverse proxy.
3. SSL certificates.
4. Basic load balancing.
5. NGINX Caching.

> **NOTE**: The tutorial starts not using Docker right away, thereby I used _docker compose scripts_ to avoid install NGINX and all packages need it. This is my contribution I left for this repo.


## Structure

1. Each directory represents an exercise, except:
  - tutorial_battery: Useful files I used for some exercises.
  - basic_compose: When I test NGNIX + backend + frontend containers before following the tutorial.
2. Not every exercise uses self-signed SSL certificates, I only generated certificates for 2 exercises:
  - ssl_certificates
  - load_balancer
3. See **ssl_certificates/web-server/certs** file for more information about SSL certificates generation. Instructions are more specific for Windows, but for another OS you must search for the command to install openssl.
4. I didn't create a directory for the last exercise, consisting of NGINX + Docker usage, because I used Docker since the beginning.
5. The "core" for each directory are the files "docker-compose.yml" and "web-server/conf/default.conf".


**I hope you find useful this repo.**
**Have a great coding day!**