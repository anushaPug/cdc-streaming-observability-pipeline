# DynamoDB CDC & Observability Pipeline

This project implements a serverless Change Data Capture (CDC) pipeline to capture,
process, and visualize DynamoDB data mutations for observability, audit, and incident
response use cases.

## Objectives
- Capture INSERT / MODIFY / REMOVE events
- Ensure durable, at-least-once delivery
- Enable fast incident triage and auditability
- Achieve sub-minute ingestion latency

## SLA
- P95 ingestion latency < 30 seconds
- 0 data loss (S3-backed durability)
- 99.9% pipeline availability

## Architecture
DynamoDB → Streams → Kinesis → Firehose → Lambda → OpenSearch  
                                             ↘ S3 (backup)

## Key Outcomes
- ~60% reduction in incident triage time
- Searchable mutation history
- Audit-grade durability
