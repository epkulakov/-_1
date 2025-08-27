SELECT 
	payment_id,
	customer_id,
	amount,
	title,
	first_name,
	last_name,
	length, -- Перечесляем нужные столбцы которые должны выводится
	
	CASE  --Создаём условие
	 WHEN amount >= 8.00 THEN 'Дорогая покупка'   --Если покупка дороже 8,00 то это дорогая покупка
	 WHEN amount >= 2.99 THEN 'Покупка с средней ценой'  --Если нет, но покупка дороже 2,99 то это Покупка с средней ценой
	 ELSE 'Дешёвая покупка'  -- А если цена ещё ниже то это Дешёвая покупка
	END level_price,  -- Создаём столбец в который мы будем писать какая это покупка
	MIN(length) OVER (PARTITION BY customer_id) AS min_time,  --Создаём оконую функцию с минимальной продолжительностью фильма
	MAX(length) OVER (PARTITION BY customer_id) AS max_time   --Создаём оконую функцию с максимальной продолжительностью фильма
FROM payment -- Указываем таблицу из которой мы будем брать основные данные

LEFT JOIN film  -- Объединяем таблицы  по потраченой сумме - цена фильма
  ON payment.amount = film.rental_rate  
LEFT JOIN film_actor  -- Объединяем таблицы по id_film - id_fim чтобы сопоставить о получить нужный actor_id
  ON film.film_id = film_actor.film_id
LEFT JOIN actor  -- Объединяем таблицы по actor_id - actor_id и теперь мы знаем фамилию и имя актёра который бфл в фильме
  ON film_actor.actor_id = actor.actor_id
  
ORDER BY payment_id DESC  -- Сортируем данные по столбцу payment_id по убыванию

LIMIT 5000  -- Ставим лимит 5000 строк
