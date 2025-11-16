# Sprint 4 — Subdomínio Task Notes

## Objetivo
- Implementar `TaskNote` e operações de CRUD vinculadas a uma `Task`, garantindo coerência com o `Project` e o estado da tarefa.

## Por que
- Notas em nível de tarefa fornecem contexto granular e histórico dentro do fluxo de trabalho.

## Escopo
- Dentro: `TaskNote` (domínio), repositório, casos de uso e endpoints.
- Fora: menções/links ricos e versionamento (podem vir depois).

## Entregáveis
- `projects/domain/task_notes`: `TaskNote` + `TaskNoteRepositoryInterface`.
- `projects/infrastructure/task_notes`: `TaskNoteModel`, mappers e `TaskNoteRepository`.
- `projects/application/task_notes`: `create_task_note`, `update_task_note`, `delete_task_note`, `list_task_notes`.
- `projects/interfaces/api/task_notes`: views e serialização.
- Testes: unidade, integração, smoke.

## Endpoints
- `GET /projects/{id}/tasks/{task_id}/notes` — lista notas da tarefa.
- `POST /projects/{id}/tasks/{task_id}/notes` — cria nota (`title`, `content`).
- `PUT /projects/{id}/tasks/{task_id}/notes/{note_id}` — atualiza nota.
- `DELETE /projects/{id}/tasks/{task_id}/notes/{note_id}` — remove nota.

## Estrutura
- Domain
  - `TaskNote`: `id`, `task_id`, `title`, `content`, `created_at`.
  - Regras: criação/edição restritas se `Project` for arquivado; opcionalmente bloquear se `Task.status=done`.
  - `TaskNoteRepositoryInterface`: `get`, `list_by_task`, `create`, `update`, `delete`.
- Application
  - Valida `Project` ativo e consulta `Task` via ports de `tasks`.
- Infrastructure
  - `TaskNoteModel`, mappers e `TaskNoteRepository`.
- Interfaces
  - Views REST e DTOs.

## Testes
- Domínio: validações e restrições por `Task`/`Project`.
- Integração: persistência e filtro por `task_id`.
- API: smoke de rotas e códigos HTTP.

## Critérios de Aceite
- CRUD operando com validações, vínculo correto e hierarquia `Project→Task→TaskNote`.

## Riscos/Dependências
- Dependências das Sprints 1 e 2 (Project e Task).
- Risco: acoplamento indevido; mitigar usando IDs e ports em `application`.

## Métricas
- Tempo: 1 dia.
- Cobertura mínima: 70% domínio; smoke em API.