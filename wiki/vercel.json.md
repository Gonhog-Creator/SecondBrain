# vercel.json

Source: junk_drawer/github/PersonalWebsite/vercel.json.txt

Category: [[github-code]]

## Summary
{ "version": 2, "builds": [ { "src": "package.json", "use": "@vercel/next" } ], "routes": [ {

## Full Content
{
  "version": 2,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/next"
    }
  ],
  "routes": [
    {
      "src": "/side-quests/foodtree/api/(.*)",
      "dest": "/api/foodtree/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/$1"
    }
  ]
}


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/vercel.json.txt
- Extracted: 2026-05-18
- Category: github-code
