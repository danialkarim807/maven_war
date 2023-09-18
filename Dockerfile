FROM tomcat:8.5.91
ADD **/*.war /home/danial/devops-master-class/dev-master-class-web/MyWebApp/
EXPOSE 7070
CMD ["catalina.sh", "run"]