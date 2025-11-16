# Plano de Sprints — App Projects (DDD)

## Visão Geral
- App `projects` com domínio principal (`core/Project`) e subdomínios: `tasks`, `notes` (do projeto) e `task_notes` (notas da tarefa).
- Camadas por DDD: `domain` (regras), `application` (casos de uso), `infrastructure` (ORM/adapters), `interfaces` (API).
- Objetivo: demonstrar sub-domínios claros e integração via ports/IDs, evitando acoplamento indevido.

## Índice de Sprints
- Sprint 1 — Core/Project: `sprint_1_core.md`
- Sprint 2 — Tasks: `sprint_2_tasks.md`
- Sprint 3 — Project Notes: `sprint_3_project_notes.md`
- Sprint 4 — Task Notes: `sprint_4_task_notes.md`
- Sprint 5 — Qualidade Transversal: `sprint_5_quality.md`
- Glossário DDD (opcional): `glossario_ddd.md`

## Estrutura Proposta
- `projects/domain/core` — agregado `Project`, invariantes e ports de repositório
- `projects/domain/tasks` — `Task` e regras de status/prazos
- `projects/domain/notes` — `ProjectNote` e regras de edição
- `projects/domain/task_notes` — `TaskNote` e vínculo com `Task`
- Pastas espelhadas em `application`, `infrastructure`, `interfaces/api` por subdomínio

## Principais Endpoints
- Core:
  - `GET /projects/`, `GET /projects/{id}/`, `POST /projects/`
  - `POST /projects/{id}/archive`, `POST /projects/{id}/unarchive`
- Tasks:
  - `GET /projects/{id}/tasks`, `POST /projects/{id}/tasks`
  - `PUT /projects/{id}/tasks/{task_id}`, `PATCH /projects/{id}/tasks/{task_id}/status`
- Project Notes:
  - `GET /projects/{id}/notes`, `POST /projects/{id}/notes`
  - `PUT /projects/{id}/notes/{note_id}`, `DELETE /projects/{id}/notes/{note_id}`
- Task Notes:
  - `GET /projects/{id}/tasks/{task_id}/notes`, `POST /projects/{id}/tasks/{task_id}/notes`
  - `PUT /projects/{id}/tasks/{task_id}/notes/{note_id}`, `DELETE /projects/{id}/tasks/{task_id}/notes/{note_id}`

## Critérios Gerais
- Cada sprint entrega regras de domínio, casos de uso, adapters e endpoints com testes.
- Subdomínios interagem via `ProjectId` e ports expostos pela `application/core`.