#################################################################################
# File name : build-myd-docs.sh
#
# Create at       : 04/07/2022 14:49:28
# Create by     : [Lenny Delgado]
# -------------------------------------------------------------------------------------
# Description   : Script for launching Nginx
#
# -------------------------------------------------------------------------------------
#
# Parameters    :
#                 $1 => Docker repository URL
#                 $2 => Port d'écoute externe Nginx
#
# Exemple       : ./run-nginx.sh your-repository-docker-url.com 8080
#
#################################################################################

# Repository docker url
export REPO_DOCKER_URL=$1

# External port Nginx
export NGINX_PORT_EXTERNE=$2

# NGINX port for non-container provisioning
export NGINX_PORT=80

# Delete containers if they already exist
docker rm -f nginx-myd 2>&1 $PWD/logs/nginx_run_log.txt

# Up date if needed
docker pull ${REPO_DOCKER_URL}/myd-docs:latest

# Relaunch of containers
docker run --restart=always -d --name nginx-myd -p ${NGINX_PORT_EXTERNE}:${NGINX_PORT} ${REPO_DOCKER_URL}/myd-docs:latest
