FROM tomcat:8.0
ADD **/*.war /opt/tomcat/apache-tomcat-8.5.91/webapps
EXPOSE 8080
CMD ["catalina.sh", "run" ]