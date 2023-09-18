FROM tomcat:8.0
ADD **/*.war

EXPOSE 8080
CMD ["catalina.sh", "run"]