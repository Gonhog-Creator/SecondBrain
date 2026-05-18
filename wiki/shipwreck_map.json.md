# shipwreck_map.json

Source: junk_drawer/github/TheAncientWorld/src/main/resources/data/theancientworld/loot_tables/chests/shipwreck_map.json.txt

Category: [[github-code]]

## Summary
{ "pools": [ { "name": "glowing_ingredients", "rolls": { "min": 2.0, "max": 3.0, "type": "minecraft:uniform" }, "entries": [

## Full Content
{
  "pools": [
    {
      "name": "glowing_ingredients",
      "rolls": {
        "min": 2.0,
        "max": 3.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "theancientworld:glowing_powder"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 2.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "theancientworld:glowing_gem"
        }
      ]
    }
  ]
}

## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/resources/data/theancientworld/loot_tables/chests/shipwreck_map.json.txt
- Extracted: 2026-05-18
- Category: github-code
