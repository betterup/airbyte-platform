ARG JDK_IMAGE=airbyte/airbyte-base-java-image:2.0.2
FROM ${JDK_IMAGE}

ARG VERSION=0.44.4

ENV APPLICATION airbyte-bootloader
ENV VERSION ${VERSION}

RUN addgroup -S appgroup && \
    adduser -S appuser -G appgroup -u 1000

WORKDIR /app

ADD bin/${APPLICATION}-${VERSION}.tar /app

# Removes vulnerabilities flagged in Prisma

# CVE: https://nvd.nist.gov/vuln/detail/CVE-2023-2976
# CVE: https://nvd.nist.gov/vuln/detail/CVE-2023-2976
# CVE: https://nvd.nist.gov/vuln/detail/CVE-2020-8908
RUN rm /app/airbyte-bootloader-dev/lib/launchdarkly-java-server-sdk-*.jar
RUN rm /app/airbyte-bootloader-dev/lib/auto-value-*.jar


# CVE: https://nvd.nist.gov/vuln/detail/CVE-2023-34462
RUN rm /app/airbyte-bootloader-dev/lib/netty-handler-4.1.94.Final.jar

USER appuser

ENTRYPOINT ["/bin/sh", "-c", "${APPLICATION}-${VERSION}/bin/${APPLICATION}"]
