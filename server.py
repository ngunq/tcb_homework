from flask import Flask, request, jsonify, abort
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# sharding data into 10 shards for scale up
shard_num = 10
shard_data = [{}] * shard_num  # can split into 10 independence dictionaries to avoid GIL


def quantile(x, p):
    p_index = int(p / 100 * len(x))
    return sorted(x)[p_index]


def get_shard_index(id, num):
    return id % num


def response(data):
    return jsonify(data=data, success=True)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e), success=False), code


@app.route('/append', methods=['POST'])
def append():
    try:
        payload = request.json
        pool_id = payload['poolId']
        pool_vals = payload['poolValues']
        s_index = get_shard_index(pool_id, shard_num)

        if pool_id not in shard_data[s_index]:
            shard_data[s_index][pool_id] = pool_vals
            return response("inserted")
        else:
            shard_data[s_index][pool_id] += pool_vals
            return response("appended")
    except Exception as e:
        abort(400)


@app.route('/query', methods=['POST'])
def query():
    try:
        payload = request.json
        pool_id = payload['poolId']
        percentile = payload['percentile']

        s_index = get_shard_index(pool_id, shard_num)

        if pool_id not in shard_data[s_index]:
            return response({
                "message": "poolId not found!"
            })

        pool_count = len(shard_data[s_index][pool_id])
        x_quantile = quantile(shard_data[s_index][pool_id], percentile)

        return response({
            "quantile": x_quantile,
            "poolCount": pool_count
        })
    except Exception as e:
        abort(400)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=7777)