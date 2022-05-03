FROM adoptopenjdk/openjdk11:x86_64-alpine-jre-11.0.14.1_1
COPY target/hello-world-1.0.1-SNAPSHOT.jar /usr/src/webserver.jar
WORKDIR /usr/src/
EXPOSE 9090
ENTRYPOINT ["java", "-jar", "webserver.jar"]

