# DirtGolemModel.java

Source: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/dirt_golem/DirtGolemModel.java.txt

Category: [[github-code]]

## Summary
package com.gonhog.theancientworld.entities.dirt_golem; import com.gonhog.theancientworld.TheAncientWorld; import net.minecraft.util.ResourceLocation; import software.bernie.geckolib3.core.event.predicate.AnimationEvent; import software.bernie.geckolib3.core.processor.IBone; import software.bernie.geckolib3.model.AnimatedGeoModel; import software.bernie.geckolib3.model.provider.data.EntityModelData; import javax.annotation.Nullable;

## Full Content
package com.gonhog.theancientworld.entities.dirt_golem;

import com.gonhog.theancientworld.TheAncientWorld;
import net.minecraft.util.ResourceLocation;
import software.bernie.geckolib3.core.event.predicate.AnimationEvent;
import software.bernie.geckolib3.core.processor.IBone;
import software.bernie.geckolib3.model.AnimatedGeoModel;
import software.bernie.geckolib3.model.provider.data.EntityModelData;

import javax.annotation.Nullable;

public class DirtGolemModel extends AnimatedGeoModel<DirtGolemEntity> {

    @Override
    public ResourceLocation getModelLocation(DirtGolemEntity entity)
    {
        return new ResourceLocation(TheAncientWorld.MOD_ID, "geo/dirt_golem.geo.json");
    }

    @Nullable
    @Override
    public ResourceLocation getTextureLocation(DirtGolemEntity entity) {
        return new ResourceLocation(TheAncientWorld.MOD_ID, "textures/entities/dirt_golem.png");
    }

    @Override
    public ResourceLocation getAnimationFileLocation(DirtGolemEntity object)
    {
        return new ResourceLocation(TheAncientWorld.MOD_ID, "animations/dirt_golem_animation.json");
    }

    @Override
    public void setLivingAnimations(DirtGolemEntity entity, Integer uniqueID, AnimationEvent customPredicate)
    {
        super.setLivingAnimations(entity, uniqueID, customPredicate);
        IBone head = this.getAnimationProcessor().getBone("head");
        EntityModelData extraData = (EntityModelData) customPredicate.getExtraDataOfType(EntityModelData.class).get(0);
        head.setRotationX(extraData.headPitch * (0.014F));
        head.setRotationY(extraData.netHeadYaw * (0.014F));

    }
}


## Metadata
- Source file: junk_drawer/github/TheAncientWorld/src/main/java/com/gonhog/theancientworld/entities/dirt_golem/DirtGolemModel.java.txt
- Extracted: 2026-05-18
- Category: github-code
