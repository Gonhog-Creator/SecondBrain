# pgadmin-servers.json

Source: junk_drawer/github/DeltaVision/configs/pgadmin-servers.json.txt

Category: [[github-code]]

## Summary
{ "Servers": { "1": { "Name": "DeltaVision PostgreSQL", "Group": "Servers", "Host": "postgres", "Port": 5432, "MaintenanceDB": "postgres", "Username": "deltavision_user", "Password": "deltavision_pass",

## Full Content
{
    "Servers": {
        "1": {
            "Name": "DeltaVision PostgreSQL",
            "Group": "Servers",
            "Host": "postgres",
            "Port": 5432,
            "MaintenanceDB": "postgres",
            "Username": "deltavision_user",
            "Password": "deltavision_pass",
            "SSLMode": "prefer",
            "ConnectionParameters": {
                "sslmode": "prefer"
            }
        }
    }
}


## Metadata
- Source file: junk_drawer/github/DeltaVision/configs/pgadmin-servers.json.txt
- Extracted: 2026-05-18
- Category: github-code
