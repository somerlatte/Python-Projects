Este coding challenge requer que você escreva uma função que aplique diferentes descontos a uma lista de preços de produtos. A função deve receber uma lista de inteiros, que representam os preços de vários produtos no carrinho de compras de um usuário. A função deve aplicar descontos em produtos. Seguindo as regras detalhadas abaixo:



Um desconto de $10 está disponível para todos os produtos que tem preço original superior a $100.

Um desconto de $30 está disponível para todos os produtos de um carrinho de compras superior a $1000. 

Os descontos não podem ser aplicados simultaneamente. Ou seja, caso um produto tenha se qualificado para o desconto de $10, e o carrinho ainda assim exceda $1000, o desconto aplicado deve ser de $30.

A aplicação de desconto deve se atentar para a regra de preço mínimo dos produtos: quando um desconto é aplicado, o produto deve ser vendido por no mínimo $10. Ou seja, caso um produto de $20 se qualifique para o desconto de $30, o preço final do produto deve ser $10 (preço mínimo).


A função deve retornar uma string representando a fórmula utilizada para calcular o preço do carrinho de compras do cliente. Os preços dos produtos na fórmula devem estar organizados em ordem ascendente. Todos os valores devem estar precedidos de pelo símbolo "$". Os preços dos produtos devem estar separados pelo símbolo "+", e ao final da string, o preço total do carrinho deve ser exibido precedido do símbolo "=". Todos os valores devem ser inteiros.



Disclaimer: Em algumas linguagens, o tipo de retorno da função original deve ser alterado para String. Certifique-se de alterar o tipo de retorno para String ao escrever a sua solução.


Entrada: [30, 500, 1200, 100, 800, 150]

Saída: $10 + $70 + $120 + $470 + $770 + $1170 = $2610

- Aplicar regra de -$10 de desconto aos preços que se qualificam:
	[30, 490, 1190, 100, 790, 140]

- Preço total do carrinho:
	2740

- Aplicar regra de -$30 de desconto aos preços originais:
	[10, 470, 1170, 70, 770, 120]

- Preço total do carrinho:
	2610

- Organizar os preços com desconto aplicado em ordem ascendente:
	[10, 70, 120, 470, 770, 1170]

- Saída:
	$10 + $70 + $120 + $470 + $770 + $1170 = $2610

Examples

Input: [128]

Output: $118 = $118Input: [566, 50, 458, 128, 20]

Output: $10 + $20 + $98 + $428 + $536 = $1092
