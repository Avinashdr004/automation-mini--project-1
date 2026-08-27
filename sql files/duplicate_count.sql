select count(*) from (
select customer_id from kalaburgi_store.curated_zone.curated_customer 
group by customer_id having count(*)>1);