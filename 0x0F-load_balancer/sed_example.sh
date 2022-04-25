#!/usr/bin/env bash

# configure response header
sudo sed -i "/^server/a \\\tadd_header X-Served-By $HOSTNAME;" $1
