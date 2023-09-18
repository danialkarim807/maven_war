FROM tomcat:8.0
ADD **/*.war /home/danial/devops-master-class/dev-master-class-web/MyWebApp/
EXPOSE 8080
CMD ["catalina.sh", "run"]