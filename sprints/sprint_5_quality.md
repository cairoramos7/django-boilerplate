# Sprint 5 — Qualidade Transversal

## Objetivo
- Consolidar validações cross-domain, padronizar respostas de erro, adicionar paginação/ordenação e realizar smoke tests finais nas rotas principais.

## Por que
- Garantir consistência de comportamento e robustez em todo o app `projects`, reduzindo surpresas para consumidores da API.

## Escopo
- Dentro: validações de `Project` ativo em `application`, paginação `limit/offset`, ordenação previsível, tratamento uniforme de erros e smoke tests.
- Fora: autenticação/autorização avançada e observabilidade profunda (podem ser tratadas depois).

## Entregáveis
- Ajustes em `projects/application/*` para validações transversais.
- Padronização de DTOs de erro nas views em `interfaces/api/*`.
- Paginação e ordenação em list endpoints (`projects`, `tasks`, `project_notes`, `task_notes`).
- Suite de smoke tests cobrindo rotas principais.

## Endpoints
- Revisão de todos os list endpoints adicionando `limit`, `offset` e `order_by` (quando aplicável), com defaults seguros.

## Estrutura
- Application: funções utilitárias para checagem de status do projeto em casos de uso.
- Interfaces: middleware simples (se necessário) para formatação de erros; padronização de respostas.

## Testes
- Smoke tests para cada subdomínio e para `core`.
- Verificação de paginação e ordenação.
- Checagem de mensagens de erro padronizadas.

## Critérios de Aceite
- Paginação e ordenação disponíveis e consistentes.
- Erros padronizados.
- Validações transversais aplicadas corretamente.

## Riscos/Dependências
- Dependências de todas as sprints anteriores.
- Risco: quebra de compatibilidade em respostas; mitigar com defaults e documentação.

## Métricas
- Tempo: 0,5–1 dia.
- Cobertura: smoke em endpoints críticos.