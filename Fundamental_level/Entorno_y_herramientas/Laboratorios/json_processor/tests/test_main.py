from json_processor.main import clasificar_edad


def test_clasificacion():
    assert clasificar_edad({"edad": 20}) == "joven"
    assert clasificar_edad({"edad": 30}) == "adulto"
    assert clasificar_edad({"edad": 40}) == "senior"
