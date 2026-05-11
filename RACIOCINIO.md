# RACIOCINIO.md

# Parte 1 — Modelagem do problema

## 1. Classificação do problema

Classifiquei o problema como escalonamento e otimização combinatória, pois o objetivo é organizar atendimentos em horários e consultórios sem conflitos, utilizando os recursos da melhor forma possível.


## 2. Semelhança com problemas clássicos

O problema é parecido com o "Interval Scheduling", onde tarefas com horário de início e fim precisam ser organizadas sem sobreposição.

Também lembra "Bin Packing", pois os consultórios funcionam como espaços que recebem atendimentos respeitando limites.


## 3. Estruturas de dados

Utilizei listas para armazenar atendimentos e consultórios, pois são simples e facilitam a organização cronológica.

Cada atendimento possui informações como horário, duração e prioridade.

# Parte 2 — Estratégia algorítmica

## 4. Funcionamento do algoritmo

O programa lê os atendimentos, ordena por horário e tenta encaixar cada atendimento em um consultório disponível.

Se não existir consultório livre, um novo é criado.

Atendimentos expressos recebem prioridade.


## 5. Tipo de abordagem

A solução utiliza uma abordagem gulosa (greedy), pois toma decisões locais rápidas tentando encaixar cada atendimento no primeiro consultório possível.


## 6. Limitação da solução

Em alguns casos, o algoritmo pode abrir mais consultórios do que o necessário por não analisar todas as combinações possíveis antes de decidir.


## 7. Complexidade

A ordenação inicial custa O(n log n).

Depois, o algoritmo pode percorrer vários consultórios para cada atendimento, chegando a aproximadamente O(n²) no pior caso.

# Parte 3 — Decisões de implementação

## 8. Abertura de consultórios

Um novo consultório é aberto apenas quando nenhum dos existentes consegue receber o atendimento sem conflito de horário.


## 9. Atendimentos expressos

Os atendimentos expressos receberam prioridade para reduzir o tempo de espera e melhorar o atendimento dos casos urgentes.


## 10. Melhor parte da solução

A reutilização de consultórios antes de abrir novos foi a parte mais eficiente da solução.


## 11. Parte que pode melhorar

A busca por consultórios disponíveis pode ser otimizada usando estruturas mais eficientes, como filas de prioridade.


## 12. Considerações finais

A solução priorizou simplicidade, organização e facilidade de explicação durante a defesa oral, mantendo um bom equilíbrio entre clareza e eficiência.
