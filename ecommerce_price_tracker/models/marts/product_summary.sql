with base as (
  select * from {{ ref('stg_transformed_data') }}
),

avg_price as (
  select * from {{ ref('stg_avg_brand_price') }}
)

select
  base.*,
  avg_price.final_price as avg_final_price,
  case
    when base.final_price < avg_price.final_price then true
    else false
  end as is_below_brand_avg,
  case
    when base.rating >= 4.0 then true
    else false
  end as is_high_rated
from base
left join avg_price
  on base.brand = avg_price.brand
