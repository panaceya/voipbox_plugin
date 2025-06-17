FROM netboxcommunity/netbox:latest-ldap

COPY ./voipbox_plugin /source/voipbox_plugin/voipbox_plugin/
COPY ./setup.py /source/voipbox_plugin/
COPY ./MANIFEST.in /source/voipbox_plugin/
COPY ./README.md /source/voipbox_plugin/
RUN /usr/local/bin/uv pip install --no-cache-dir /source/voipbox_plugin/
