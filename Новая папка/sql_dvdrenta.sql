SELECT 
	payment_id,
	customer_id,
	amount,
	title,
	first_name,
	last_name,
	length,
	
	CASE
	 WHEN amount >= 8.00 THEN 'Дорогая покупка'
	 WHEN amount >= 2.99 THEN 'Покупка с средней ценой'
	 ELSE 'Дешёвая покупка'
	END level_price,
	MIN(length) OVER (PARTITION BY customer_id) AS min_time,
	MAX(length) OVER (PARTITION BY customer_id) AS max_time
FROM payment

LEFT JOIN film
  ON payment.amount = film.rental_rate
LEFT JOIN film_actor
  ON film.film_id = film_actor.film_id
LEFT JOIN actor
  ON film_actor.actor_id = actor.actor_id
ORDER BY payment_id DESC

LIMIT 5000
