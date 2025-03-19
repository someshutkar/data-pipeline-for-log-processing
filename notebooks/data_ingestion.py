"""
Reads raw log data from S3.
"""
from pyspark.sql import SparkSession

def ingest_data(s3_path: str) -> DataFrame:
    """Read raw logs from S3."""
    spark = SparkSession.builder.getOrCreate()
    df = spark.read \
        .format("csv") \
        .option("header", "true") \
        .load(s3_path)
    return df

if __name__ == "__main__":
    # Example usage (replace with your S3 path)
    raw_df = ingest_data("s3://Youre_S3_Bucket_Name/Your File Name")
    raw_df.show(5)