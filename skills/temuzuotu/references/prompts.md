# Ecommerce Image Prompt Templates

Replace bracketed fields only with facts supported by the user's reference.

## Shared prompt block
```text
Use the attached image only as a product reference. Preserve the real [PRODUCT], including exact shapes, colors, materials, proportions, connection system, included accessories and quantities.

Create an EXACT 1:1 square US Amazon/TEMU ecommerce image. The product occupies approximately 70% of the frame. Use one continuous scene only.

Do not copy the reference background, logo, brand or packaging. No collage, split screen, grid, inset panel, watermark, invented accessory, unsupported claim or incorrect quantity. Use short English copy only. Show dimensions in both centimeters and inches.
```

## 1. Hero image
```text
Use case: product-mockup
Asset type: square ecommerce hero image
Scene: an original bright family playroom appropriate to [PRODUCT].
Subject: one Caucasian adult parent and one Caucasian child actively using [PRODUCT] together. Give them natural expressions, believable hands, and realistic scale. The product is complete, dominant and unobstructed.
Composition: exact 1:1 square; product about 70% of frame; people secondary.
Text (verbatim): "[PIECE COUNT] PCS"
[SHARED PROMPT BLOCK]
```

## 2. Parent-child lifestyle image
```text
Use case: photorealistic-natural
Asset type: square family lifestyle ecommerce image
Scene: a different original family activity setting.
Subject: a different Caucasian adult and Caucasian child collaboratively using [PRODUCT]. Change faces, ages, hairstyles, clothing, body positions and actions from the hero image.
Composition: exact 1:1 square; product about 70%; product clearly visible.
Text (verbatim): "CREATE TOGETHER"
[SHARED PROMPT BLOCK]
```

## 3. Multiple-build image
```text
Use case: ads-marketing
Asset type: square multiple-build ecommerce image
Subject: NO PEOPLE. Show three physically coherent builds made only from the referenced parts, arranged in one continuous tabletop scene. Use different forms appropriate to the product and a small number of real loose pieces.
Text (verbatim): "BUILD IT YOUR WAY" and "MULTIPLE BUILD IDEAS"
[SHARED PROMPT BLOCK]
```

## 4. Contents image
```text
Use case: infographic-diagram
Asset type: square exact-contents ecommerce image
Subject: NO PEOPLE. Arrange every included part into clearly separated groups. Label each group with its exact name and quantity. The displayed quantities must total exactly [PIECE COUNT].
Text (verbatim): "WHAT'S INCLUDED", "[PIECE COUNT] PCS", and the verified part labels.
[SHARED PROMPT BLOCK]
```

## 5. Dimensions image
```text
Use case: infographic-diagram
Asset type: square product-dimensions ecommerce image
Subject: NO PEOPLE. Show the relevant product or component clearly with one clean dimension arrow. Do not include package or carton dimensions unless explicitly requested.
Text (verbatim): "[SIZE HEADING]" and "[CM VALUE] cm ([IN VALUE] in)"
[SHARED PROMPT BLOCK]
```

## 6. Feature image
```text
Use case: product-mockup
Asset type: square product-feature ecommerce image
Subject: NO PEOPLE. Show a close, accurate view of genuine product materials, connections or mechanisms, with a completed product example behind it. Highlight only features supported by the reference.
Text (verbatim): "[SHORT FEATURE HEADLINE]"
[SHARED PROMPT BLOCK]
```

## Filename convention
```text
01_hero.png
02_parent_child_lifestyle.png
03_multiple_builds.png
04_whats_included.png
05_dimensions.png
06_product_features.png
```
