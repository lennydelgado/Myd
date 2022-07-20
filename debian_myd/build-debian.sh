#################################################################################
# File name : build-debian.sh
#
# Create at        : 04/07/2022 11:35:28
# Create by      : [Lenny Delgado]
# -------------------------------------------------------------------------------------
# Description   : Script to build Docker container with debian image
#
# -------------------------------------------------------------------------------------
#
# Parameters    :
#                 $1 => Docker repository URL
#
# Exemple       : ./build-debian.sh your_repo_url.com
#
#################################################################################

# Docker repository
export REPO_DOCKER_URL=$1

# All image depends of debian_slim_myd:latest
# Take the latest version of debian-bulleye-slim
docker pull debian:bullseye-slim

# Image build and push it on your repository
docker image build -f $PWD/debian_myd/debian_myd.dockerfile --build-arg CACHEBUST=$(date +%s) -t debian_myd:latest .
docker tag  debian_myd:latest ${REPO_DOCKER_URL}/debian_myd:latest
docker push  ${REPO_DOCKER_URL}/debian_myd:latest