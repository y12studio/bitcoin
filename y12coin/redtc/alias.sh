DCP=redtc
PHOME=~/git/y12bitcoin/y12coin/redtc
alias cdhome='cd ${PHOME}'
alias dc='docker-compose -p ${DCP}'
alias dcup='dc stop && dc build && dc up -d'
alias redtcdsh='docker run -i -t redtcd'
alias alicesh='docker exec -i -t ${DCP}_alice_1 /bin/bash'
alias bobsh='docker exec -i -t ${DCP}_bob_1 /bin/bash'
