#################################################################################
# File name : myd-mkdocs.dockerfile
#
# Create at       : 05/07/2022 9:24:28
# Create by      : [Lenny Delgado]
# -------------------------------------------------------------------------------------
# Description   : Docker container with mkdocs
#
#################################################################################

ARG REPO_DOCKER_URL
# Recovery of Docker repository url with build arg

# Recovery of python version with build arg
ARG PYTHON_VERSION

# Previously genrated MkDocs image
FROM ${REPO_DOCKER_URL}/myd-mkdocs:latest as mkdocs

# Image python previouslys generated
FROM $REPO_DOCKER_URL/myd-python$PYTHON_VERSION:latest AS python

# Recovery of token github with build arg
ARG GIT_TOKEN


# Recovery of github repository with build arg
ARG REQUIREMENTS_FILE

# Directory with the previous requirements.txt version
WORKDIR /tmp

# Invalidate docker cache
ARG CACHEBUST
RUN echo ${CACHEBUST}

# Copy previous version of depandancies
COPY --from=mkdocs /tmp/new/requirements.txt .

# Directory with the last requirements.txt version
WORKDIR /tmp/new

# Installation via my repo allowing to have all the files necessary for the site
RUN wget --header "Authorization: token ${GIT_TOKEN}" ${REQUIREMENTS_FILE};

RUN cat requirements.txt

# Check if depandancies have been updated
RUN if cmp -s /tmp/requirements.txt /tmp/new/requirements.txt; then Not_new_dependencies; fi

# Installing dependencies
RUN pip install -r /tmp/new/requirements.txt
