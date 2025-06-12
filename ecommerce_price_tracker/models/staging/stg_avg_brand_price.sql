select
  brand,
  cast(final_price as float64) as final_price
from {{ source('ecommerce', 'brand_avg_price') }}
