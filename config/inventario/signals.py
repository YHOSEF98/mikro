from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import EntradaInventario, SalidaInventario

@receiver(post_save, sender=EntradaInventario)
@receiver(post_save, sender=SalidaInventario)
def actualizar_stock(sender, instance, created, **kwargs):
    producto = instance.producto

    if sender == EntradaInventario and created:
        producto.stock += instance.cantidad

    if sender == SalidaInventario and created:
        producto.stock -= instance.cantidad

    producto.save()
