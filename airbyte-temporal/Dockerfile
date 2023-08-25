# A test describe in the README is available to test a version update
ARG TEMPORAL_AUTO_SETUP_IMAGE=temporalio/auto-setup:1.21
FROM ${TEMPORAL_AUTO_SETUP_IMAGE}

ENV TEMPORAL_HOME /etc/temporal

COPY bin/scripts/update-and-start-temporal.sh update-and-start-temporal.sh

# forcing removal of all binaries temporarily for vulnerability remediation
# https://nvd.nist.gov/vuln/detail/CVE-2023-39533
# https://nvd.nist.gov/vuln/detail/CVE-2023-39533
# https://nvd.nist.gov/vuln/detail/CVE-2023-3485
USER root
RUN rm /usr/local/bin/*

ENTRYPOINT ["./update-and-start-temporal.sh"]
