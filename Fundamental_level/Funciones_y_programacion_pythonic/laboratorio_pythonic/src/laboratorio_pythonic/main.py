import random
from laboratorio_pythonic.decorators import retry
from laboratorio_pythonic.generators import batch_generator
from laboratorio_pythonic.context_managers import Timer


@retry(max_retries=5, delay=1)
def funcion_inestable():
    if random.random() < 0.7:
        raise ValueError("Falló la función")
    return "Éxito"


def test_generador():
    data = list(range(10))
    for lote in batch_generator(data, 3):
        print(lote)


def test_timer():
    with Timer():
        total = sum(range(1_000_000))


if __name__ == "__main__":
    print(funcion_inestable())
    test_generador()
    test_timer()