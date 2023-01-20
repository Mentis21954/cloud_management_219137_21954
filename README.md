# cloud_management_219137_21954
team 11:
Μέντης Κωνσταντίνος Αντώνιος: it21954
Γεροκώστας Κωνσταντίνος: it219137 


KAFKA 
- install kafka with docker compose (url: https://developer.confluent.io/quickstart/kafka-docker/)
docker-compose up -d
docker-compose down

- create a topic
docker exec broker \
kafka-topics --bootstrap-server broker:9092 \
             --create \
             --topic iphone

- write to the topic
docker exec --interactive --tty broker \
kafka-console-producer --bootstrap-server broker:9092 \
                       --topic iphone

- read messages from the topic
docker exec --interactive --tty broker \
kafka-console-consumer --bootstrap-server broker:9092 \
                       --topic iphone \
                       --from-beginning


Mongo DB for UBUNTU (url installation: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)
- sudo systemctl start mongod
- sudo systemctl status mongod
- sudo systemctl stop mongod
- sudo systemctl restart mongod


# Start project
- run app: python app.py
- run producer: python produce.py
- run consumer: python consume.py
- view list of collections and created users from mongodb: python mongodb.py

# EXAMPLES ENDPOINTS FOR APP
- CREATE USER 
/create/maria?k1=iphone&k2=android&k3=cars&k4=intel&k5=microsoft&k6=sony&k7=java&k8=python&city=athens 
/create/kostas?k1=pop&k2=greece&k3=cars&k4=gaming&k5=microsoft&k6=sony&k7=xbox&k8=marketing&city=patra

- READ USER
read/kostas

- UPDATE USER
update/maria?k1=pop&k2=greece&k3=cars&k4=gaming&k5=microsoft&k6=sony&k7=xbox&k8=marketing

- DELETE USER
delete/maria
