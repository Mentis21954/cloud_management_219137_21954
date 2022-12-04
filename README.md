# cloud_management_219137_21954

- install kafka with docker compose (url https://developer.confluent.io/quickstart/kafka-docker/)
docker-compose up -d
docker-compose down

- create a topic
docker exec broker \
kafka-topics --bootstrap-server broker:9092 \
             --create \
             --topic my_topic

- write to the topic
docker exec --interactive --tty broker \
kafka-console-producer --bootstrap-server broker:9092 \
                       --topic my_topic

- read messages from the topic
docker exec --interactive --tty broker \
kafka-console-consumer --bootstrap-server broker:9092 \
                       --topic my_topic \
                       --from-beginning

