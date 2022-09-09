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

# Image python previouslys generated
FROM $REPO_DOCKER_URL/myd-mkdocs:latest AS mkdocs

# Recovery of token github with build arg
ARG GIT_TOKEN

# Recovery of github repository with build arg
ARG GIT_REPO

# Recovery of github zip name with build arg
ARG GIT_ZIP_NAME

# Recovery of github directory name with build arg
ARG DIR_NAME

# Recovery of github username with build arg
ARG GIT_USERNAME

# Recovery of github mail with build arg
ARG GIT_MAIL

# Recovery of github page repo with build arg
ARG GIT_PAGE_REPO

# Recovery of github directory name with build arg
ARG PROJ_NAME

# Recovery of github directory name with build arg
ARG COMMIT_MESSAGE

# Nginx listening port --- Default value 80
ARG NGINX_PORT 80

# Adding listening port to environement variable
ENV PORT_NGINX=$NGINX_PORT

WORKDIR /tmp

# Invalidate docker cache
ARG CACHEBUST
RUN echo ${CACHEBUST}

# Installation via my repo allowing to have all the files necessary for the site
RUN wget --header "Authorization: token ${GIT_TOKEN}" ${GIT_REPO};  \
    unzip $GIT_ZIP_NAME;  \
    rm $GIT_ZIP_NAME

# Changing the name of the decompressed archive
RUN echo ${DIR_NAME}
RUN mv ${DIR_NAME}/ serv/

# We go to the location of the .yml file then we build the server and we go back to the root
WORKDIR /tmp/serv/docs

# Build HTML file with MkDocs
RUN mkdocs build --site-dir site

# Check if we need install git or not
RUN apt-get update
RUN apt-get -y install git

# Configuration of git to push on repository
RUN git config --global user.name "${GIT_USERNAME}"
RUN git config --global user.email "${GIT_MAIL}"
RUN git config --global user.password "${GIT_TOKEN}"

RUN git clone ${GIT_PAGE_REPO}

WORKDIR /tmp/serv/docs/${PROJ_NAME}

# Removing previous generated HTML page
RUN rm -rf site

# Add new HTML page
RUN mv /tmp/serv/docs/site /tmp/serv/docs/${PROJ_NAME}

# Pushing to repository
RUN git add .
RUN git commit -m "${COMMIT_MESSAGE}"
RUN git push

# Cleaning folder of all installation files that are no longer needed
RUN mv site /app

# We only keep an nginx container to make it slim
FROM nginx:1.23.0-alpine AS ngx

# We go to the directory needed to install our website
WORKDIR /usr/share/nginx/html

# Copy all web page files from previous frame
COPY --from=mkdocs /app/ .

# Forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

CMD ["nginx", "-g", "daemon off;"]