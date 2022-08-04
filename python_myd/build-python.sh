#################################################################################
# File name : build-python.sh
#
# Create at       : 17/06/2022 13:35:28
# Create by      : [Lenny Delgado]
# -------------------------------------------------------------------------------------
# Description   : Python base container build script
#
# -------------------------------------------------------------------------------------
#
# Parameters    :
#                 $1 => N° version de python (3.10.4)
#                 $2 => Docker repository URL
#
# Exemple       : ./build-python.sh 3.10.4 your-docker-repository-url.com
#
#################################################################################

# Recovery python version we use
export PYTHON_VERSION=$1

# Repository docker url
export REPO_DOCKER_URL=$2

# All image depends of debian_slim_myd:latest
# Take the latest version of debian-bulleye-slim
docker pull ${REPO_DOCKER_URL}/debian_slim_myd:latest

# Deleting of previously generated images
docker image rm ${REPO_DOCKER_URL}/python${PYTHON_VERSION}:latest 2>&1 $PWD/logs/python_build_log.txt
docker image rm python${PYTHON_VERSION}:latest 2>&1 $PWD/logs/python_build_log.txt

# Image build and push it on your repository
docker image build --build-arg PYTHON_VERSION="$PYTHON_VERSION" --build-arg REPO_DOCKER_URL="$REPO_DOCKER_URL" -f $PWD/python_myd/python${PYTHON_VERSION}.dockerfile -t python${PYTHON_VERSION}:latest .
docker tag python${PYTHON_VERSION}:latest ${REPO_DOCKER_URL}/python${PYTHON_VERSION}:latest
docker push ${REPO_DOCKER_URL}/python${PYTHON_VERSION}:latest
