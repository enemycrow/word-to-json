# 📚 Word to JSON Converter

Convierte documentos **.docx** (Word) en un archivo **JSON estructurado** con capítulos y contenido.  
Ideal para procesar libros largos (ej. 300 páginas) y poder analizarlos o navegarlos fácilmente con otros programas.

---

## 🚀 Requisitos

- [Python 3.9+](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [python-docx](https://python-docx.readthedocs.io/)

Instalar dependencias:

```bash
pip install fastapi uvicorn python-docx
```

---

## ⚙️ Uso

1. Clonar el proyecto o copiar el archivo `main.py`.
2. Activar el entorno virtual (opcional pero recomendado).
3. Ejecutar el servidor:

```bash
uvicorn main:app --reload
```

4. Abrir en el navegador:

```
http://127.0.0.1:8000/docs
```

5. En la interfaz, usar el endpoint **POST /convert**:
   - Subir un archivo `.docx`.
   - Recibirás el JSON estructurado.

---

## 📊 Ejemplo de salida

Entrada (`.docx` con capítulos en **Heading 1**):

```
Prólogo
Este es el texto de introducción...

Capítulo 1: El sonido del bosque
Aquí empieza la historia...
```

Salida (`.json`):

```json
{
  "title": "MiLibro.docx",
  "chapters": [
    {
      "title": "Prólogo",
      "content": "Este es el texto de introducción..."
    },
    {
      "title": "Capítulo 1: El sonido del bosque",
      "content": "Aquí empieza la historia..."
    }
  ]
}
```

---

## ✨ Notas

- Detecta capítulos por estilo **Heading 1** en Word.
- Todo el texto normal debajo se añade como **contenido del capítulo**.
- Si un capítulo no tiene texto debajo, se guardará vacío.
- Compatible con libros largos (probado con más de 300 páginas).

---

## 🌹 Autores

Proyecto creado con cariño por Rodolfo & Nova   
