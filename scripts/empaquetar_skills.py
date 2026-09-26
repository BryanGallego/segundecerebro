#!/usr/bin/env python3
"""Valida las skills de skills/ y genera dist/<skill>.zip, listos para subir a Claude.

Uso:
    python3 scripts/empaquetar_skills.py            valida todas y genera los ZIP
    python3 scripts/empaquetar_skills.py --probar   demuestra que el validador rechaza
                                                    defectos conocidos y acepta una skill válida

Reglas de claude.ai (verificadas el 2026-09-26): un solo SKILL.md por carpeta; encabezado
con name y description; name en kebab-case de 64 caracteres o menos; description de 200
o menos, sin < ni >. El ZIP lleva la carpeta de la skill en su raíz.
"""

from __future__ import annotations

import re
import sys
import tempfile
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILLS = RAIZ / "skills"
DIST = RAIZ / "dist"

CLAVES_PERMITIDAS = {"name", "description"}
MAX_NOMBRE = 64
MAX_DESCRIPCION = 200
NOMBRE_VALIDO = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
# Un valor YAML sin comillas que empieza con uno de estos caracteres no se lee como texto.
INICIO_ESPECIAL_YAML = tuple("\"'[]{}&*!|>%@`#,?:-")
EXCLUIDOS_DEL_ZIP = {".DS_Store", "__pycache__"}


def leer_encabezado(texto: str) -> dict[str, str]:
    """Lee el encabezado (una «clave: valor» por línea) o lanza ValueError con la causa."""
    texto = texto.replace("\r\n", "\n")  # un archivo editado en Windows trae CRLF
    if not texto.startswith("---\n"):
        raise ValueError("falta el encabezado: el archivo debe empezar con ---")
    fin = texto.find("\n---", 4)
    if fin == -1:
        raise ValueError("el encabezado no se cierra con ---")
    campos: dict[str, str] = {}
    for linea in texto[4:fin].splitlines():
        if not linea.strip():
            continue
        clave, separador, valor = linea.partition(": ")
        if not separador:
            raise ValueError(f"línea del encabezado sin «clave: valor»: {linea!r}")
        if clave in campos:
            raise ValueError(f"clave repetida en el encabezado: {clave}")
        campos[clave] = valor.strip()
    return campos


def validar(carpeta: Path) -> list[str]:
    """Devuelve los errores de una carpeta de skill; una lista vacía significa válida."""
    principales = [p for p in carpeta.rglob("*") if p.is_file() and p.name.lower() == "skill.md"]
    if len(principales) != 1 or principales[0] != carpeta / "SKILL.md":
        return [f"debe haber exactamente un SKILL.md, en la raíz de {carpeta.name}/; hay {len(principales)}"]
    try:
        campos = leer_encabezado(principales[0].read_text(encoding="utf-8"))
    except ValueError as error:
        return [str(error)]

    errores: list[str] = []
    sobrantes = sorted(set(campos) - CLAVES_PERMITIDAS)
    if sobrantes:
        errores.append(f"claves no permitidas en el encabezado: {', '.join(sobrantes)}")
    nombre = campos.get("name", "")
    descripcion = campos.get("description", "")
    if not NOMBRE_VALIDO.fullmatch(nombre):
        errores.append(f"name {nombre!r} debe ir en kebab-case: minúsculas, dígitos y guiones")
    if len(nombre) > MAX_NOMBRE:
        errores.append(f"name tiene {len(nombre)} caracteres; el máximo es {MAX_NOMBRE}")
    if nombre and nombre != carpeta.name:
        errores.append(f"name {nombre!r} no coincide con la carpeta {carpeta.name!r}")
    if not descripcion:
        errores.append("falta description")
    if len(descripcion) > MAX_DESCRIPCION:
        errores.append(f"description tiene {len(descripcion)} caracteres; el máximo es {MAX_DESCRIPCION}")
    if "<" in descripcion or ">" in descripcion:
        errores.append("description no puede contener < ni >")
    if ": " in descripcion:
        errores.append("description no puede contener «: », rompe el YAML")
    if descripcion.startswith(INICIO_ESPECIAL_YAML):
        errores.append("description no puede empezar con un carácter especial de YAML")
    return errores


