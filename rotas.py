from flask import Blueprint, jsonify

calculadora_bp = Blueprint('calculadora', __name__)

@calculadora_bp.route('/soma/<int:a>/<int:b>')
def soma(a, b):
    resultado = a + b
    return jsonify({
        'operacao': 'soma',
        'a': a,
        'b': b,
        'resultado': resultado
    })
