import braintree
import json
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="p5xgghhtsbp4cvcy",
        public_key="t65fhwdp6vx25xxd",
        private_key="1e83558a7759a7ff45292b43d1e0b396"
    )
)


@app.route("/client_token", methods=["GET"])
def client_token():
  token = gateway.client_token.generate()
  print(token)
  return json.dumps({"token": token})

@app.route("/checkout", methods=["POST"])
def create_purchase():
  nonce_from_the_client = request.form["payment_method_nonce"]

'''
result = gateway.transaction.sale({
    "amount": "10.00",
    "payment_method_nonce": nonce_from_the_client,
    "options": {
      "submit_for_settlement": True
    }
})
'''