import os
import datetime as dt
from random import seed, uniform

from airflow.decorators import dag, task
import boto3
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, month, year, col

spark_conf = {
    "spark.hadoop.fs.s3a.endpoint": "http://minio:9000",
    "spark.hadoop.fs.s3a.access.key": os.environ.get("MINIO_ROOT_USER"),
    "spark.hadoop.fs.s3a.secret.key": os.environ.get("MINIO_ROOT_PASSWORD"),
    "spark.hadoop.fs.s3a.path.style.access": "true",
    "spark.hadoop.fs.s3a.impl": "org.apache.hadoop.fs.s3a.S3AFileSystem",
    "spark.jars.packages": "io.delta:delta-spark_2.12:3.2.0,org.apache.hadoop:hadoop-aws:3.3.4",
    "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
    "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog",
}


@dag(start_date=dt.datetime(2024, 1, 1), schedule="@daily", catchup=False)
def example_dag():
    @task.pyspark(conn_id="spark", config_kwargs=spark_conf)
    def create_data(spark, sc):
        s3 = get_s3_client()
        bucket_exists = True
        try:
            s3.get_bucket_acl(Bucket="example-data")
        except:
            bucket_exists = False
        if not bucket_exists:
            s3.create_bucket(Bucket="example-data")
        seed(42)
        prices = spark.createDataFrame(
            pd.DataFrame(
                {
                    "id": [i for i in range(100)],
                    "date": pd.date_range(start="2024-01-01", periods=100),
                    "price": [round(uniform(10, 2), 2) for _ in range(100)],
                    "volume": [round(uniform(100, 5)) for _ in range(100)],
                }
            ).set_index("id")
        )
        prices.write.format("delta").mode("overwrite").save("s3a://example-data/prices")

    @task.pyspark(conn_id="spark", config_kwargs=spark_conf)
    def create_monthly_volume(spark, sc):
        prices = spark.read.format("delta").load("s3a://example-data/prices")
        monthly_volumes = prices.groupBy(month("date").alias("month")).agg(
            sum("volume").alias("volume")
        )
        monthly_volumes.write.format("delta").mode("overwrite").save(
            "s3a://example-data/monthly_volumes"
        )

    @task.pyspark(conn_id="spark", config_kwargs=spark_conf)
    def create_yearly_revenue(spark, sc):
        prices = spark.read.format("delta").load("s3a://example-data/prices")
        prices = prices.withColumn("revenue", col("price") * col("volume"))
        yearly_revenue = prices.groupBy(year("date").alias("year")).agg(
            sum("revenue").alias("revenue")
        )
        yearly_revenue.write.format("delta").mode("overwrite").save(
            "s3a://example-data/yearly_revenue"
        )

    @task.pyspark(conn_id="spark", config_kwargs=spark_conf)
    def create_monthly_price(spark, sc):
        prices = spark.read.format("delta").load("s3a://example-data/prices")
        prices = prices.withColumn("revenue", col("price") * col("volume"))
        monthly_revenues = prices.groupBy(month("date").alias("month")).agg(
            sum("revenue").alias("revenue")
        )
        monthly_volumes = spark.read.format("delta").load(
            "s3a://example-data/monthly_volumes"
        )
        monthly_prices = monthly_revenues.join(monthly_volumes, on="month", how="left")
        monthly_prices = monthly_prices.withColumn(
            "price", col("revenue") / col("volume")
        )
        monthly_prices.write.format("delta").mode("overwrite").save(
            "s3a://example-data/monthly_prices"
        )

    create_data_op = create_data()
    create_data_op >> create_monthly_volume() >> create_monthly_price()
    create_data_op >> create_yearly_revenue()


def get_s3_client():
    session = boto3.Session(
        aws_access_key_id=os.environ.get("MINIO_ROOT_USER"),
        aws_secret_access_key=os.environ.get("MINIO_ROOT_PASSWORD"),
    )
    s3 = session.client(
        "s3",
        endpoint_url="http://minio:9000",
        config=boto3.session.Config(signature_version="s3v4"),
    )
    return s3


example_dag()
