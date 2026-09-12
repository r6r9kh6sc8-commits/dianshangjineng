# TEMUzuotu 图片角色与提示词模板

生成套图前阅读此文件。先填充已确认事实，再将共享约束与对应角色合并为一条独立提示词，每张图片单独调用内置图片生成。以下花括号是任务填写字段；缺少事实时省略相关卖点，不输出花括号或编造内容。

## 共享约束模板

```text
Use case: product-mockup / ads-marketing as appropriate.
Asset: ONE US-market children's toy ecommerce image.
Reference inputs: {identify each product reference explicitly}.
Product facts: {confirmed product, actual colors, shapes, translucency,
construction system, included parts and accessories}.
Inventory: {category-by-category quantities, confirmed total}.
Dimensions: {verified product measurements and measured object, if relevant}.
Format: exactly 1:1 square; prefer 2000 x 2000 px if supported.
Scene: one continuous {original setting}, with consistent perspective and lighting.
Composition: product visually dominant, about 70% of frame, complete and unobstructed.
Visual direction: {shared palette, lighting, photography style and typography}.
Preserve the reference product's real shapes, materials, proportions and connections.
Use only confirmed parts; keep all depicted quantities within the actual inventory.
No collage, split screen, grid, inset, card panels, extra accessories,
copied packaging, logos, watermarks, unsupported claims or internally glowing plastic.
Copy: short English text specified below; do not invent extra text.
```

不要把同一套人物或动作作为风格统一条件。共享的是色彩、光线、文字排版风格和真实产品，不是人物身份。

## 01 — Hero

```text
Create a photorealistic hero image of {confirmed toy/build} in {original setting}.
Exactly one white adult {appearance/clothing} and one white child
{distinct appearance/clothing}, interacting naturally: {supported play action}.
People are secondary behind or beside the toy, with hands clear of key structures.
Keep believable scale. Show the entire toy with breathing room on every edge.
Only confirmed accessories, at most {confirmed quantities}.
Text, verbatim: "{short supported headline}".
Optional subline: "{confirmed product description or total}".
```

选择参考已展示的玩法，例如搭建或滚珠，不添加参考未支持的电子、遥控等功能。

## 02 — Lifestyle

```text
Create a second photorealistic parent-child scene with {confirmed toy}.
Exactly one white adult {identity visibly different from 01} and one white child
{identity visibly different from 01}, in {different original setting}.
Action: {different supported interaction}.
Use different faces, age appearance, hair, clothing, poses and actions from image 01.
Keep toy dominant and unobstructed, natural hands and believable scale.
Use only the real included parts and accessories.
Text, verbatim: "{short supported lifestyle headline}".
```

记录 01 的人物设计再选择 02，避免只换背景而复制同一组人物。

## 03 — Multiple Builds

```text
Product-only photograph: three distinct physically plausible builds of {toy}
naturally positioned on ONE continuous {surface}, same camera and shadows.
Build A: {structure and part allocation}.
Build B: {structure and part allocation}.
Build C: {structure and part allocation}.
The three combined use no more than {inventory per category}; do not duplicate kits.
Use only reference-confirmed parts and connection methods, with structural support.
No people, hands, collage, grid, dividers, inset windows or separate scene panels.
All three builds fully visible and together occupy about 70% of frame.
Text, verbatim: "{short headline}".
```

先核算三种搭建各类零件用量。产品不支持重组或只有一种固定形态时，不虚构三种形态；说明限制并向用户确认替代角色，继续其他独立图片。

## 04 — What's Included

```text
Product-only contents photograph on one continuous {neutral surface}.
Arrange ALL actual included parts in naturally staggered, clearly separated groups,
without a grid or cards. Use shallow fans or separated pieces so counts are inspectable.
Exact groups and labels: {English category names × exact quantities}.
Headline: "What's Included".
Total: "{confirmed N} Pieces".
Render exactly the labeled number of real objects in each group.
No extra assembled model that duplicates the displayed inventory.
No people, hands, packaging, props or unconfirmed accessories.
Preserve exact opening shapes, connector details, colors and translucency.
```

逐项看图计数；不能用标签代替视觉核验。白色实体嵌片与空心孔位不可混淆。无法看清或稳定还原时保留为草稿，说明缺陷。

## 05 — Dimensions

```text
Product-only dimension image on one continuous {neutral studio surface}.
Show {exact measured product/part} matching the reference.
Measurement arrows point precisely to {verified measured edges}.
Exact labels: "{cm value} cm ({converted in value} in)" for each confirmed measurement.
Headline: "{short dimension headline}".
Preserve the real shape and proportions; no inferred dimensions.
No people, hands, packaging, shipping measurements, collage or inset panel.
```

先计算单位换算再提交提示词。若只有包装尺寸，不能生成产品尺寸图或悄悄改为包装图；向用户索取产品实测数据。尺寸待补不阻止其他有充分资料的图片。

## 06 — Features

```text
One continuous product-only close-up of {genuine feature/connection/mechanism}.
Show {reference-confirmed assembly} with visible {real detail}.
Use normal reflections and translucency; no internal light source.
Keep accurate joints, openings and proportions. No invented screws, magnets,
cutaway internals, accessories, arrows implying unsupported action, or mechanisms.
No people, hands, collage or inset zoom windows.
Text, verbatim: "{short factual feature headline}".
Optional subline: "{reference-supported material appearance or mechanism}".
```

只选择有图像依据的特征，例如半透明片、磁力边缘或轨道连接；不得从玩具类别推断认证、教育成效或安全保证。

