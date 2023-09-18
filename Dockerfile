FROM tomcat:8.0
ADD **/*.war MyWebApp/
EXPOSE 8080
CMD ["catalina.sh", "run"]