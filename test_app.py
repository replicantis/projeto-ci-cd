from app import app, celsius_para_fahrenheit


def test_celsius_para_fahrenheit_zero():
    assert celsius_para_fahrenheit(0) == 32


def test_celsius_para_fahrenheit_cem():
    assert celsius_para_fahrenheit(100) == 212


def test_celsius_para_fahrenheit_negativo():
    assert celsius_para_fahrenheit(-40) == -40


def test_rota_principal():
    cliente = app.test_client()
    resposta = cliente.get("/")

    assert resposta.status_code == 200
    assert b"Conversor de Temperatura" in resposta.data


def test_api_converter():
    cliente = app.test_client()
    resposta = cliente.get("/api/converter?celsius=20")

    assert resposta.status_code == 200
    assert resposta.json["celsius"] == 20
    assert resposta.json["fahrenheit"] == 68


def test_celsius_para_fahrenheit_trinta_sete():
    assert celsius_para_fahrenheit(37) == 98.6


def test_celsius_para_fahrenheit_dez():
    assert celsius_para_fahrenheit(10) == 50


def test_api_converter_com_zero():
    cliente = app.test_client()
    resposta = cliente.get("/api/converter?celsius=0")

    assert resposta.status_code == 200
    assert resposta.json["celsius"] == 0
    assert resposta.json["fahrenheit"] == 32