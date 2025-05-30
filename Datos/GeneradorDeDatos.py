import pickle
import random

# Clase Product
class Product:
    def __init__(self, cod: int, name: str, price: float, stock):
        if price < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.codigo: int = cod
        self.nombre: str = name
        self.precio: float = price
        self.stock: int = stock

    def __str__(self):
        return f"Producto ({self.codigo}): {self.nombre} - Precio: ${self.precio:.2f} - Stock: {self.stock}"

    def aplicar_descuento(self, porcentaje: float) -> float:
        if not isinstance(porcentaje, (int, float)):
            raise TypeError("El porcentaje debe ser un número.")
        if not (1 <= porcentaje <= 100):
            raise ValueError("El porcentaje debe estar entre 1 y 100.")
        descuento = self.precio * (porcentaje / 100)
        return round(self.precio - descuento, 2)

# Lista ampliada de nombres únicos de productos
nombres_unicos = [
    "Camiseta estampada", "Pantalón cargo", "Zapatillas deportivas", "Campera de cuero", "Gorra trucker",
    "Mochila escolar", "Reloj inteligente", "Gafas polarizadas", "Auriculares inalámbricos", "Mouse gamer",
    "Teclado mecánico", "Monitor LED", "Silla ergonómica", "Escritorio de madera", "Lámpara de escritorio",
    "Billetera de cuero", "Perfume floral", "Libro de ciencia ficción", "Agenda 2025", "Bolígrafo premium",
    "Tableta gráfica", "Disco externo", "Altavoz Bluetooth", "Cargador portátil", "Fundas para celular",
    "Memoria USB", "Cámara instantánea", "Impresora multifunción", "Router WiFi", "Drone con cámara",
    "Gorra de lana", "Bufanda tejida", "Camisa de lino", "Pantalón de vestir", "Zapatillas urbanas",
    "Botines de cuero", "Guantes térmicos", "Cinturón trenzado", "Collar artesanal", "Pendientes de plata",
    "Reloj clásico", "Gafas de sol vintage", "Cartera de mano", "Maletín ejecutivo", "Bolso deportivo",
    "Zapatillas de trekking", "Pijama de algodón", "Pantuflas peludas", "Sandalias playeras", "Paraguas plegable",
    "Sombrero de ala ancha", "Camisa hawaiana", "Remera básica", "Short de baño", "Bañador entero",
    "Toalla de playa", "Protector solar", "Crema hidratante", "Shampoo sólido", "Cepillo de dientes eléctrico",
    "Termo inoxidable", "Mate de cerámica", "Bombilla curva", "Cuaderno rayado", "Marcadores permanentes",
    "Lapicera de gel", "Set de geometría", "Calculadora científica", "Auriculares con cable", "Soporte para celular",
    "Trípode compacto", "Micrófono USB", "Almohada viscoelástica", "Colchón inflable", "Sábanas de algodón",
    "Edredón nórdico", "Cortinas blackout", "Espejo de aumento", "Set de brochas", "Secador de pelo",
    "Plancha para el pelo", "Maquinita de afeitar", "Cortauñas", "Estuche organizador", "Mochila para notebook",
    "Campera impermeable", "Chaleco inflable", "Botella térmica", "Bolsa de dormir", "Linterna LED",
    "Cuerda de escalada", "Casco de ciclismo", "Rodilleras deportivas", "Guantes de gimnasio", "Bandas de resistencia",
    "Balón de fútbol", "Pelota de yoga", "Pesas rusas", "Colchoneta de pilates", "Ropa térmica", "Camiseta dry-fit",
    "Zapatillas para running", "Muñequeras", "Tobilleras de compresión", "Gafas de natación", "Tapones para oídos"
]

# Verificación
assert len(nombres_unicos) >= 100, "Faltan nombres únicos para los productos."

# Generar 100 productos únicos
productos = []
for i, nombre in enumerate(nombres_unicos[:100], start=1):
    precio = round(random.uniform(5.0, 500.0), 2)
    stock = random.randint(1, 100)
    producto = Product(i, nombre, precio, stock)
    productos.append(producto)

# Guardar en archivo binario
with open("productos_con_stock.bin", "wb") as f:
    pickle.dump(productos, f)

print("Archivo productos.bin generado con éxito con productos únicos.")
