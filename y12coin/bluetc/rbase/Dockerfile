FROM gliderlabs/alpine:3.1
# upgrade to edge
RUN sed -i -e 's/v3\.1/edge/g' /etc/apk/repositories
#RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >>  /etc/apk/repositories
RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >>  /etc/apk/repositories
RUN apk upgrade --update-cache --available
RUN apk-install bash boost
