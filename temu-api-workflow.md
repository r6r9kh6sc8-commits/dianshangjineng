# TEMU Open API workflow

Confirm names and parameters against the current official Partner documentation before a live call. API contracts can change.

## Signing

For a request map containing `app_key`, `access_token`, `type`, `timestamp`, and business parameters:

1. Remove `sign` and omit parameters whose value is `null`.
2. Sort parameter names by their string key.
3. Serialize object or array values as compact UTF-8 JSON with stable key order.
4. Concatenate `app_secret + key1 + value1 + ... + app_secret`.
5. Compute uppercase MD5 hex and send it as `sign`.

Use the signing method shown by the current official documentation if it differs from this reference.

## Discovery order

| Purpose | API | Parameter detail |
|---|---|---|
| Validate token/shop | `bg.open.accesstoken.info.get.global` | Use current access token |
| Match category | `bg.glo.goods.category.match` | `searchText` |
| Category attributes | `bg.glo.goods.attrs.get` | resolved category ID |
| Parent specifications | `bg.glo.goods.parentspec.get` | resolved category ID |
| Create specification | `bg.glo.goods.spec.create` | only when supported by evidence |
| Warehouses | `bg.btg.goods.stock.warehouse.list.get` | `siteIdList`, not `siteIds` |
| Freight templates | `bg.glo.logistics.template.get` | `siteIds`, not `siteIdList` |
| Upload image | `bg.goods.image.upload.global` | current documented image field |
| Create product | `bg.glo.goods.add` | fully validated listing payload |
| Verify list status | `bg.glo.goods.list.get` | product/SKC identifiers |
| Verify details | `bg.glo.goods.detail.get` | returned product identifier |
| Reconcile/search | `bg.glo.product.search` | stable external code when supported |

## Common failures

- Empty warehouse/template lists often mean the wrong plural parameter name or wrong site ID.
- Attribute validation failures often come from a value copied from another category or shop.
- Specification failures often mean the custom property object is incomplete or a parent spec ID is stale.
- Error `2000306` in detail content commonly indicates missing width or height on a layer-decoration image.
- A successful create response does not prove the product is live. Query the product and report the verified `skcTopStatus`.
- A network failure after submission is an uncertain outcome. Reconcile before retrying.

