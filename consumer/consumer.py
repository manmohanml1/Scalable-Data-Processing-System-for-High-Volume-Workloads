from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('data_topic',
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

if __name__ == "__main__":
    for message in consumer:
        print(f"Received: {message.value}")
