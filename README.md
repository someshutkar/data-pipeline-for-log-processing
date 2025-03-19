 # Data Pipeline for Log Processing

[![Build Status](https://img.shields.io/badge/status-active-success.svg)]()
[![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?logo=amazon-aws)](https://aws.amazon.com)
[![Databricks](https://img.shields.io/badge/Databricks-%23FF3621.svg?logo=databricks)](https://databricks.com)

A pipeline to process application logs hourly, transform them, and load them into Redshift for analysis.

## 🔹 Problem Statement
Process raw application logs into structured data for analytics while ensuring scalability and reliability.

## 🚀 Overview
1. **Extract**: Raw logs stored in AWS S3
2. **Transform**: Clean and structure data using Databricks
3. **Load**: Load processed data into Redshift Serverless

## 📋 Features
- Automatically handles schema inconsistencies
- Filters invalid/malformed logs
- Optimized for hourly batch processing
- Integrated with AWS services (S3, IAM, Redshift)

## 🛠️ Architecture
![Architecture Diagram](docs/architecture_diagram.png)

## 💻 Tech Stack
- **Storage**: AWS S3
- **Processing**: Databricks (PySpark)
- **Database**: Redshift Serverless
- **Infrastructure**: Terraform (IaC)

## 🛠️ Setup
### Prerequisites
- AWS Account with S3, Redshift, and IAM access
- Databricks workspace
- Python 3.8+ with `boto3`, `pyspark`

### Steps
1. **AWS Setup**:
   ```bash
   aws configure
   aws s3 mb s3://bucket_name-<YOUR_ACCOUNT_ID>
