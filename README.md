# SF Crime Statistics with Spark Streaming

## Intro

In this project, you will be provided with a real-world dataset, extracted from Kaggle, on San Francisco crime incidents, and you will provide statistical analyses of the data using Apache Spark Structured Streaming. You will draw on the skills and knowledge you've learned in this course to create a Kafka server to produce data, and ingest data through Spark Structured Streaming.

## Development Environment

You may choose to create your project in the workspace we provide here, or if you wish to develop your project locally, you will need to set up your environment properly as described below:

- Spark 2.4.3
- Scala 2.11.x
- Java 1.8.x
- Kafka build with Scala 2.11.x
- Python 3.6.x or 3.7.x

## Kafka-consumer

![consumer](https://github.com/yl2982/SF-Crime-Statistics-with-Spark-Streaming/blob/master/screenshots/1.png?raw=True)

## Progress

![progress](https://github.com/yl2982/SF-Crime-Statistics-with-Spark-Streaming/blob/master/screenshots/2.png?raw=True)

## Question

### 1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
It affected how much data was being processed.

### 2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
- `Kafka.bootstrap.servers`: without it, Kafka streaming won't run.
- `maxRatePerPartition`: decides the throughput and latency of the data.



