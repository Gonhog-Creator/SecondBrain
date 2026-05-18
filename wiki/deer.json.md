# deer.json

Source: junk_drawer/github/TheAncientWorld/src/main/resources/data/theancientworld/loot_tables/entities/deer.json.txt

Category: [[github-code]]

## Summary
{ "type" : "minecraft:entity", "pools": [ { "rolls": { "min": 1, "max": 3 }, "entries": [ {

## Full Content
{
  "type" : "minecraft:entity",
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "theancientworld:raw_venison",
          "functions": [
            {
              "function": "minecraft:looting_enchant",
              "count": {
                "min": 0,
                "max": 1
              },
              "limit": 1
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 0,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "theancientworld:deer_antler",
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{isMale:isMale}"
              }
            }
          ]
        }
      ]
    }
  ]
}

## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/resources/data/theancientworld/loot_tables/entities/deer.json.txt
- Extracted: 2026-05-18
- Category: github-code
