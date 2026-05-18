# CookedCustomMeat.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/items/CookedCustomMeat.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.items; import com.gonhog.theancientworld.TheAncientWorld; import net.minecraft.item.Food; import net.minecraft.item.Item; public class CookedCustomMeat extends Item { public CookedCustomMeat() { super(new Item.Properties() .group(TheAncientWorld.TAB)

## Full Content
package com.gonhog.theancientworld.items;

import com.gonhog.theancientworld.TheAncientWorld;
import net.minecraft.item.Food;
import net.minecraft.item.Item;

public class CookedCustomMeat extends Item {
    public CookedCustomMeat() {
        super(new Item.Properties()
                .group(TheAncientWorld.TAB)
                .food(new Food.Builder()
                        .hunger(8)
                        .meat()
                        .saturation(8)
                        .build())
        );
    }
}


## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/items/CookedCustomMeat.java.txt
- Extracted: 2026-05-18
- Category: github-code
