# UnicornRender.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/unicorn/UnicornRender.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.entities.unicorn; import net.minecraft.client.renderer.entity.EntityRendererManager; import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer; public class UnicornRender extends GeoEntityRenderer<UnicornEntity> { public UnicornRender(EntityRendererManager renderManager) {

## Full Content
package com.gonhog.theancientworld.entities.unicorn;

import net.minecraft.client.renderer.entity.EntityRendererManager;
import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer;


public class UnicornRender extends GeoEntityRenderer<UnicornEntity>
{
    public UnicornRender(EntityRendererManager renderManager)
    {
        super(renderManager, new UnicornModel());
        this.shadowSize = 0.7F;
    }
}


## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/unicorn/UnicornRender.java.txt
- Extracted: 2026-05-18
- Category: github-code
