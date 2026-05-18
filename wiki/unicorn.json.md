# unicorn.json

Source: junk_drawer/github/TheAncientWorld/src/main/resources/data/theancientworld/loot_tables/entities/unicorn.json.txt

Category: [[github-code]]

## Summary
{ "type": "minecraft:entity", "pools": [ { "rolls": 1, "entries": [ { "type": "minecraft:item", "functions": [ {

## Full Content
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
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
          "name": "theancientworld:unicorn_meat"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "theancientworld:unicorn_horn"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        },
        {
          "condition": "minecraft:random_chance_with_looting",
          "chance": 0.25,
          "looting_multiplier": 0.01
        }
      ]
    }
  ]
}

## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/resources/data/theancientworld/loot_tables/entities/unicorn.json.txt
- Extracted: 2026-05-18
- Category: github-code
