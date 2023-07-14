ARG JDK_IMAGE=airbyte/airbyte-base-java-image:2.0.2
FROM ${JDK_IMAGE} AS worker

ARG DOCKER_BUILD_ARCH=amd64

RUN apk add jq tar

RUN wget "https://dl.k8s.io/release/$(wget -qO- https://dl.k8s.io/release/stable.txt)/bin/linux/${DOCKER_BUILD_ARCH}/kubectl" \
        && chmod +x kubectl && mv kubectl /usr/local/bin/

# Don't change this manually.  Bump version expects to make moves based on this string
ARG VERSION=0.44.4

ENV APPLICATION airbyte-workers
ENV VERSION ${VERSION}

WORKDIR /app

COPY WellKnownTypes.json /app

# Move worker app
ADD bin/${APPLICATION}-${VERSION}.tar /app

# Grab well-known types file
COPY WellKnownTypes.json /app

# Removes lingering jars with vulnerable packages
RUN \
    # removes jars with guava_guava
    rm /app/airbyte-workers-dev/lib/launchdarkly-java-server-*.jar && \
    rm /app/airbyte-workers-dev/lib/auto-value-*.jar && \
    # removes jars with netty_netty
    rm /app/airbyte-workers-dev/lib/micrometer-registry-statsd-*.jar && \
    echo '*Removed all jars with guava_guava vulnerability*'

# wait for upstream dependencies to become available before starting server
ENTRYPOINT ["/bin/sh", "-c", "${APPLICATION}-${VERSION}/bin/${APPLICATION}"]
