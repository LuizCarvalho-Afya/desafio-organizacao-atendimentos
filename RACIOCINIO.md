# RACIOCÍNIO DA SOLUÇÃO

# Parte 1 — Modelagem do problema

## 1. Classificação do problema

Classifiquei esse problema como escalonamento e otimização de recursos.

O objetivo é organizar atendimentos sem conflito de horários utilizando o menor número possível de consultórios, além de priorizar atendimentos expressos.


## 2. Semelhança com problemas clássicos

O problema é parecido com o Interval Scheduling.

Cada atendimento representa um intervalo de tempo e cada consultório funciona como um recurso disponível para receber esses intervalos sem sobreposição.


## 3. Estruturas de dados utilizadas

Utilizei classes para representar atendimentos e consultórios.

Também utilizei listas para armazenar os dados, pois facilitam a ordenação e o percurso dos atendimentos durante a organização.

# Parte 2 — Estratégia algorítmica

## 4. Descrição do algoritmo

1. Os atendimentos são ordenados priorizando expressos e horários menores.

2. O sistema percorre cada atendimento.

3. O algoritmo tenta encaixar o atendimento em um consultório já existente.

4. Caso não seja possível, um novo consultório é criado.


## 5. Tipo de abordagem utilizada

A solução utiliza abordagem gulosa (greedy).

O algoritmo tenta reutilizar o primeiro consultório disponível encontrado, buscando uma solução simples e eficiente.


## 6. Limitações da solução

Em alguns casos, a solução pode criar mais consultórios do que o necessário, pois o algoritmo toma decisões imediatas sem analisar todas as combinações possíveis.


## 7. Complexidade da solução

A complexidade aproximada é O(n²), pois para cada atendimento o algoritmo pode percorrer todos os consultórios existentes.


# Parte 3 — Decisões de implementação

## 8. Como o sistema decide quantos consultórios abrir?

O sistema cria um novo consultório apenas quando nenhum consultório existente consegue receber o atendimento sem conflito de horário.


## 9. Tratamento dos atendimentos expressos

Os atendimentos expressos recebem prioridade durante a ordenação inicial, ficando na frente dos atendimentos normais.


## 10. Parte mais inteligente da solução

A parte principal da solução é a verificação de conflito de horários:

```python id="vyff6q"
return atendimento.inicio >= ultimo.fim
```

Essa lógica impede que dois atendimentos ocupem o mesmo consultório ao mesmo tempo.

## 11. Parte que pode ser melhorada

A organização dos horários poderia ser otimizada utilizando estruturas mais avançadas para melhorar o desempenho em cenários maiores.

## 12. Considerações finais

Busquei criar uma solução simples, organizada e fácil de explicar, além de implementar uma interface gráfica utilizando Tkinter para melhorar a visualização do sistema.
