FROM logstash
RUN apt-get update && apt-get install -yq net-tools
WORKDIR /loges
ADD bitcoin-search.conf /loges/

EXPOSE 9200 8333
