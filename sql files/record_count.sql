select 
(select count(*) from kalaburgi_store.landing_zone.landing_customer) as source_count,
(select count(*) from kalaburgi_store.curated_zone.curated_customer)as target_count;
