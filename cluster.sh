#!/bin/bash

#Gestão stack de aplicações docker

case $1 in
   "start") echo "Iniciando stack de aplicações no docker."
             sudo docker-compose up -d
             #Inicia stack de aplicações de acordo com o docker-compose.yml
         ;;
   "stop") echo "Parando stack de aplicações no docker"
            sudo docker-compose stop
            #Finaliza stack de aplicações de acordo com o docker-compose.yml
         ;;
   "status") echo "Status da stack de aplicações no docker."
              sudo docker ps -a
              #Exibe o status da stack de aplicações no docker.
         ;;
   "del") echo "Parando e removendo stack de aplicações no docker"
           sudo docker-compose down
           #Comando extra, para e remove os containers no docker.
         ;;
   *) echo "Opção inválida!"
      exit 1
      ;;
esac