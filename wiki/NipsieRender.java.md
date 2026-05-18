# NipsieRender.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/nipsie/NipsieRender.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.entities.nipsie; import com.gonhog.theancientworld.entities.centaur.CentaurEntity; import com.gonhog.theancientworld.entities.centaur.CentaurModel; import net.minecraft.client.renderer.entity.EntityRendererManager; import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer; public class NipsieRender extends GeoEntityRenderer<NipsieEntity> { public NipsieRender(EntityRendererManager renderManager)

## Full Content
package com.gonhog.theancientworld.entities.nipsie;

import com.gonhog.theancientworld.entities.centaur.CentaurEntity;
import com.gonhog.theancientworld.entities.centaur.CentaurModel;
import net.minecraft.client.renderer.entity.EntityRendererManager;
import software.bernie.geckolib3.renderers.geo.GeoEntityRenderer;

public class NipsieRender extends GeoEntityRenderer<NipsieEntity>
{
    public NipsieRender(EntityRendererManager renderManager)
    {
        super(renderManager, new NipsieModel());
        this.shadowSize = .1F;
    }
}



## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/nipsie/NipsieRender.java.txt
- Extracted: 2026-05-18
- Category: github-code
