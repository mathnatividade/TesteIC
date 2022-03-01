#!/bin/bash

#Rejeita pacotes danificados
#iptables -A FORWARD -m unclean -j DROP

#Libera acesso as portas 22 e 80 por todas as redes
iptables -A INPUT -p tcp --destination-port 22 -j ACCEPT
iptables -A INPUT -p tcp --destination-port 80 -j ACCEPT
iptables -A INPUT -p tcp --destination-port 443 -j ACCEPT

#Libera acesso as portas de 9000 a 9010 apenas a rede local
iptables -A INPUT -p tcp --syn -s 192.168.1.0/24 --dport 9000:9010 -j ACCEPT
#iptables -A INPUT -p tcp --destination-port 9000:9010 -s 172.10.0.0/255.255.255.0 -j ACCEPT

#Fechando as outras portas 
iptables -A INPUT -p tcp --syn -j DROP

#Rejeita ping
#echo "1" > /proc/sys/net/ipv4/icmp_echo_ignore_all