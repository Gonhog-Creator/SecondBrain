# CustomMeat.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/items/CustomMeat.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.items; import com.gonhog.theancientworld.TheAncientWorld; import net.minecraft.item.Food; import net.minecraft.item.Item; import net.minecraft.potion.EffectInstance; import net.minecraft.potion.Effects; public class CustomMeat extends Item { public CustomMeat() {

## Full Content
package com.gonhog.theancientworld.items;

import com.gonhog.theancientworld.TheAncientWorld;
import net.minecraft.item.Food;
import net.minecraft.item.Item;
import net.minecraft.potion.EffectInstance;
import net.minecraft.potion.Effects;

public class CustomMeat extends Item {
    public CustomMeat() {
        super(new Item.Properties()
                .group(TheAncientWorld.TAB)
                .food(new Food.Builder()
                        .hunger(4)
                        .meat()
                        .saturation(4)
                        .build())
        );
    }
}


## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/items/CustomMeat.java.txt
- Extracted: 2026-05-18
- Category: github-code