def empaquetar(carpeta: Path, destino: Path) -> Path:
    """Escribe <destino>/<skill>.zip con la carpeta de la skill en la raíz del ZIP."""
    ruta_zip = destino / f"{carpeta.name}.zip"
    with zipfile.ZipFile(ruta_zip, "w", zipfile.ZIP_DEFLATED) as archivo:
        for ruta in sorted(carpeta.rglob("*")):
            relativa = ruta.relative_to(carpeta.parent)
            if ruta.is_file() and not EXCLUIDOS_DEL_ZIP.intersection(relativa.parts):
                archivo.write(ruta, relativa.as_posix())
    return ruta_zip


def principal() -> int:
    carpetas = sorted(p for p in SKILLS.iterdir() if p.is_dir()) if SKILLS.is_dir() else []
    if not carpetas:
        print(f"No hay skills en {SKILLS}")
        return 1

    # Sin ZIP viejos: si la validación falla, no debe quedar ninguno que parezca vigente.
    DIST.mkdir(exist_ok=True)
    for viejo in DIST.glob("*.zip"):
        viejo.unlink()

    rechazadas = {c.name: errores for c in carpetas if (errores := validar(c))}
    if rechazadas:
        for nombre, errores in rechazadas.items():
            for error in errores:
                print(f"RECHAZADA {nombre}: {error}")
        print("No se generó ningún ZIP.")
        return 1

    for carpeta in carpetas:
        print(f"OK {carpeta.name} → {empaquetar(carpeta, DIST).relative_to(RAIZ).as_posix()}")
    return 0


DESCRIPCION_DE_PRUEBA = "Skill de prueba del validador. Usar solo en la prueba."


def escribir_skill(base: Path, carpeta: str, nombre: str, descripcion: str, otro_skill_md: str = "") -> Path:
    destino = base / carpeta
    destino.mkdir(parents=True)
    (destino / "SKILL.md").write_text(
        f"---\nname: {nombre}\ndescription: {descripcion}\n---\n\n# Prueba\n", encoding="utf-8"
    )
    if otro_skill_md:
        duplicado = destino / otro_skill_md
        duplicado.parent.mkdir(parents=True, exist_ok=True)
        duplicado.write_text("---\nname: otra\ndescription: otra\n---\n", encoding="utf-8")
    return destino


def probar() -> int:
    """Inyecta defectos conocidos y exige que cada uno se rechace citando su causa."""
    casos = [
        ("descripción de 201 caracteres",
         dict(carpeta="larga", nombre="larga", descripcion="x" * 201), "el máximo es 200"),
        ("nombre con mayúsculas",
         dict(carpeta="Brief", nombre="Brief", descripcion=DESCRIPCION_DE_PRUEBA), "kebab-case"),
        ("descripción con <",
         dict(carpeta="angulo", nombre="angulo", descripcion="Resume el <correo> del día"), "< ni >"),
        ("descripción con «: »",
         dict(carpeta="dos-puntos", nombre="dos-puntos", descripcion="Brief diario: cinco líneas"), "«: »"),
        ("dos SKILL.md",
         dict(carpeta="doble", nombre="doble", descripcion=DESCRIPCION_DE_PRUEBA,
              otro_skill_md="referencias/SKILL.md"), "exactamente un SKILL.md"),
    ]
    rechazados = 0
    with tempfile.TemporaryDirectory() as temporal:
        base = Path(temporal)
        for titulo, datos, causa in casos:
            errores = validar(escribir_skill(base, **datos))
            citados = [e for e in errores if causa in e]
            if citados:
                rechazados += 1
                print(f"RECHAZADA como se esperaba · {titulo}: {citados[0]}")
            else:
                print(f"FALLA · {titulo}: se esperaba un error con «{causa}» y se obtuvo {errores or 'ninguno'}")
        control = validar(escribir_skill(base, carpeta="valida", nombre="valida", descripcion=DESCRIPCION_DE_PRUEBA))
        if control:
            print(f"FALLA · control positivo: una skill válida fue rechazada: {control}")
        else:
            print("ACEPTADA como se esperaba · control positivo")

    correcto = rechazados == len(casos) and not control
    print(f"{rechazados} de {len(casos)} defectos rechazados; control positivo {'aceptado' if not control else 'RECHAZADO'}.")
    return 0 if correcto else 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # la consola de Windows no siempre usa UTF-8
    argumentos = sys.argv[1:]
    if argumentos == ["--probar"]:
        sys.exit(probar())
    if argumentos:
        sys.exit(__doc__)
    sys.exit(principal())
