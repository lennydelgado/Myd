#################################################################################
# File name: build-myd-docs.sh
#
# Create at      : 04/07/2022 14:49:28
# Create by      : [Lenny Delgado]
# -------------------------------------------------------------------------------------
# Description   : Script to build Docker container with Nginx and Mkdocs
#
# -------------------------------------------------------------------------------------
#
# Parameters    :
#                 $1 => Python version
#                 $2 => Docker repository URL
#                 $3 => Token link with github account of the repository with mkdocs
#                 $4 => Paste link of repository github where is located the root of mkdocs file
#                 $5 => Put your GitHub account username
#                 $6 => Put your GitHub account e-mail
#                 $7 => Commit message
#
# Exemple       : ./build-myd-docs.sh 3.10.4 your-repository-docker.com your_token_github https://github.com/user/project-name/archive/name-of-branch.zip username your-mail@mail.com message
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
export GIT_REPO=$4

# Recovery of GitHub username account
export GIT_USERNAME=$5

# Recovery of GitHub email account
export GIT_MAIL=$6

# Recovery commit message
export COMMIT_MESSAGE=$7
CURRENT_DATE=`date`
COMMIT_MESSAGE="Automatic push: '$COMMIT_MESSAGE' at $CURRENT_DATE"

# Recovery of the name of .zip file
export GIT_ZIP_NAME=$(echo "$GIT_REPO" | rev | cut -d'/' -f 1 | rev)

# Recovery of the name of directory when repository is decompress
export GIT_PROJ_NAME=$(echo "$GIT_REPO" | cut -d'/' -f5)
export DIR_NAME="$GIT_PROJ_NAME-$(echo "$GIT_ZIP_NAME" | cut -d'.' -f1)"
export GIT_PAGE_REPO=$(echo "$GIT_REPO" | cut -d'/' -f3- | cut -d'/' -f1-3)
GIT_PAGE_REPO="https://"$GIT_TOKEN"@"$GIT_PAGE_REPO""
export PROJ_NAME=$(echo "$GIT_PAGE_REPO" | cut -d'/' -f5)

# Check if MkDocs image exist or not
docker manifest inspect qxzvnoxv.gra7.container-registry.ovh.net/stagelenny/myd-mkdocs:latest > /dev/null
RES=$?
if ! [ "$RES" -eq "0" ]; then
    sh nginx/./first-build-myd-mkdocs.sh ${PYTHON_VERSION} ${REPO_DOCKER_URL} ${GIT_TOKEN} ${GIT_REPO}
fi;

# Take the latest version of previsous image with python and previous image with mkdocs
docker pull ${REPO_DOCKER_URL}/myd-python${PYTHON_VERSION}:latest
docker pull ${REPO_DOCKER_URL}/myd-mkdocs:latest

# Deleting of previously generated images
docker image rm ${REPO_DOCKER_URL}/stage-lenny:latest 2>&1 $PWD/logs/nginx_build_log.txt
docker image rm stage-lenny:latest 2>&1 $PWD/logs/nginx_build_log.txt

# Build image with MkDocs only if already exist on docker repository
if [ "$RES" -eq "0" ]; then
    docker image build --build-arg CACHEBUST=$(date +%s) --build-arg REPO_DOCKER_URL --build-arg PYTHON_VERSION --build-arg GIT_TOKEN --build-arg GIT_REPO --build-arg GIT_ZIP_NAME --build-arg DIR_NAME -f $PWD/nginx/myd-mkdocs.dockerfile -t myd-mkdocs:latest . 2>&1 $PWD/logs/nginx_build_log.txt
    docker tag myd-mkdocs:latest ${REPO_DOCKER_URL}/myd-mkdocs:latest 2>&1 $PWD/logs/nginx_build_log.txt
    docker push ${REPO_DOCKER_URL}/myd-mkdocs:latest 2>&1 $PWD/logs/nginx_build_log.txt
fi;

# Build image with nginx
docker image build --build-arg CACHEBUST=$(date +%s) --build-arg COMMIT_MESSAGE --build-arg PROJ_NAME --build-arg GIT_PAGE_REPO --build-arg GIT_MAIL --build-arg GIT_USERNAME --build-arg REPO_DOCKER_URL --build-arg GIT_TOKEN -f $PWD/nginx/myd-docs.dockerfile -t stage-lenny:latest .
docker tag stage-lenny:latest ${REPO_DOCKER_URL}/stage-lenny:latest
docker push ${REPO_DOCKER_URL}/stage-lenny:latest