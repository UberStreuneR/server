FROM python:3.9

ARG USER_ID
ARG GROUP_ID

COPY requirements/test-requirements.txt /tmp/test-requirements.txt

RUN apt-get update && \
    apt-get install -y apache2 \
            libapache2-mod-wsgi-py3

RUN set -x \
    && python -m venv /opt/orders_api \
    && /opt/orders_api/bin/python -m pip install -U pip wheel setuptools a2wsgi \
    && /opt/orders_api/bin/python -m pip install --no-cache-dir -q -r /tmp/test-requirements.txt \
    && mkdir -p /workspace && chown -R www-data:www-data /workspace && chown -R www-data:www-data /opt/orders_api
    # && mkdir -p /workspace && chown -R $USER_ID:$GROUP_ID /workspace && chown -R $USER_ID:$GROUP_ID /opt/orders_api
# RUN addgroup --gid $GROUP_ID user
# RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
# USER user

# Activate the mod_wsgi
RUN a2enmod wsgi

# Add the apache VirtualHost, to setup the WSGI module for the app
# COPY apache-vhost.conf /etc/apache2/sites-enabled/000-default.conf

# Optional: Redirect error log to stdout, to make it visible in `docker compose up` output
RUN ln -sf /dev/stdout /var/log/apache2/error.log


WORKDIR /workspace

ENV PATH="/opt/orders_api/bin:${PATH}"

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /workspace/src

CMD ["apachectl", "-D", "FOREGROUND"]