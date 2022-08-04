#################################################################################
# File name : myd-docs.dockerfile
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

# Image python previouslys generated
FROM $REPO_DOCKER_URL/python$PYTHON_VERSION:latest AS python

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

# Nginx listening port --- Default value 80
ARG NGINX_PORT 80

# Adding listening port to environement variable
ENV PORT_NGINX=$NGINX_PORT

# Opening of port 80 for the container
EXPOSE ${PORT_NGINX}

WORKDIR /tmp

# Installation via my repo allowing to have all the files necessary for the site
RUN wget --header "Authorization: token ${GIT_TOKEN}" $GIT_REPO;  \
    unzip $GIT_ZIP_NAME;  \
    rm $GIT_ZIP_NAME

# Changing the name of the decompressed archive
RUN echo ${DIR_NAME}
RUN mv ${DIR_NAME}/ serv/

# Installing dependencies
RUN pip install -r serv/requirements.txt

# We go to the location of the .yml file then we build the server and we go back to the root
WORKDIR /tmp/serv/docs

RUN mkdocs build

# Cleaning folder of all installation files that are no longer needed
RUN mv site /app

# We only keep an nginx container to make it slim
FROM nginx:1.23.0-alpine AS ngx

# We go to the directory needed to install our website
WORKDIR /usr/share/nginx/html

# Copy all web page files from previous frame
COPY --from=python /app/ .

# Forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

CMD ["nginx", "-g", "daemon off;"]
