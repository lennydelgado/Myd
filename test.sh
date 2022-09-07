#!/bin/bash

docker manifest inspect qxzvnoxv.gra7.container-registry.ovh.net/stagelenny/myd-mkdcs:latest > /dev/null

A=$?
if ! [ "$A" -eq "0" ]; then
    echo True;
    exit 1;
else
    echo False
    echo $A;
fi;