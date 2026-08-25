# Contribution History

A summary of my open-source contributions to [Vector](https://github.com/vectordotdev/vector), a high-performance observability data pipeline.

## DataDog / Vector

My contributions to Vector have focused on improving code quality, enabling new features, and modernizing the codebase. Below is a summary of my merged pull requests.

### ✨ New Features

- **[#26075 - enhancement(prometheus scrape): support request headers](https://github.com/vectordotdev/vector/pull/26075)**  
  Added support for configurable HTTP request headers to the `prometheus_scrape` source. This allows users to pass custom headers (e.g., `Accept: application/openmetrics-text`) when scraping Prometheus endpoints, improving compatibility with various metrics endpoints.

### 🧹 Code Cleanup & Maintenance

- **[#26183 - chore(aws kinesis firehose): remove obsolete const lint allow](https://github.com/vectordotdev/vector/pull/26183)**  
  Made the `RequestError::request_id` accessor const-compatible, allowing removal of an obsolete Clippy lint suppression. This contributes to ongoing internal cleanup to reduce module-level lint suppressions that can mask issues.

- **[#26128 - chore(core): remove obsolete const lint allows](https://github.com/vectordotdev/vector/pull/26128)**  
  Removed two obsolete `clippy::missing_const_for_fn` allowances by making affected string getters const. This internal Rust API cleanup improves code quality and maintainability.

- **[#26059 - chore(config): remove obsolete Darling lint allows](https://github.com/vectordotdev/vector/pull/26059)**  
  Removed obsolete crate-level Clippy allowances for `manual_unwrap_or_default` from `vector-config-common` and `vector-config-macros`. With Vector's pinned Rust 1.95 toolchain, these suppressions are no longer needed.
