# CentaurRender.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/centaur/CentaurRender.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.entities.centaur; import net.minecraft.client.renderer.entity.EntityRendererManager; import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer; public class CentaurRender extends GeoEntityRenderer<CentaurEntity> { public CentaurRender(EntityRendererManager renderManager) { super(renderManager, new CentaurModel());

## Full Content
package com.gonhog.theancientworld.entities.centaur;

import net.minecraft.client.renderer.entity.EntityRendererManager;
import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer;

public class CentaurRender extends GeoEntityRenderer<CentaurEntity>
{
    public CentaurRender(EntityRendererManager renderManager)
    {
        super(renderManager, new CentaurModel());
        this.shadowSize = .7F;
    }
}


## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/centaur/CentaurRender.java.txt
- Extracted: 2026-05-18
- Category: github-code
