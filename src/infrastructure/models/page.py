from django.db import models

class Page(models.Model):
    url = models.URLField(
        max_length=200,
        help_text="URL della pagina"
    )
    level = models.IntegerField(
        help_text="Livello gerarchico (intero)"
    )
    hash_content = models.CharField(
        max_length=64,
        help_text="Hash del contenuto (tipicamente SHA‑256, 64 caratteri esadecimali)"
    )
    from_id = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_column='from_id',
        related_name='children',
        help_text="Riferimento (ID) alla pagina da cui è derivata"
    )

    class Meta:
        db_table = 'pages'

    def __str__(self):
        return f"Page #{self.pk} – Level: {self.level}"
