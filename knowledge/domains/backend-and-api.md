# Backend, APIs and Distributed Services

Trace route/transport -> authentication -> authorization -> parsing/validation -> domain logic -> persistence/outbound calls -> response/error mapping. Check async work, queues, retries, idempotency keys, ordering, transaction boundaries, partial failure, pagination, caching, serialization, versioned contracts, and role/tenant identity as evidence warrants. Avoid changing wire formats or public endpoints accidentally. Verify status codes and error envelopes under normal and failure conditions; consider API clients and workers as consumers.
