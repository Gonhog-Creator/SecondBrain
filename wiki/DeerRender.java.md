# DeerRender.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/deer/DeerRender.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.entities.deer; import com.gonhog.theancientworld.entities.astrid.AstridModel; import net.minecraft.client.renderer.entity.EntityRendererManager; import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer; public class DeerRender extends GeoEntityRenderer<DeerEntity> { public DeerRender(EntityRendererManager renderManager) { super(renderManager, new DeerModel());

## Full Content
package com.gonhog.theancientworld.entities.deer;

import com.gonhog.theancientworld.entities.astrid.AstridModel;
import net.minecraft.client.renderer.entity.EntityRendererManager;
import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer;

public class DeerRender extends GeoEntityRenderer<DeerEntity> {
    public DeerRender(EntityRendererManager renderManager)
    {
        super(renderManager, new DeerModel());
        this.shadowSize = .8F;
    }
}


## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/deer/DeerRender.java.txt
- Extracted: 2026-05-18
- Category: github-code
