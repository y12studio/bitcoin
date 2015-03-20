DCP=papertc
alias dc='docker-compose -p ${DCP}'
alias dcup='dc stop && dc build && dc up -d'
alias patcdsh='docker run -i -t ${DCP}_patcd bash'
alias alicesh='docker exec -i -t ${DCP}_alice_1 bash'
