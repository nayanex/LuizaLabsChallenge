## Consultas da API

1. Solicitar tipos de "channel" distintos existentes a partir de table "interaction"

```sql
SELECT channel FROM public.interaction GROUP BY 1;
```
Result: test, magazine_ecomm, magazine_mobile, magazine_mobile_app, magazine_voce, magazine_mobile_app_test

2. Solicitar tipos de "action existentes a partir de table "interaction"

```sql
SELECT action FROM public.interaction GROUP BY 1;
```
Result: addedtocart, bought, dislikeProduct, likeProduct, viewed

3. Solicitar tipos de "department" existentes a partir de table "interaction" 

```sql
SELECT department FROM public.interaction GROUP BY 1;
```

4. Solicitar quais usuários existem no sistema

```sql
SELECT uid FROM public.interaction GROUP BY 1;
```

5. Consultar produtos que foram "bought", pegar os seguintes dados:

```SQL
SELECT (uid, pid, at) from user_interaction WHERE (action = 'bought')
```

6. Pegar a data em que produtos foram last_viewed antes de "bought"

```SQL
'''
SELECT MIN(at) from user_interaction WHERE (uid = '%s' AND pid = '%s' AND at = '%s' AND action = 'viewed'
''' (user, product, time_of_action)
```

or

```sql
'''
SELECT at FROM user_interaction WHERE (uid = '%s' AND pid = '%s' AND at = '%s' AND action = 'viewed' ORDER BY at DESC LIMIT 1
''' (user, product, time_of_action)
```

Depois acrescente o `last_viewed at` na tabela de "purchase_interval":

```python
'''
INSERT INTO `purchase_interval`(uid, pid, last_viewed_at, bought_at, time_interval) VALUES (%s, %s, %s::timestamp, %s::timestamp, %s::totimestamp - %s::totimestamp)
''' (uid, pid, last_viewed_at, bought_at, bought_at, last_viewed_at)
```

7. Pegar média de tempo que determinado usuário leva para efetuar uma compra desde a última visualização do produto:

```python
'''
SELECT MEDIAN(`time_interval`) FROM `user_interaction` WHERE (uid = '%s') 
''' (user)
```
or

```python
'''
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER by `time_interval`) FROM `user_interaction` WHERE (uid = '%s') 
''' (user)
```

8. Selecionar mediana dos preços do quanto o usuário costuma gastar

```sql
'''
SELECT `price_at` FROM user_interaction
INNER JOIN purchase
ON purchase.pid = user_interaction.pid 
WHERE interaction.uid = purchase.uid AND interaction.action = 'bought'
purchase.uid = user_interaction.uid AND purchase.bought_at = user_interaction.at AND user_interaction = 'bought' AND interaction.at = purchase.bought_at
WHERE purchase.uid = '%s' 
''' (user)
```

tirar mediana dos preços selecionados em Python

Baseado em:

SELECT * FROM Individual
INNER JOIN Publisher
ON Individual.IndividualId = Publisher.IndividualId
WHERE Individual.IndividualId = (SELECT someID FROM table WHERE blahblahblah)


9. Selecionar em qual categoria usuário mais faz compra

```sql
'''
SELECT `category` FROM product
INNER JOIN purchase
ON purchase.pid = user_interaction.pid 
WHERE interaction.uid = purchase.uid AND interaction.action = 'bought'
purchase.uid = user_interaction.uid AND purchase.bought_at = user_interaction.at AND user_interaction = 'bought' AND interaction.at = purchase.bought_at
WHERE purchase.uid = '%s' 
''' (user)
```

10. Selecionar quais são as marcas que ele compra recorrentemente

Depois calcula

11. Tempo de intervalo médio entre horário em que usuário visualizou o produto e o comprou


12. Como preço do produto variou ao longo do tempo







* Faixa de preço que determinado usuário costuma comprar

* Se "addedtocart" aumentaram ou diminuiram ao longo do tempo
* Se "viewed" aumentaram ou diminuiram ao longo do tempo
* Qual é a faixa de preço que as pessoas mais "addedtocart" por "departamento"

* Qual é o canal de compra que determinado usuário usa mais?
	- table: usuário | canal

* Qual é o canal de compra mais utilizado, baseado no passo anterior - Ordem hierarquica de canais mais utilizados, 
	- canais | número de usuários
* Quais são as categorias de produtos existentes
* Quais são os departamentos existentes
* Que categorias de produtos são vendidos por departamento
* Marcas de produto por categoria
* Produtos mais vistos por usuário
* Produtos mais adicionados ao cart por usuário
* Produtos mais adicionados ao cart em determinado intervalo de tempo
* Produtos mais vistos em determinado intervalo de tempo e sua categoria e departamento
* Produtos com melhor rating -categoria - departamento - marca
* Quais as marcas mais bem avaliadas?
* Com que frequência o usuário "addedtocart"
	- user | product | at
* Com que frequência o usuário "viewed"
	- user | product | at
* Faixa de preçco que determinado usuário mais compra
* Quais marcas são mais compradas por categoria
* Tipo de produto que usuário mais compra por categoria - ranking
* Talvez perceber renda do cliente por meio do que ele compra, se ele compra muito ele deve ter renda maior.
* Qual é o horário(intervalo de tempo em horas, ex.: entre 21 e 22h) em que as pessoas mais fazem compras em determinado canal e dia(por canal)?
