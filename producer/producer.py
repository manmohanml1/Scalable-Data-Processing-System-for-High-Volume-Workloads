import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092', 
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_message(topic, message):
    producer.send(topic, message)
    producer.flush()

if __name__ == "__main__":
    for i in range(10):
        send_message('data_topic', {'id': i, 'event_time': '2025-03-07T12:00:00Z', 'payload': f'message_{i}'})
    print("Messages sent to Kafka!")
