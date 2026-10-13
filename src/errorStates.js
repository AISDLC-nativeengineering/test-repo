# Error State Implementation

## Invalid Login Credentials
```javascript
export function handleInvalidLogin() {
  return 'Invalid login details, please try again.';
}
```

## Non-existent Page
```javascript
export function handle404Page() {
  return '404 Page not found - navigate back to Homepage.';
}
```

## Generic Error Banner
```javascript
export function handleGenericError() {
  return 'We encountered an issue, please try again later.';
}
```
