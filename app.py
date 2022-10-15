from flask import Flask, jsonify, request, Blueprint

from bild import bild_query, CMD_TO_FANCTION

app = Flask(__name__)

FILE_NAME = 'data/apache_logs.txt'

input = {
    "cmd": "filter",
    "value": "POST"
}


@app.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        input_json = request.get_json(force=True)
    except ValueError:
        return 400

    q = {'queries': list(input_json)}

    result = None
    for query in q['queries']:

        if query['cmd'] in CMD_TO_FANCTION:
            result = bild_query(
                cmd=query['cmd'],
                param=query['value'],
                data=result
            )
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
