## CDC Pipeline Architecture

### Source
- DynamoDB table storing application state

### Change Capture
- DynamoDB Streams capture row-level mutations

### Transport
- Kinesis Data Streams buffer events durably

### Delivery
- Firehose handles batching, retries, and S3 fallback

### Transformation
- Lambda normalizes records into analytics-ready documents

### Storage & Analytics
- OpenSearch Serverless (time-series collection)
- S3 for dead-letter and replay

### CAP Model
- AP (Availability + Partition tolerance)
- Eventual consistency
