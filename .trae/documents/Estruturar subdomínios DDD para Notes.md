## Resumo
- Vou criar uma pasta `sprints/` na raiz do repositório contendo arquivos detalhando cada sprint (objetivo, porquê, escopo, entregáveis, endpoints, estrutura, testes, critérios de aceite, riscos e métricas).
- Sprints cobrem `core/Project`, `tasks`, `notes (do projeto)`, `task_notes`, e uma sprint de qualidade transversal.

## Estrutura de Pastas/Arquivos (a produzir)
- `sprints/README.md` — índice, visão geral do domínio e dos subdomínios.
- `sprints/sprint_1_core.md` — Fundações do domínio principal (`Project`).
- `sprints/sprint_2_tasks.md` — Subdomínio `Tasks`.
- `sprints/sprint_3_project_notes.md` — Subdomínio `Notes` do projeto.
- `sprints/sprint_4_task_notes.md` — Subdomínio `Task Notes`.
- `sprints/sprint_5_quality.md` — Validações transversais, erros, paginação, smoke tests.
- (Opcional) `sprints/glossario_ddd.md` — termos (entity, aggregate, repository, use case, port, adapter, bounded context, ACL, saga/eventos).

## Conteúdo de Cada Arquivo
### Cabeçalho padrão
- Objetivo — o que será entregue.
- Por que — qual problema resolve; relação com DDD.
- Escopo — o que está dentro/fora.
- Entregáveis — itens concretos (código, endpoints, testes).
- Endpoints — rotas, verbos, payloads e respostas esperadas.
- Estrutura — pastas e arquivos nas camadas `domain/application/infrastructure/interfaces`.
- Testes — unitários, integração, smoke + critérios de cobertura mínima.
- Critérios de aceite — condições claras de conclusão.
- Riscos/Dependências — o que pode atrasar, ordem correta.
- Métricas — tempo estimado, tamanho do change set, verificação.

### Sprint 1 — Core/Project (sprint_1_core.md)
- Objetivo: implementar `Project` (agregado), invariantes, repositório e endpoints básicos.
- Por que: base para `tasks`, `notes` e `task_notes`, fornece IDs e regras transversais.
- Escopo: `create/list/get/archive/unarchive`; unicidade por `owner_id`; status `active/archived`.
- Endpoints: `GET /projects/`, `GET /projects/{id}/`, `POST /projects/`, `POST /projects/{id}/archive`, `POST /projects/{id}/unarchive`.
- Estrutura: `projects/domain/core`, `projects/application/core`, `projects/infrastructure/core`, `projects/interfaces/api/core`.
- Testes: invariantes de domínio; integração repositório; smoke endpoints.
- Critérios de aceite: CRUD e transições operacionais com validações.
- Riscos: acoplamento indevido; mitigar via ports.
- Métricas: tempo 1–2 dias; cobertura mínima 70% em domínio.

### Sprint 2 — Tasks (sprint_2_tasks.md)
- Objetivo: `Task` e operações (criar/editar/status/listar por projeto).
- Por que: decompor trabalho do projeto com regras próprias.
- Escopo: `todo/doing/done`, `due_date?`, validação `Project` ativo.
- Endpoints: `GET /projects/{id}/tasks`, `POST /projects/{id}/tasks`, `PUT /projects/{id}/tasks/{task_id}`, `PATCH /projects/{id}/tasks/{task_id}/status`.
- Estrutura: `projects/domain/tasks`, `application/tasks`, `infrastructure/tasks`, `interfaces/api/tasks`.
- Testes: transições de status; integração com `Project`.
- Critérios de aceite: operações restritas por `Project` ativo; status coerente.
- Riscos: validações cruzadas; mitigar via `application/core`.
- Métricas: tempo 1–2 dias; cobertura 70% domínio/60% integração.

### Sprint 3 — Project Notes (sprint_3_project_notes.md)
- Objetivo: `ProjectNote` e CRUD vinculado ao projeto.
- Por que: documentação do projeto em nível macro.
- Escopo: tamanho máximo; edição apenas se `Project` ativo.
- Endpoints: `GET /projects/{id}/notes`, `POST /projects/{id}/notes`, `PUT /projects/{id}/notes/{note_id}`, `DELETE /projects/{id}/notes/{note_id}`.
- Estrutura: `projects/domain/notes`, `application/notes`, `infrastructure/notes`, `interfaces/api/notes`.
- Testes: regras de edição; integração com `Project`.
- Critérios de aceite: CRUD consistente e relacionamento correto.
- Riscos: duplicidade com `notes` app existente; mitigar por escopo de app.
- Métricas: tempo 1 dia; cobertura 70% domínio.

### Sprint 4 — Task Notes (sprint_4_task_notes.md)
- Objetivo: `TaskNote` e CRUD vinculado à tarefa.
- Por que: granularidade de anotação por atividade.
- Escopo: validar `Task` e `Project` ativo; limites de edição.
- Endpoints: `GET /projects/{id}/tasks/{task_id}/notes`, `POST /projects/{id}/tasks/{task_id}/notes`, `PUT /projects/{id}/tasks/{task_id}/notes/{note_id}`, `DELETE /projects/{id}/tasks/{task_id}/notes/{note_id}`.
- Estrutura: `projects/domain/task_notes`, `application/task_notes`, `infrastructure/task_notes`, `interfaces/api/task_notes`.
- Testes: vínculo de `TaskNote→Task→Project`; smoke endpoints.
- Critérios de aceite: CRUD com validações e hierarquia correta.
- Riscos: acoplamento indevido; mitigar com IDs e ports.
- Métricas: tempo 1 dia; cobertura 70% domínio.

### Sprint 5 — Qualidade Transversal (sprint_5_quality.md)
- Objetivo: validações cross-domain, paginação/ordenação, tratamento uniforme de erros e smoke tests finais.
- Por que: robustez e consistência.
- Escopo: impedir operações em projeto arquivado; paginação `limit/offset`; erros HTTP padronizados.
- Endpoints: revisão das rotas; adicionar query params (paginação/ordenar).
- Estrutura: ajustes em `application` e `interfaces`.
- Testes: smoke e integração; validação de erros e paginação.
- Critérios de aceite: endpoints estáveis e validações transversais OK.
- Métricas: tempo 0,5–1 dia.

## Próximo Passo
- Ao confirmar, crio a pasta `sprints/` e os arquivos acima com o conteúdo detalhado, seguindo este esqueleto e o estilo do seu boilerplate.