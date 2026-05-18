# desert_pyramid.json

Source: junk_drawer/github/TheAncientWorld/src/main/resources/data/theancientworld/loot_tables/chests/desert_pyramid.json.txt

Category: [[github-code]]

## Summary
{ "pools": [ { "name": "main", "rolls": 1, "entries": [ { "type": "item", "weight": 10, "name": "theancientworld:strength_ring"

## Full Content
{
  "pools": [
    {
      "name": "main",
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "weight": 10,
          "name": "theancientworld:strength_ring"
        },
        {
          "type": "item",
          "weight": 10,
          "name": "theancientworld:resistance_ring"
        },
        {
          "type": "item",
          "weight": 10,
          "name": "theancientworld:potion_ring"
        },
        {
          "type": "minecraft:empty",
          "weight": 50
        }
      ]
    },
    {
      "name": "glowing_ingredients",
      "rolls": {
        "min": 2.0,
        "max": 6.0,
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
          "weight": 10,
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
          "name": "theancientworld:glowing_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0.0,
                "max": 1.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "theancientworld:adamant_plate"
        }
      ]
    }
  ]
}

## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/resources/data/theancientworld/loot_tables/chests/desert_pyramid.json.txt
- Extracted: 2026-05-18
- Category: github-code
