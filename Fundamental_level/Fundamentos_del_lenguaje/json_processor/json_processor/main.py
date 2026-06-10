import json
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "data.json"


def cargar_datos(path: Path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if not isinstance(data, list):
                raise ValueError("El JSON debe ser una lista")

            return data

    except FileNotFoundError:
        print("Archivo no encontrado")
        return []
    except json.JSONDecodeError:
        print("Error de formato JSON")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []


def filtrar_activos(datos):
    return [d for d in datos if d.get("activo")]


def agrupar_por_pais(datos):
    resultado = defaultdict(list)

    for persona in datos:
        pais = persona.get("pais", "UNKNOWN")
        resultado[pais].append(persona)

    return resultado


def clasificar_edad(persona):
    edad = persona.get("edad", 0)

    match edad:
        case edad if edad < 25:
            return "joven"
        case edad if edad < 35:
            return "adulto"
        case _:
            return "senior"


def enriquecer_datos(datos):
    for d in datos:
        d["categoria_edad"] = clasificar_edad(d)
    return datos


def main():
    datos = cargar_datos(DATA_PATH)

    if not datos:
        print("No hay datos para procesar")
        return

    activos = filtrar_activos(datos)
    enriquecidos = enriquecer_datos(activos)
    agrupados = agrupar_por_pais(enriquecidos)

    print("\nResultado:\n")

    for pais, personas in agrupados.items():
        print(f"{pais} → {len(personas)} personas")
        for p in personas:
            print(f"  - {p['nombre']} ({p['categoria_edad']})")


if __name__ == "__main__":
    main()
