# railway.toml

Source: junk_drawer/github/DeltaDash/frontend/railway.toml.txt

Category: [[github-code]]

## Summary
[build] dockerfilePath = "Dockerfile" [build.args] VITE_API_URL = "https://deltadash-backend-production.up.railway.app" [deploy] healthcheckPath = "/" healthcheckTimeout = 30 restartPolicyType = "on_failure"

## Full Content
[build]
dockerfilePath = "Dockerfile"

[build.args]
VITE_API_URL = "https://deltadash-backend-production.up.railway.app"

[deploy]
healthcheckPath = "/"
healthcheckTimeout = 30
restartPolicyType = "on_failure"


## Metadata
- Source file: junk_drawer/github/DeltaDash/frontend/railway.toml.txt
- Extracted: 2026-05-18
- Category: github-code
