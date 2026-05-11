# RACIOCINIO.md

## 1. Classificação do problema

O problema foi tratado como escalonamento, pois organiza atendimentos em horários sem conflitos.

## 2. Semelhança com problemas clássicos

É parecido com "Interval Scheduling", onde tarefas precisam ser encaixadas sem sobreposição.

## 3. Estruturas de dados

Usei listas para armazenar consultórios e atendimentos por serem simples e organizadas.

## 4. Funcionamento do algoritmo

O sistema ordena os atendimentos e tenta encaixar cada um em um consultório disponível. Se não conseguir, abre um novo.

## 5. Tipo de abordagem

A solução é gulosa (greedy), pois toma decisões rápidas usando o primeiro consultório possível.

## 6. Limitação

Em alguns casos, o algoritmo pode usar mais consultórios do que o necessário.

## 7. Complexidade

A complexidade aproximada é O(n²) no pior caso.

## 8. Abertura de consultórios

Novos consultórios são criados apenas quando não existe espaço nos atuais.

## 9. Atendimentos expressos

Os atendimentos expressos receberam prioridade na organização.

## 10. Melhor parte

A reutilização de consultórios evitou desperdício de recursos.

## 11. Parte a melhorar

A busca por consultórios pode ser otimizada futuramente.

## 12. Conclusão

A solução priorizou simplicidade, clareza e facilidade de manutenção.
