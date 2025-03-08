# Scalable-Data-Processing-System-for-High-Volume-Workloads

## Overview

This project implements a high-performance data ingestion and processing pipeline using Kafka, AWS Kinesis, PostgreSQL, and Kubernetes.

## Features

- **Asynchronous Data Processing:** Kafka producers and consumers for efficient message handling.
- **Optimized Database Indexing:** PostgreSQL with partitioning for better query performance.
- **Self-Healing Microservices:** Kubernetes auto-scaling and health checks.
- **AWS Integration:** AWS Kinesis for real-time data streaming.

## Technologies Used

- **Programming Languages:** Python, Java, C++
- **Message Queue:** Kafka, AWS Kinesis
- **Database:** PostgreSQL
- **Containerization:** Docker, Kubernetes

## Project Structure

```
scalable_data_pipeline/
│── producer/
│   ├── producer.py (Kafka producer implementation)
│── consumer/
│   ├── consumer.py (Kafka consumer implementation)
│── database/
│   ├── init.sql (PostgreSQL schema and partitioning setup)
│── k8s/
│   ├── deployment.yaml (Kubernetes deployment)
│   ├── service.yaml (Kubernetes service)
│── README.md
```

## Getting Started

### Prerequisites

1. **Install Docker and Kubernetes on Windows**

   - Download and install **[Docker Desktop](https://www.docker.com/products/docker-desktop/)**.
   - Enable Kubernetes in Docker settings.
   - Restart Docker after enabling Kubernetes.

2. **Install and Setup Kafka on Windows**

   - **Step 1:** Download **Apache Kafka** and **Zookeeper** from [Kafka Downloads](https://kafka.apache.org/downloads).
   - **Step 2:** Extract Kafka and navigate to the folder:
     ```sh
     cd kafka_2.13-3.5.1
     ```
   - **Step 3:** Start Zookeeper (Kafka requires Zookeeper):
     ```sh
     bin\windows\zookeeper-server-start.bat config\zookeeper.properties
     ```
   - **Step 4:** Start Kafka Server:
     ```sh
     bin\windows\kafka-server-start.bat config\server.properties
     ```
   - **Step 5:** Create a Kafka topic:
     ```sh
     bin\windows\kafka-topics.bat --create --topic data_topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
     ```
   - **Step 6:** Verify topic creation:
     ```sh
     bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
     ```

3. **Setup PostgreSQL**
   - Install **PostgreSQL** from [PostgreSQL Official Website](https://www.postgresql.org/download/).
   - Start PostgreSQL using `docker-compose up -d postgres`.

### Running the Project

#### Step 1: Start Kafka and PostgreSQL

```sh
docker-compose up -d kafka zookeeper postgres
```

#### Step 2: Start the Producer

```sh
python producer/producer.py
```

#### Step 3: Start the Consumer

```sh
python consumer/consumer.py
```

#### Step 4: Deploy on Kubernetes

```sh
kubectl apply -f k8s/
```

## PostgreSQL Partitioning Strategy

```sql
CREATE TABLE data (
    id SERIAL PRIMARY KEY,
    event_time TIMESTAMP NOT NULL,
    payload JSONB
) PARTITION BY RANGE (event_time);

CREATE TABLE data_2024 PARTITION OF data
    FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
```

## AWS Kinesis Integration

- AWS Kinesis producer writes data streams.
- Consumer reads data and ingests it into PostgreSQL.

## Scaling with Kubernetes

- Auto-scaling based on CPU/memory usage.
- Health checks for monitoring system reliability.

## Next Steps

- Implement additional data transformations.
- Improve fault tolerance with retry mechanisms.
- Add real-time monitoring using Prometheus & Grafana.

---
