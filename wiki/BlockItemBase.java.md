# BlockItemBase.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/blocks/BlockItemBase.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.blocks; import com.gonhog.theancientworld.TheAncientWorld; import net.minecraft.block.Block; import net.minecraft.item.BlockItem; public class BlockItemBase extends BlockItem { public BlockItemBase(Block blockIn) { super(blockIn, new Properties().group(TheAncientWorld.TAB)); }

## Full Content
package com.gonhog.theancientworld.blocks;

import com.gonhog.theancientworld.TheAncientWorld;
import net.minecraft.block.Block;
import net.minecraft.item.BlockItem;

public class BlockItemBase extends BlockItem {
    public BlockItemBase(Block blockIn) {
        super(blockIn, new Properties().group(TheAncientWorld.TAB));
    }
}


## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/blocks/BlockItemBase.java.txt
- Extracted: 2026-05-18
- Category: github-code
