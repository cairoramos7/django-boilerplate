# Sprint 2 — Subdomínio Tasks

## Objetivo
- Implementar o subdomínio `Tasks` com entidade `Task`, regras de negócio e operações para criação, atualização, mudança de status e listagem por projeto.

## Por que
- Tarefas representam unidades de trabalho do projeto e exigem regras próprias (status, datas) mantendo a dependência apenas do `ProjectId` e das validações de `Project` ativo.

## Escopo
- Dentro: `Task` (domínio), repositório, casos de uso e endpoints.
- Fora: notificações, dependências entre tarefas e SLA (podem ser evoluídos depois).

## Entregáveis
- `projects/domain/tasks`: `Task` + `TaskRepositoryInterface`.
- `projects/infrastructure/tasks`: `TaskModel`, mappers e `TaskRepository`.
- `projects/application/tasks`: `create_task`, `update_task`, `change_task_status`, `list_project_tasks`.
- `projects/interfaces/api/tasks`: views e serialização.
- Testes: unidade de domínio, integração e smoke de API.

## Endpoints
- `GET /projects/{id}/tasks` — lista tarefas do projeto.
- `POST /projects/{id}/tasks` — cria tarefa (`title`, `due_date?`).
- `PUT /projects/{id}/tasks/{task_id}` — atualiza (`title`, `due_date?`).
- `PATCH /projects/{id}/tasks/{task_id}/status` — muda status (`todo/doing/done`).

## Estrutura
- Domain
  - `Task`: `id`, `project_id`, `title`, `status`, `due_date?`, `created_at`.
  - Regras: transições de `status`, validação opcional de prazo, criação bloqueada se `Project` arquivado.
  - `TaskRepositoryInterface`: `get`, `list_by_project`, `create`, `update`, `update_status`.
- Application
  - Orquestra validações de `Project` ativo via ports da `core`.
- Infrastructure
  - `TaskModel`, mappers e `TaskRepository` (Django ORM).
- Interfaces
  - Views REST e DTOs simples.

## Testes
- Domínio: transições válidas de status e invariantes de título.
- Integração: persistência e filtros por `project_id`.
- API: smoke de rotas e códigos HTTP.

## Critérios de Aceite
- CRUD e mudança de status funcionam com validações de projeto ativo.
- Domínio isolado do ORM e da camada de interface.

## Riscos/Dependências
- Dependência do `Project` da Sprint 1.
- Risco: acoplamento direto a modelos de `Project`; mitigar via ports de `application/core`.

## Métricas
- Tempo: 1–2 dias.
- Cobertura mínima: 70% domínio; smoke em API.