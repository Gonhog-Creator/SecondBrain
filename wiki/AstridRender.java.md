# AstridRender.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/astrid/AstridRender.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.entities.astrid; import net.minecraft.client.renderer.entity.EntityRendererManager; import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer; public class AstridRender extends GeoEntityRenderer<AstridEntity> { public AstridRender(EntityRendererManager renderManager) { super(renderManager, new AstridModel()); this.shadowSize = .2F;

## Full Content
package com.gonhog.theancientworld.entities.astrid;

import net.minecraft.client.renderer.entity.EntityRendererManager;
import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer;

public class AstridRender extends GeoEntityRenderer<AstridEntity> {
    public AstridRender(EntityRendererManager renderManager)
    {
        super(renderManager, new AstridModel());
        this.shadowSize = .2F;
    }
}


## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/astrid/AstridRender.java.txt
- Extracted: 2026-05-18
- Category: github-code
