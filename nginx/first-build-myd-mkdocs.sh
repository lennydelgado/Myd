#################################################################################
# File name: first-build-myd-mkdocs.sh
#
# Create at      : 04/07/2022 14:49:28
# Create by      : [Lenny Delgado]
# -------------------------------------------------------------------------------------
# Description   : Script to build the first time MkDocs container
#
# -------------------------------------------------------------------------------------
#
# Parameters    :
#                 $1 => Python version
#                 $2 => Docker repository URL
#                 $3 => Token link with github account of the repository with mkdocs
#                 $4 => Paste link of repository github where is located the root of mkdocs file
#
# Exemple       : ./first-build-myd-mkdocs.sh 3.10.4 your-repository-docker.com your_token_github https://github.com/user/project-name/archive/name-of-branch.zip
#
#
#################################################################################

# Recovery of the python version
export PYTHON_VERSION=$1

# Recovery of your docker repository
export REPO_DOCKER_URL=$2

# Recovery of the token github
export GIT_TOKEN=$3

# Recovery of link to your project
export REQUIREMENTS_FILE=$4

# Build image with MkDocs
docker image build --no-cache --build-arg CACHEBUST=$(date +%s) --build-arg REPO_DOCKER_URL --build-arg PYTHON_VERSION --build-arg GIT_TOKEN --build-arg REQUIREMENTS_FILE -f $PWD/nginx/first-myd-mkdocs.dockerfile -t myd-mkdocs:latest .
docker tag myd-mkdocs:latest ${REPO_DOCKER_URL}/myd-mkdocs:latest
docker push ${REPO_DOCKER_URL}/myd-mkdocs:latest
