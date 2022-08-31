import base64
import json
import hmac
import hashlib
import datetime
 
def getJWT(secret_jwt,email):
    current_time = datetime.datetime.now()
    encoding = "utf-8"
    secret = secret_jwt.encode(encoding)
    iat = int(current_time.strftime("%s"))
    exp =  iat+(3600*24*30)
    
    jwt_header = json.dumps(
       { "alg": "HS256", "typ": "JWT" }, separators=(",", ":")
    ).encode(encoding)
 
    jwt_payload = json.dumps(
       {"email": email, "iat": iat, "exp": exp}, separators=(",", ":")
    ).encode(encoding)
 
    encoded_header_bytes = base64.urlsafe_b64encode(jwt_header).replace(b"=", b"")
    encoded_payload_bytes = base64.urlsafe_b64encode(jwt_payload).replace(b"=", b"")
 
    jwt_signature = hmac.digest(
       key=secret,
       msg=b".".join([encoded_header_bytes, encoded_payload_bytes]),
       digest=hashlib.sha256
    )
 
    encoded_signature_bytes = base64.urlsafe_b64encode(jwt_signature).replace(b"=", b"")
    
    jwt_returned = (
       f"{str(encoded_header_bytes, encoding)}" +
       f".{str(encoded_payload_bytes, encoding)}" +
       f".{str(encoded_signature_bytes, encoding)}"
    )
    print(jwt_returned)
    return jwt_returned