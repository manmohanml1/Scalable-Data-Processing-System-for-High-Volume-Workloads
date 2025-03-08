#!/bin/bash
echo "Starting services..."
python producer/producer.py &
python consumer/consumer.py &
