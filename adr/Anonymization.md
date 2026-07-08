# Architectural Decision: Anonymization

## Decision
Implement anonymization using cohort analysis via secure aggregation methods.

## Rationale
Ensures compliance with GDPR by anonymizing personal data before analytics while keeping the ability to generate insights.

## Alternatives
1. Direct Encryption Storage
   - Pros: High security.
   - Cons: Limited usability for aggregated analytics.

2. Pseudonymization
   - Pros: Useful for tracking individual-level metrics.
   - Cons: Risk of deanonymization.

## Consequences
Keeps analytic insights compliant, but may require advanced aggregation techniques.