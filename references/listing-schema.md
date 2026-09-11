# Listing package schema

Create a UTF-8 JSON package for each workbook row. Keep the original cell name and normalized value when names differ.

## Source facts

- `source.workbook`: workbook name and sheet name
- `source.row`: one-based worksheet row
- `source.images`: extracted reference-image paths
- `product.source_title`: original title
- `product.source_description`: original description
- `product.material`: exact stated material
- `product.quantity`: package quantity
- `product.age_range`: stated age range
- `product.battery`: required, included, and battery chemistry when stated
- `product.brand`: brand or unbranded status only when stated
- `product.origin`: country and region stated by the user or workbook
- `package.length_mm`, `width_mm`, `height_mm`, `weight_mg`
- `commercial.currency`, `supply_price_minor`, `inventory`
- `shipping.lead_time_days`, `warehouse_name`, `freight_template_name`
- `safety`: choking-hazard, chemical, magnetic, food-contact, and other sensitive facts when stated

Do not convert an uncertain value into a definite statement. Keep it null and report it as missing.

## Generated listing fields

- `generated.title_en`: evidence-based English title
- `generated.sku`: compact stable SKU
- `generated.images`: final image paths, dimensions, MIME types, sizes, and upload URLs
- `taxonomy.category_path`: resolved category IDs and names
- `taxonomy.attributes`: required and optional attribute selections with source evidence
- `specifications`: resolved parent and child specification IDs
- `shop.site_id`, `warehouse_id`, `freight_template_id`: current shop-specific IDs
- `submission.external_code`: stable idempotency/reconciliation key
- `submission.product_id`, `skc_id`, `status`, `verified_at`

## Evidence rules

For each claim that TEMU displays to buyers, record one of: workbook cell, visible image evidence, user-provided fact, or official API dictionary value. A model inference is not sufficient evidence for material, size, quantity, age, battery, safety, certification, or brand.

