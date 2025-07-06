# Contenido del archivo .Rmd con explicación del programa y el código incluido

rmd_content = """
---
title: "Tarea: Aplicación de Conceptos de POO en Python"
output: html_document
---

## 💻 Tarea: Aplicación de Conceptos de POO en Python

**✅ Desarrollado en:** PyCharm  
**✅ Lenguaje:** Python  
**✅ Tema:** Programación Orientada a Objetos (POO)  

---

## 👨‍💻 Código del programa

```python
# Ejemplo base 
class Animal:
    def __init__(self, nombre):
        self._nombre = nombre  # atributo encapsulado

    def hablar(self):
        return "Hace un sonido"

class Perro(Animal):
    def hablar(self):  # polimorfismo: sobrescribe método de la clase base
        return "Ladra"

class Gato(Animal):
    def hablar(self):  # polimorfismo: sobrescribe método de la clase base
        return "Maulla"

# Instancias
mascota1 = Perro("Max")
mascota2 = Gato("Luna")

print(mascota1.hablar())  # Ladra
print(mascota2.hablar())  # Maulla
