---
description: Sketch a bounded load test for an endpoint or workflow
---

# Load test

Target: $ARGUMENTS

No target given? The busiest or slowest endpoint you can identify from the code and logs. Say which, and why.

A load test answers a question. Write the question down first: "does checkout stay under 500 ms at 50 requests a second?" Without one, you're just making noise at a server.

- **Use the runner the repo already has.** If none, pick a small scriptable one and keep it to one file.
- **Thresholds before running:** latency percentile, error rate, and the load shape. p95 and p99, not the average; the average hides the people who left.
- **Realistic traffic:** the mix of calls, think time, data that isn't one cached row hit a thousand times.
- Start small and ramp. Watch the server side too (CPU, memory, connection pools, queues), or you'll know that it fell over but not why.
- **Local or a dedicated environment only.** Anything shared or production is outward-facing: ask, and expect "no".

**Done when** the question, thresholds and run command are written down, and a run is quoted with its percentiles and error rate (or you've said why it wasn't safe to run).
