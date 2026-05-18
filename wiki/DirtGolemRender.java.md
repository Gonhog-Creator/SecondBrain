# DirtGolemRender.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/dirt_golem/DirtGolemRender.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.entities.dirt_golem; import com.gonhog.theancientworld.entities.nipsie.NipsieModel; import net.minecraft.client.renderer.entity.EntityRendererManager; import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer; public class DirtGolemRender extends GeoEntityRenderer<DirtGolemEntity> { public DirtGolemRender(EntityRendererManager renderManager) {

## Full Content
package com.gonhog.theancientworld.entities.dirt_golem;

import com.gonhog.theancientworld.entities.nipsie.NipsieModel;
import net.minecraft.client.renderer.entity.EntityRendererManager;
import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer;

public class DirtGolemRender extends GeoEntityRenderer<DirtGolemEntity> {

    public DirtGolemRender(EntityRendererManager renderManager)
    {
        super(renderManager, new DirtGolemModel());
        this.shadowSize = 1F;
    }
}


## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/dirt_golem/DirtGolemRender.java.txt
- Extracted: 2026-05-18
- Category: github-code
