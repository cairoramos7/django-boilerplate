# Sprint 3 — Subdomínio Project Notes

## Objetivo
- Implementar `ProjectNote` e operações de CRUD associadas ao projeto, respeitando invariantes do `Project`.

## Por que
- Notas em nível de projeto permitem documentação macro e decisões registradas, separadas das notas de tarefas.

## Escopo
- Dentro: `ProjectNote` (domínio), repositório, casos de uso e endpoints.
- Fora: versionamento de nota e tags (podem ser evoluídos depois).

## Entregáveis
- `projects/domain/notes`: `ProjectNote` + `ProjectNoteRepositoryInterface`.
- `projects/infrastructure/notes`: `ProjectNoteModel`, mappers e `ProjectNoteRepository`.
- `projects/application/notes`: `create_project_note`, `update_project_note`, `delete_project_note`, `list_project_notes`.
- `projects/interfaces/api/notes`: views e serialização.
- Testes: unidade, integração, smoke.

## Endpoints
- `GET /projects/{id}/notes` — lista notas do projeto.
- `POST /projects/{id}/notes` — cria nota (`title`, `content`).
- `PUT /projects/{id}/notes/{note_id}` — atualiza nota (`title`, `content`).
- `DELETE /projects/{id}/notes/{note_id}` — remove nota.

## Estrutura
- Domain
  - `ProjectNote`: `id`, `project_id`, `title`, `content`, `created_at`.
  - Regras: tamanho máximo de `content` (definir), edição apenas se `Project` ativo.
  - `ProjectNoteRepositoryInterface`: `get`, `list_by_project`, `create`, `update`, `delete`.
- Application
  - Valida `Project` ativo via ports da `core`.
- Infrastructure
  - `ProjectNoteModel`, mappers e `ProjectNoteRepository`.
- Interfaces
  - Views REST e DTOs.

## Testes
- Domínio: validação de tamanho e edição condicionada ao status do projeto.
- Integração: persistência e filtro por `project_id`.
- API: smoke de rotas e códigos HTTP.

## Critérios de Aceite
- CRUD operando com validações e vínculo correto ao projeto.
- `notes` do projeto separadas de `task_notes`.

## Riscos/Dependências
- Dependência do `Project` (Sprint 1) para validação de status.
- Risco: confusão com o app `notes` existente; escopo isolado por app `projects`.

## Métricas
- Tempo: 1 dia.
- Cobertura mínima: 70% domínio; smoke em API.