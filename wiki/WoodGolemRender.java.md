# WoodGolemRender.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/wood_golem/WoodGolemRender.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.entities.wood_golem; import net.minecraft.client.renderer.entity.EntityRendererManager; import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer; public class WoodGolemRender extends GeoEntityRenderer<WoodGolemEntity> { public WoodGolemRender(EntityRendererManager renderManager) { super(renderManager, new WoodGolemModel());

## Full Content
package com.gonhog.theancientworld.entities.wood_golem;

import net.minecraft.client.renderer.entity.EntityRendererManager;
import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer;

public class WoodGolemRender extends GeoEntityRenderer<WoodGolemEntity> {

    public WoodGolemRender(EntityRendererManager renderManager)
    {
        super(renderManager, new WoodGolemModel());
        this.shadowSize = .9F;
    }
}


## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/wood_golem/WoodGolemRender.java.txt
- Extracted: 2026-05-18
- Category: github-code
