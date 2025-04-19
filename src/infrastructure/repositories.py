from infrastructure.models import Page as PageModel
from domain.entities import Page as PageEntity

class DjangoPageRepository:
    """
    Repository che mappa i PageModel di Django
    in dizionari JSON serializzabili (anziché entità di dominio).
    """

    def all(self) -> list[dict]:
        """Restituisce tutte le pagine come dizionari JSON-ready."""
        pages = PageModel.objects.all()
        return [self._to_dict(p) for p in pages]

    def get_by_id(self, page_id: int) -> dict | None:
        """Recupera una pagina per ID come dict; restituisce None se non esiste."""
        try:
            model = PageModel.objects.get(pk=page_id)
        except PageModel.DoesNotExist:
            return None
        return self._to_dict(model)

    def save(self, entity: PageEntity) -> dict:
        """
        Salva o aggiorna l'entità di dominio come record Django.
        Ritorna il record salvato come dizionario.
        """
        if getattr(entity, 'id', None):
            model = PageModel.objects.get(pk=entity.id)
        else:
            model = PageModel()
        model.url = entity.url
        model.level = entity.level
        model.hash_content = entity.hash_content
        model.from_id_id = entity.from_id
        model.save()
        return self._to_dict(model)

    def delete(self, entity: PageEntity) -> None:
        """Elimina l'entità dal database."""
        PageModel.objects.filter(pk=entity.id).delete()

    def _to_dict(self, model: PageModel) -> dict:
        """Converte un modello Django in un dizionario JSON serializzabile."""
        return {
            'id': model.id,
            'url': model.url,
            'level': model.level,
            'hash_content': model.hash_content,
            'from_id': model.from_id_id,
        }
