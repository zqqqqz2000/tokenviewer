from flask import Flask
from flask_cors import CORS
import config
from global_var import db
from token_api import get_token_data_from_server, get_btc_addr_data_from_server, get_token_data_multi_from_server
from flask import jsonify

app = Flask(__name__)
app.config.from_object(config)
CORS(app, resources=r'/*', supports_credentials=True)
with app.app_context():
    db.init_app(app=app)
    db.drop_all()
    db.create_all()


@app.route("/get_token_info/<string:token_name>")
def get_token_info(token_name):
    return get_token_data_from_server(token_name)


@app.route("/get_token_infos/<string:token_name>")
def get_token_infos(token_name):
    return jsonify(get_token_data_multi_from_server(token_name))


@app.route("/get_btc_account_info/<string:pub_addr>")
def get_btc_account_info(pub_addr):
    return get_btc_addr_data_from_server(pub_addr)


if __name__ == '__main__':
    app.run(debug=True)
