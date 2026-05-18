# QuickHitArrowRender.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/quick_hit_arrow/QuickHitArrowRender.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.entities.quick_hit_arrow; import com.gonhog.theancientworld.TheAncientWorld; import net.minecraft.client.renderer.entity.ArrowRenderer; import net.minecraft.client.renderer.entity.EntityRendererManager; import net.minecraft.util.ResourceLocation; public class QuickHitArrowRender extends ArrowRenderer<QuickHitArrowEntity> { private static final ResourceLocation QUICK_HIT_ARROW_TEXTURE = new ResourceLocation(TheAncientWorld.MOD_ID,

## Full Content
package com.gonhog.theancientworld.entities.quick_hit_arrow;

import com.gonhog.theancientworld.TheAncientWorld;
import net.minecraft.client.renderer.entity.ArrowRenderer;
import net.minecraft.client.renderer.entity.EntityRendererManager;
import net.minecraft.util.ResourceLocation;

public class QuickHitArrowRender extends ArrowRenderer<QuickHitArrowEntity> {

    private static final ResourceLocation QUICK_HIT_ARROW_TEXTURE = new ResourceLocation(TheAncientWorld.MOD_ID,
            "textures/entities/projectiles/quick_hit_arrow.png");

    public QuickHitArrowRender(EntityRendererManager renderManagerIn) {
        super(renderManagerIn);
    }

    @Override
    public ResourceLocation getEntityTexture(QuickHitArrowEntity entity) {
        return QUICK_HIT_ARROW_TEXTURE;
    }
}


## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/quick_hit_arrow/QuickHitArrowRender.java.txt
- Extracted: 2026-05-18
- Category: github-code
