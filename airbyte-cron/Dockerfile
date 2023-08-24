ARG JDK_IMAGE=airbyte/airbyte-base-java-image:2.0.2
FROM ${JDK_IMAGE} AS cron

ARG VERSION=0.44.4

ENV APPLICATION airbyte-cron
ENV VERSION ${VERSION}

RUN addgroup -S appgroup && \
    adduser -S appuser -G appgroup -u 1000
USER appuser

WORKDIR /app

# This is automatically unzipped by Docker
ADD bin/${APPLICATION}-${VERSION}.tar /app

# Removes vulnerabilities flagged in Prisma

# CVE: https://nvd.nist.gov/vuln/detail/CVE-2023-34462
RUN rm /app/airbyte-server-dev/lib/netty-handler-4.1.94.Final.jar

# CVE: https://nvd.nist.gov/vuln/detail/CVE-2023-2976
# CVE: https://nvd.nist.gov/vuln/detail/CVE-2023-2976
# CVE: https://nvd.nist.gov/vuln/detail/CVE-2020-8908
RUN rm  /app/airbyte-server-dev/lib/launchdarkly-java-server-sdk-6.2.0.jar

# wait for upstream dependencies to become available before starting server
ENTRYPOINT ["/bin/sh", "-c", "${APPLICATION}-${VERSION}/bin/${APPLICATION}"]
