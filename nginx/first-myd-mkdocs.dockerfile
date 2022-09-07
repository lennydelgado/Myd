#################################################################################
# File name : first-myd-mkdocs.dockerfile
#
# Create at       : 05/07/2022 9:24:28
# Create by      : [Lenny Delgado]
# -------------------------------------------------------------------------------------
# Description   : First Docker container with mkdocs
#
#################################################################################

ARG REPO_DOCKER_URL
# Recovery of Docker repository url with build arg

# Recovery of python version with build arg
ARG PYTHON_VERSION

# Image python previouslys generated
FROM $REPO_DOCKER_URL/myd-python$PYTHON_VERSION:latest AS python

# Recovery of token github with build arg
ARG GIT_TOKEN

# Invalidate docker cache
ARG CACHEBUST
RUN echo '$CACHEBUST'

# Recovery of github repository with build arg
ARG GIT_REPO

# Recovery of github zip name with build arg
ARG GIT_ZIP_NAME

# Recovery of github directory name with build arg
ARG DIR_NAME

WORKDIR /tmp

# Clonning GitHub repository
RUN wget --header "Authorization: token ${GIT_TOKEN}" ${GIT_REPO};  \
    unzip $GIT_ZIP_NAME;  \
    rm $GIT_ZIP_NAME

# Changing the name of the decompressed archive
RUN echo ${DIR_NAME}
RUN mv ${DIR_NAME}/ serv/

# Installing dependencies
RUN pip install -r serv/requirements.txt

# We go to the location of the .yml file then we build the server and we go back to the root
WORKDIR /tmp/serv/docs

# Build HTML file with MkDocs
RUN mkdocs build --site-dir site
