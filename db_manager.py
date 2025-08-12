import sqlite3

DB_NAME = "biblioteca.db"

def crear_tabla():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT NOT NULL,
            estado TEXT NOT NULL CHECK(estado IN ('Leído', 'No leído'))
        )
    """)
    conn.commit()
    conn.close()

def agregar_libro(titulo, autor, genero, estado):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO libros (titulo, autor, genero, estado) VALUES (?, ?, ?, ?)",
                   (titulo, autor, genero, estado))
    conn.commit()
    conn.close()

def actualizar_libro(id_libro, campo, nuevo_valor):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE libros SET {campo} = ? WHERE id = ?", (nuevo_valor, id_libro))
    conn.commit()
    conn.close()

def eliminar_libro(id_libro):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conn.commit()
    conn.close()

def ver_libros():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    conn.close()
    return libros

def buscar_libros(campo, valor):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = f"SELECT * FROM libros WHERE {campo} LIKE ?"
    cursor.execute(query, (f"%{valor}%",))
    libros = cursor.fetchall()
    conn.close()
    return libros