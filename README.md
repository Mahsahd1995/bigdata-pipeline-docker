Big Data Sentiment Analysis Pipeline with Docker

This project demonstrates how to build an end-to-end big data pipeline using Docker, Hadoop, Hive, Spark, and PySpark MLlib for sentiment analysis of Amazon customer reviews.

- GitHub: https://github.com/mahshad1995/bigdata-pipeline-docker

- Technologies Used

Docker & Docker Compose

Hadoop HDFS (for distributed storage)

Hive (for querying large datasets)

Apache Spark (for distributed data processing)

PySpark + MLlib (for machine learning)

Python 3.8

- Project Structure

├── docker-compose.yml         # Docker config for Hadoop, Hive, Spark
├── sentiment_pipeline.py      # PySpark ML pipeline script
├── hive_table.sql             # Hive table definition and load command

- Getting Started

Step 1: Clone the repository

git clone https://github.com/mahshadsalari/bigdata-pipeline-docker.git
cd bigdata-pipeline-docker

Step 2: Launch the Big Data environment

docker-compose up -d

Step 3: Load the dataset to HDFS (from namenode container)

docker exec -it <namenode_container> bash
hdfs dfs -mkdir -p /user/student/amazon_reviews
hdfs dfs -put amazon_reviews.tsv /user/student/amazon_reviews/

Step 4: Create Hive table (from hive container)

Run contents of hive_table.sql inside the Hive CLI.

Step 5: Train model with PySpark

docker exec -it <spark_container> spark-submit /opt/sentiment_pipeline.py

- Output

The model performs binary sentiment classification on reviews (positive or negative) using logistic regression. Outputs include:

Cleaned and labeled data

Feature extraction using TF-IDF

Accuracy, precision, recall, F1-score

Top 10 prediction samples

-Author

Mahshad Salari - Big Data Analytics, 2025

- License

This project is for educational use in academic coursework.

