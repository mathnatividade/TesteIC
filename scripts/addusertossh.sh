#!/bin/bash
clear

#Boas vindas
echo "++++++++++++++++++++Adduser 1.0++++++++++++++++++++"
echo "Ao adicionar um usuário, será solicitado alguns dados."
echo "Basta deixar em branco e apertar enter."
echo ""

#Recebe nome de usuário
echo "Digite um nome de usuário:"
read user

#Adiciona usuário
adduser $user
#Adiciona usuário ao sudoers
usermod -aG sudo $user

#Encerra o script
echo "O usuário $user foi criado com sucesso"