# DynamoDB CDC & Observability Pipeline

This project implements a serverless Change Data Capture (CDC) streaming pipeline that captures real-time data mutations (inserts, updates, deletes) from AWS DynamoDB using DynamoDB Streams. The pipeline processes these events and delivers them to durable storage and search/analytics systems, enabling auditability, debugging, and historical analysis of data changes.

The architecture is designed to be scalable, fault-tolerant, and replayable, supporting downstream use cases such as incident investigation, compliance auditing, and analytics on data change behavior. By decoupling operational workloads from analytics and audit concerns, the pipeline provides data-level visibility without impacting application performance.

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
