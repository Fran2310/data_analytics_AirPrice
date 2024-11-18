#modulo deprecado
import matplotlib.colors as mcolors

palette_base = ['#007f97', '#a4bcbc', '#7c587f', '#4c3f77']

#Aclarar/oscurecer un color
def adjust_color(color, factor):
    """
    Ajusta la claridad de un color
    - color: Color en formato HEX
    - factor: Positivo para aclarar, negativo para oscurecer
    """
    rgb = mcolors.to_rgb(color)  # Convertir a formato RGB
    adjusted = [(1 + factor) * c if factor > 0 else c * (1 + factor) for c in rgb]
    return mcolors.to_hex([min(1, max(0, ch)) for ch in adjusted])  # Asegurar rango válido

# Generar variaciones de colores
def generate_variations(colors, num_variations=1):
    palette = []
    for color in colors:
        for i in range(1, num_variations + 1):
            palette.append(adjust_color(color, 0.3 * i))   # Más claro
            palette.append(adjust_color(color, -0.3 * i))  # Más oscuro
    return palette

# Crear la paleta extendida
extended_palette = generate_variations(palette_base)
