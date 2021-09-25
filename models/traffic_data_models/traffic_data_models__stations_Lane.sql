
-- Use the `ref` function to select from other models

select *
from {{ ref('traffic_data_models__stations') }}
where Lanes = 2