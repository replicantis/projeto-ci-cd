from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conversor de Temperatura</title>
    <style>
        body {
            align-items: center;
            background: #0f172a;
            color: #e2e8f0;
            display: flex;
            font-family: Arial, sans-serif;
            justify-content: center;
            margin: 0;
            min-height: 100vh;
        }

        .card {
            background: #1e293b;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            max-width: 430px;
            padding: 32px;
            width: 90%;
        }

        h1 {
            color: #38bdf8;
            margin-top: 0;
        }

        input, button {
            border-radius: 6px;
            box-sizing: border-box;
            font-size: 16px;
            margin-top: 10px;
            padding: 12px;
            width: 100%;
        }

        input {
            border: 1px solid #64748b;
        }

        button {
            background: #0284c7;
            border: none;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background: #0369a1;
        }

        #resultado {
            color: #7dd3fc;
            font-size: 20px;
            font-weight: bold;
            margin-top: 24px;
        }
    </style>
</head>
<body>
    <main class="card">
        <h1>Conversor de Temperatura</h1>
        <p>Informe uma temperatura em Celsius para convertê-la em Fahrenheit.</p>

        <form method="post">
            <label for="celsius">Temperatura em Celsius:</label>
            <input id="celsius" name="celsius" type="number" step="any" required>
            <button type="submit">Converter</button>
        </form>

        {% if resultado is not none %}
            <p id="resultado">{{ celsius }} °C equivalem a {{ resultado }} °F.</p>
        {% endif %}
    </main>
</body>
</html>
"""


def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    celsius = None

    if request.method == "POST":
        celsius = float(request.form["celsius"])
        resultado = celsius_para_fahrenheit(celsius)

    return render_template_string(
        HTML,
        resultado=resultado,
        celsius=celsius
    )


@app.route("/api/converter")
def api_converter():
    celsius = float(request.args.get("celsius", 0))
    fahrenheit = celsius_para_fahrenheit(celsius)

    return jsonify(
        {
            "celsius": celsius,
            "fahrenheit": fahrenheit
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)