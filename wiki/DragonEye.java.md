# DragonEye.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/items/DragonEye.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.items; import com.gonhog.theancientworld.TheAncientWorld; import com.gonhog.theancientworld.events.ClientEventHandler; import com.gonhog.theancientworld.items.potionRings.PotionRingEffectHandler; import com.gonhog.theancientworld.util.RegistryHandler; import net.minecraft.entity.Entity; import net.minecraft.entity.player.PlayerEntity; import net.minecraft.item.Item; import net.minecraft.item.ItemStack;

## Full Content
package com.gonhog.theancientworld.items;

import com.gonhog.theancientworld.TheAncientWorld;
import com.gonhog.theancientworld.events.ClientEventHandler;
import com.gonhog.theancientworld.items.potionRings.PotionRingEffectHandler;
import com.gonhog.theancientworld.util.RegistryHandler;
import net.minecraft.entity.Entity;
import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.potion.EffectInstance;
import net.minecraft.potion.Effects;
import net.minecraft.world.World;

public class DragonEye extends Item {

    public DragonEye(Properties properties) {
        super(new Item.Properties()
                .maxStackSize(1)
                .group(TheAncientWorld.TAB)
        );
    }

    //Gives the player fire resistance effect if the item is equipped
    @Override
    public void inventoryTick(ItemStack itemStack, World world, Entity entity, int i, boolean flag) {
        ItemStack eyeEquipped = PotionRingEffectHandler.getEquippedCurios(stack -> stack.getItem() == RegistryHandler.DRAGON_EYE.get(), (PlayerEntity) entity);
        if (!world.isRemote) {
            if (!eyeEquipped.isEmpty()) {
                ((PlayerEntity) entity).addPotionEffect(new EffectInstance(Effects.FIRE_RESISTANCE, 5, 1, true, true));
            }
        }
    }
}


## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/items/DragonEye.java.txt
- Extracted: 2026-05-18
- Category: github-code
