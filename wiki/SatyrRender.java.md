# SatyrRender.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/satyr/SatyrRender.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.entities.satyr; import net.minecraft.client.renderer.entity.EntityRendererManager; import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer; public class SatyrRender extends GeoEntityRenderer<SatyrEntity> { public SatyrRender(EntityRendererManager renderManager) { super(renderManager, new SatyrModel());

## Full Content
package com.gonhog.theancientworld.entities.satyr;

import net.minecraft.client.renderer.entity.EntityRendererManager;
import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer;

public class SatyrRender extends GeoEntityRenderer<SatyrEntity>
{
    public SatyrRender(EntityRendererManager renderManager)
    {
        super(renderManager, new SatyrModel());
        this.shadowSize = .5F;
    }
}



## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/satyr/SatyrRender.java.txt
- Extracted: 2026-05-18
- Category: github-code
