ARG JDK_IMAGE=airbyte/airbyte-base-java-image:2.0.2
FROM ${JDK_IMAGE} AS metrics-reporter

ARG VERSION=0.44.4

ENV APPLICATION airbyte-metrics-reporter
ENV VERSION ${VERSION}

RUN addgroup -S appgroup && \
    adduser -S appuser -G appgroup -u 1000


WORKDIR /app

ADD bin/${APPLICATION}-${VERSION}.tar /app

# Removes vulnerabilities flagged in Prisma

# CVE: https://nvd.nist.gov/vuln/detail/CVE-2023-34462
RUN rm /app/airbyte-metrics-reporter-dev/lib/netty-handler-4.1.94.Final.jar

USER appuser

# wait for upstream dependencies to become available before starting server
ENTRYPOINT ["/bin/sh", "-c", "${APPLICATION}-${VERSION}/bin/${APPLICATION}"]
