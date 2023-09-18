FROM tomcat:8.0
ADD **/*.war MyWebApp/
EXPOSE 8000
CMD ["catalina.sh", "run"]