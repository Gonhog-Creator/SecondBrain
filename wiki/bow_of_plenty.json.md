# bow_of_plenty.json

Source: junk_drawer/github/TheAncientWorld/src/main/resources/assets/theancientworld/models/item/bow_of_plenty.json.txt

Category: [[github-code]]

## Summary
{ "parent": "item/handheld", "textures": { "layer0": "theancientworld:items/bow_of_plenty" }, "overrides": [ { "predicate": { "theancientworld:bow_of_plenty_pulling": 1 },

## Full Content
{
  "parent": "item/handheld",
  "textures": {
    "layer0": "theancientworld:items/bow_of_plenty"
  },
  "overrides": [
    {
      "predicate": {
        "theancientworld:bow_of_plenty_pulling": 1
      },
      "model": "theancientworld:item/bow_of_plenty_pulling_1"
    },
    {
      "predicate": {
        "theancientworld:bow_of_plenty_pulling": 1,
        "theancientworld:bow_of_plenty_pull": 0.65
      },
      "model": "theancientworld:item/bow_of_plenty_pulling_2"
    },
    {
      "predicate": {
        "theancientworld:bow_of_plenty_pulling": 1,
        "theancientworld:bow_of_plenty_pull": 0.9
      },
      "model": "theancientworld:item/bow_of_plenty_pulling_3"
    }
  ]
}

## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/resources/assets/theancientworld/models/item/bow_of_plenty.json.txt
- Extracted: 2026-05-18
- Category: github-code
