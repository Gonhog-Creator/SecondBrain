# satyr.json

Source: junk_drawer/github/TheAncientWorld/src/main/resources/data/theancientworld/loot_tables/entities/satyr.json.txt

Category: [[github-code]]

## Summary
{ "type": "minecraft:entity", "pools": [ { "rolls": 2, "entries": [ { "type": "minecraft:item", "functions": [ {

## Full Content
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0.0,
                "max": 2.0,
                "type": "minecraft:uniform"
              }
            },
            {
              "function": "minecraft:looting_enchant",
              "count": {
                "min": 0.0,
                "max": 1.0
              }
            }
          ],
          "name": "theancientworld:raw_satyr_meat"
        }
      ]
    }
  ]
}

## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/resources/data/theancientworld/loot_tables/entities/satyr.json.txt
- Extracted: 2026-05-18
- Category: github-code
