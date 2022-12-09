# cloud_management_219137_21954


KAFKA 
- install kafka with docker compose (url https://developer.confluent.io/quickstart/kafka-docker/)
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


Mongo DB for UBUNTU
- sudo systemctl start mongod
- sudo systemctl status mongod
- sudo systemctl stop mongod
- sudo systemctl restart mongod
