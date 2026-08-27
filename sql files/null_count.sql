select count(*) from (
select customer_id from kalaburgi_store.curated_zone.curated_customer 
where customer_id is null);