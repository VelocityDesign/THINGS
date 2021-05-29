# Import Modules
# following imports are required by PKI
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

# Make the Identity class
class Identity:
  def init(bits="2048"):
    self._private_key = RSA.generate(bits, random)
    self._public_key = self._private_key.publickey()
class Wallet:
  def init(name, bits="2048", imported_identity="NONE"):
    self.name = name
    if imported_identity="NONE":
      self.keys = new Identity(bits)
    else:
      self.keys = imported_identity
    self.nonce = 0
    
