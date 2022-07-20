#################################################################################
# File name : deban_myd.dockerfile
#
# Create at       : 04/07/2022 10:35:28
# Create by      : [Lenny Delgado]
# -------------------------------------------------------------------------------------
# Description   : Dockerfile to make a container with debian-bulleye-slim image
#
#################################################################################

FROM debian:bullseye-slim

# Invalidate docker cache
ARG CACHEBUST
RUN echo '$CACHEBUST'

RUN  apt-get update; \
     apt-get -y upgrade; \
     apt-get install -y zip unzip; \
     apt-get install -y wget

# Change timezone
ENV TZ=Europe/Paris

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD ["sleep", "1000000000"]
