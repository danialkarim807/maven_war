FROM tomcat:8.0
RUN cp -a **/*.war /home/danial/devops-master-class/dev-master-class-web/MyWebApp/
EXPOSE 8080
CMD ["catalina.sh", "run"]