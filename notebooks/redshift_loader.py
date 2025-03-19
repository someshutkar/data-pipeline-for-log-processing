"""
Loads processed data into Redshift.
"""
from pyspark.sql import DataFrame

def load_to_redshift(df: DataFrame, jdbc_url: str, table: str) -> None:
    """Write DataFrame to Redshift."""
    df.write \
        .format("jdbc") \
        .option("url", jdbc_url) \
        .option("dbtable", table) \
        .option("user", "Your Username Here") \
        .option("password", "Your Password Here") \
        .option("driver", "com.amazon.redshift.jdbc42.Driver") \
        .mode("append") \
        .save()

if __name__ == "__main__":
    # Example usage (replace with your Redshift endpoint)
    from data_transformation import transform_data
    from data_ingestion import ingest_data
    
    raw_df = ingest_data("s3://Your Bucket Name/Your_Files.csv")
    cleaned_df = transform_data(raw_df)
    
    jdbc_url = "Your jdbc_url"
    load_to_redshift(cleaned_df, jdbc_url, "Your Table Name")
