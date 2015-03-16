FROM y12docker/pbase:15.03
WORKDIR /bcp2p
RUN npm install bunyan
RUN npm install bitcore bitcore-p2p
ADD app.js /bcp2p/

# josegonzalez/python-beaver
# https://github.com/josegonzalez/python-beaver
RUN pip install beaver==33.2.0

ADD beaver.conf /bcp2p/
