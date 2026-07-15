# Route Planning - Multimodal Transportation

This module handles route planning for users based on their preferences for ground, aerial, or multimodal travel options. It calculates ETAs, pricing, and handles error messaging when routes are unavailable.

## Acceptance Criteria

### Multimodal Option:
When "Multimodal" is selected:
- Display routes combining ground and aerial segments.
- Include ETAs and pricing.

### Ground Only Option:
When "Ground Only" is selected:
- Provide only ground-based transport options.

### No Suitable Routes:
When no routes are available:
- Show an error message with suggestions for retry.

## Implementation Plan

### Feature Overview
Create a class `RoutePlanner` with methods for:
1. **`plan_multimodal_routes(destination)`**
    - Calculate routes combining aerial and ground transport.
    - Fetch data from external APIs for aerial routes.
    - Provide formatted output with ETA and pricing.

2. **`plan_ground_routes(destination)`**
    - Calculate ground-only routes from local transportation database.

3. **`handle_no_routes()`**
    - Generate user-friendly error messages with retry suggestions.

## Example Usage
```python
from src.route_planner import RoutePlanner

planner = RoutePlanner()

# Multimodal routes
multimodal_routes = planner.plan_multimodal_routes("Central Park, NY")
print(multimodal_routes)

# Ground-only routes
ground_routes = planner.plan_ground_routes("Statue of Liberty, NY")
print(ground_routes)

# Handling no routes
print(planner.handle_no_routes())
```