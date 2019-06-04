FROM alpine:3.9

ADD ./ /app
ENV NICKNAME=honey_dckr \
    PORT=6667 \
    SERVER=chat.freenode.net
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install -r /app/requirements.txt && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache && \
    sed -i "s/\(server_url =\).*/\1 ${SERVER}/g" /app/honeybot/settings/CONNECT.conf && \
    sed -i "s/\(port =\).*/\1 ${PORT}/g" /app/honeybot/settings/CONNECT.conf && \
    sed -i "s/\(name =\).*/\1 ${NICKNAME}/g" /app/honeybot/settings/CONNECT.conf
WORKDIR /app/honeybot/
CMD python main.py

