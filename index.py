<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crypto Trading Bot</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.1.3/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f8f9fa;
            font-family: Arial, sans-serif;
        }
        .header {
            background-color: #007bff;
            color: white;
            padding: 20px 0;
            text-align: center;
        }
        .card {
            margin: 20px 0;
        }
        .table {
            margin-top: 20px;
        }
        .positive {
            background-color: #d4edda; /* Verde claro */
            font-weight: bold;
        }
        .negative {
            background-color: #f8d7da; /* Vermelho claro */
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Crypto Trading Bot</h1>
        <p>Atualização do valor do dólar: <strong id="dolar-value">R$ {{ dolar_value }}</strong></p>
        <p>Última atualização: <span id="last-update">A cada 5 minutos</span></p>
    </div>

    <div class="container">
        <h2>Top 10 Altcoins</h2>
        <div class="card">
            <div class="card-body">
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th>Nome</th>
                            <th>Preço Atual (R$)</th>
                            <th>Variação 24h (%)</th>
                            <th>Volume Total (R$)</th>
                            <th>Market Cap (R$)</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for coin in top_altcoins %}
                        <tr class="{% if coin.price_change_percentage_24h > 0 %}positive{% else %}negative{% endif %}">
                            <td>{{ coin.name }}</td>
                            <td>R$ {{ '{:,.2f}'.format(coin.current_price_brl) }}</td>
                            <td>{{ coin.price_change_percentage_24h }}</td>
                            <td>R$ {{ '{:,.2f}'.format(coin.total_volume_brl) }}</td>
                            <td>R$ {{ '{:,.2f}'.format(coin.market_cap_brl) }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>

        <h2>Top 10 Altcoins Mais Baratas</h2>
        <div class="card">
            <div class="card-body">
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th>Nome</th>
                            <th>Preço Atual (R$)</th>
                            <th>Variação 24h (%)</th>
                            <th>Volume Total (R$)</th>
                            <th>Market Cap (R$)</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for coin in cheap_altcoins %}
                        <tr class="{% if coin.price_change_percentage_24h > 0 %}positive{% else %}negative{% endif %}">
                            <td>{{ coin.name }}</td>
                            <td>R$ {{ '{:,.2f}'.format(coin.current_price_brl) }}</td>
                            <td>{{ coin.price_change_percentage_24h }}</td>
                            <td>R$ {{ '{:,.2f}'.format(coin.total_volume_brl) }}</td>
                            <td>R$ {{ '{:,.2f}'.format(coin.market_cap_brl) }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>

        <h2>Gainers nas Últimas 24 Horas</h2>
        <div class="card">
            <div class="card-body">
                <