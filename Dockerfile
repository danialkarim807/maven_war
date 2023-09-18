FROM tomcat:8.0
ADD **/*.war /opt/tomcat/for-tomcat-8.5/
EXPOSE 8080
CMD ["catalina.sh", "run"]