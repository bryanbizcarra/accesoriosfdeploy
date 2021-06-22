from django import forms

from stock.models import Producto


class ProductosFormulario(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['código_producto',
                  'nombre_producto',
                  'cantidad_productos',
                  'fecha',
                  'productos_ok',
                  'cantidad_productos_ok',
                  'merma',
                  'precio_compra',
                  'total_compra',
                  'inversion_ok',
                  'perdida',
                  'precio_unitario',
                  'nombre_local',
                  'dirección_local']
        widgets = {
            'fecha': forms.SelectDateWidget()
        }
