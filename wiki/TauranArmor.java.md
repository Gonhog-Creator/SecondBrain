# TauranArmor.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/armor/TauranArmor.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.armor; import com.gonhog.theancientworld.TheAncientWorld; import net.minecraft.inventory.EquipmentSlotType; import net.minecraft.item.ArmorItem; import net.minecraft.item.IArmorMaterial; import net.minecraft.item.Item; import javax.swing.plaf.TableHeaderUI;

## Full Content
package com.gonhog.theancientworld.armor;

import com.gonhog.theancientworld.TheAncientWorld;
import net.minecraft.inventory.EquipmentSlotType;
import net.minecraft.item.ArmorItem;
import net.minecraft.item.IArmorMaterial;
import net.minecraft.item.Item;

import javax.swing.plaf.TableHeaderUI;

public class TauranArmor extends ArmorItem {
    public TauranArmor( EquipmentSlotType slot) {
        super(ModArmorBase.TAURAN, slot, new Item.Properties().group(TheAncientWorld.TAB).maxStackSize(1));
    }
}


## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/armor/TauranArmor.java.txt
- Extracted: 2026-05-18
- Category: github-code
