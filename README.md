# Contribution History

A living record of my open-source contributions to
**[Vector](https://github.com/vectordotdev/vector)**, the observability data
pipeline maintained by Datadog.

## Summary

Current totals:

- **10 pull requests** submitted
- **5 merged pull requests**
- **5 open pull requests**
- Primary language: **Rust**
- Focus areas: metrics ingestion, HTTP configuration, and code maintenance

## Vector Contributions

This section is generated from GitHub by `scripts/update_vector_prs.py`.

<!-- vector-prs:start -->
| PR | Type | Status | Created | Completed |
| :--- | :--- | :--- | :--- | :--- |
| [#26324 — chore(vector-buffers): remove needless pass-by-value lint allow](https://github.com/vectordotdev/vector/pull/26324) | Maintenance | Open | 2026-09-08 | — |
| [#26323 — chore(elasticsearch): remove copy receiver lint allows](https://github.com/vectordotdev/vector/pull/26323) | Maintenance | Merged | 2026-09-08 | 2026-09-08 |
| [#26321 — chore(vector-core): remove fanout pass-by-value lint allow](https://github.com/vectordotdev/vector/pull/26321) | Maintenance | Open | 2026-09-08 | — |
| [#26315 — chore(vector-config): remove borrowed box lint allow](https://github.com/vectordotdev/vector/pull/26315) | Maintenance | Open | 2026-09-07 | — |
| [#26264 — feat(datadog_agent): support v3 series metrics intake](https://github.com/vectordotdev/vector/pull/26264) | Feature | Open | 2026-08-30 | — |
| [#26183 — chore(aws kinesis firehose): remove obsolete const lint allow](https://github.com/vectordotdev/vector/pull/26183) | Maintenance | Merged | 2026-08-22 | 2026-08-26 |
| [#26128 — chore(core): remove obsolete const lint allows](https://github.com/vectordotdev/vector/pull/26128) | Maintenance | Merged | 2026-08-17 | 2026-08-20 |
| [#26127 — chore(http): remove obsolete const lint allow](https://github.com/vectordotdev/vector/pull/26127) | Maintenance | Merged | 2026-08-17 | 2026-08-17 |
| [#26075 — enhancement(prometheus scrape): support request headers](https://github.com/vectordotdev/vector/pull/26075) | Feature | Open | 2026-08-09 | — |
| [#26059 — chore(config): remove obsolete Darling lint allows](https://github.com/vectordotdev/vector/pull/26059) | Maintenance | Merged | 2026-08-07 | 2026-08-11 |
<!-- vector-prs:end -->

## Datadog Work

### [#26264 — Datadog Agent v3 Series Intake](https://github.com/vectordotdev/vector/pull/26264)

Adds support for the Datadog Agent v3 series metrics endpoint, including
protobuf decoding, conversion into Vector metrics, resource and metadata
handling, allocation limits for untrusted payloads, and regression coverage.

### [#26075 — Prometheus Scrape Request Headers](https://github.com/vectordotdev/vector/pull/26075)

Adds configurable HTTP request headers to the `prometheus_scrape` source for
authenticated endpoints and content negotiation while preserving existing
default behavior.

## Automatic Updates

The `Update Vector contribution history` workflow checks the upstream Vector
repository every hour and can also be run manually. When a new pull
request appears or an existing pull request changes state, it regenerates the
table and commits the update to this repository.
