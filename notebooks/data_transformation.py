"""
Cleans and transforms raw log data.
"""
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, to_timestamp, regexp_replace, when, regexp_extract, upper

def transform_data(raw_df: DataFrame) -> DataFrame:
    """Clean and transform raw log data with multiple processing steps."""
    return raw_df \
        # 1. Standardize timestamp format and convert to datetime type
        .withColumn("timestamp", 
                    to_timestamp(col("timestamp"), "dd-MM-yyyy HH:mm")) \
        
        # 2. Convert response_time to integer and handle invalid values
        .withColumn("response_time", 
                    regexp_replace(col("response_time"), "ms", "").cast("int")) \
        .withColumn("response_time",
                    when(col("response_time") < 0, None).otherwise(col("response_time"))) \
        
        # 3. Standardize HTTP methods to uppercase
        .withColumn("request_method", upper(col("request_method"))) \
        
        # 4. Extract URL path without query parameters
        .withColumn("url_path", regexp_extract(col("url"), r"^([^?]+)", 1)) \
        
        # 5. Categorize status codes
        .withColumn("status_category",
                    when(col("status_code").between(200, 299), "Success")
                    .when(col("status_code").between(300, 399), "Redirection")
                    .when(col("status_code").between(400, 499), "Client Error")
                    .when(col("status_code").between(500, 599), "Server Error")
                    .otherwise("Unknown")) \
        
        # 6. Validate IP addresses using proper IPv4 regex
        .withColumn("valid_ip", col("ip_address").rlike(
            r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        )) \
        
        # 7. Filter valid entries with comprehensive conditions
        .filter(
            col("status_code").isin(200, 301, 404, 500) &  # Valid status codes
            col("user_id").isNotNull() &                   # Has user ID
            col("valid_ip") &                              # Valid IP format
            col("response_time").isNotNull() &             # Has response time
            col("request_method").isin(["GET", "POST", "PUT", "DELETE"])  # Valid methods
        ) \
        .drop("valid_ip", "url")  # Remove temporary validation column and original URL

if __name__ == "__main__":
    from data_ingestion import ingest_data
    
    raw_df = ingest_data("s3://your-bucket/sample_web_logs.csv")
    cleaned_df = transform_data(raw_df)
    
    cleaned_df.printSchema()
    cleaned_df.show(5, truncate=False)

