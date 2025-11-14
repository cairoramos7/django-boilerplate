# TODO DDD do módulo `notes`

## Domínio
- [ ] Criar Value Objects: `NoteId`, `Title`, `Content`, `Timestamps` com validações.
- [ ] Definir invariantes do agregado `Note` e validar em `update`.
- [ ] Introduzir eventos de domínio: `NoteCreated`, `NoteUpdated`, `NoteDeleted`.

## Infraestrutura
- [ ] Criar mapper `notes/infrastructure/mappers.py` com `to_entity(NoteModel) -> Note` e `to_model(Note) -> NoteModel`.
- [ ] Corrigir import do ORM: usar `from notes.models.note_model import NoteModel` no repositório.
- [ ] Atualizar `NoteRepository` para usar o mapper e retornar entidades de domínio.
- [ ] Sincronizar `id`, `created_at`, `updated_at` entre `NoteModel` e `Note` em `create/update`.

## Aplicação (Casos de Uso)
- [ ] Padronizar `NoteUseCases` com objetos de request/response (dataclasses) e retornos consistentes.
- [ ] Ajustar imports (`Note`, `Optional`, `List`, `NoteRepository`) e nomes (`get`/`get_by_id`, `delete(note_id)`).
- [ ] Publicar eventos de domínio nos casos de uso (criação, atualização, exclusão).

## Interfaces/API
- [ ] Definir estratégia de serializers:
  - [ ] Se usar DRF com ORM: `NoteSerializer` baseado em `NoteModel`.
  - [ ] Se usar DTO puro: `serializers.Serializer` com persistência nos casos de uso.
- [ ] Remover duplicações de views e alinhar imports (`APIView`, `Response`, `status`).
- [ ] Alinhar chamadas aos casos de uso: `get(note_id)`, `update(note_id, title, content)`, `delete(note_id)`.

## Rotas e Configuração
- [ ] Corrigir `notes/urls.py` para importar `path` e views, e expor `note-list`/`note-detail`.
- [ ] Incluir `path('api/', include('notes.urls'))` em `app/urls.py`.

## Injeção de Dependências
- [ ] Introduzir fábrica/contêiner simples para criar `NoteUseCases(NoteRepository)` nas views, evitando instanciação direta.

## Testes
- [ ] Unitários para VOs e entidade `Note` (invariantes e `update`).
- [ ] Testes do mapper e do `NoteRepository` (retornos como `Note`).
- [ ] Testes dos casos de uso com publicação de eventos.
- [ ] Testes de integração da API (listar, obter, criar, atualizar, excluir).

## Correções Rápidas (higiene)
- [ ] Importar `datetime` em `notes/domain/entities.py` e ajustar tipos de `created_at/updated_at`.
- [ ] Corrigir caminho do `NoteModel` no repositório de infraestrutura.
- [ ] Corrigir `NoteDetailView.delete` para receber `note_id` e chamar `use_case.delete(note_id)`.
- [ ] Corrigir imports de `APIView/Response` e remover duplicações de arquivos de view.
- [ ] Alinhar `get_by_id` nas views com `get(note_id)` nos casos de uso.