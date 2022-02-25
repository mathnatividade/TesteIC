FROM nginx

LABEL version="1.0.0" description="Hospedando aplicação web com NGINX" maintainer="Matheus Natividade"

EXPOSE 80

WORKDIR /usr/share/nginx/html/

ENTRYPOINT ["/usr/sbin/nginx"]

COPY ./default.conf /etc/nginx/conf.d/default.conf

CMD ["-g", "daemon off;"]
