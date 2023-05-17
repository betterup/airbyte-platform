#!/usr/bin/env bash

TEMPORAL_VERSION=1.20.3

curl -OL https://github.com/temporalio/temporal/archive/refs/tags/v"$TEMPORAL_VERSION".tar.gz
tar -xvf v"$TEMPORAL_VERSION".tar.gz
cd temporal-"$TEMPORAL_VERSION" && docker build . -t airbyte/temporal-auto-setup:"$TEMPORAL_VERSION" --build-arg TARGET=auto-setup
rm -rf ../temporal-"$TEMPORAL_VERSION" ../v"$TEMPORAL_VERSION".tar.gz
