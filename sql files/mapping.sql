select count(*) from (
select customer_id from kalaburgi_store.curated_zone.curated_customer 
minus
select customer_id from kalaburgi_store.landing_zone.landing_customer );