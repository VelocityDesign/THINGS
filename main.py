# Import Modules
# following imports are required by PKI
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

# Make the Identity class
class Identity:
  def __init__(bits="2048"):
    self._private_key = RSA.generate(bits, random)
    self._public_key = self._private_key.publickey()
    
class Transaction:
  def __init__(toAddress, cargo, isContract=false, isCreation=false):
    self.to=toAddress
    self.cargo=cargo
    if isContract:
      self._isContract=true
    else:
      self.isContract=false
    if isCreation:
      self.isCreation=true
    else:
      self.isCreation=false
      
class Thing:
  def __init__(properties, isConstant=false, canBeCloned=false):
    self.properties=properties
    self._oldProperties=[]
    if isConstant:
      self.constant=true;
    else:
      self.constant=false 
    if canBeCloned:
      self.cloneable=true;
    else:
      self.cloneable=false
    
  def edit(newProperties):
    if self.constant:
      raise self.ConstError, "This THING is constant"
    else:
      self._oldProperties.push(self.properties)
      self.properties=newProperties
      
  def getProperty(propertyToGet): 
      return self.properties[propertyToGet]
    
class Wallet:
  def __init__(name, bits="2048", imported_identity="NONE"):
    self.name = name
    if imported_identity="NONE":
      self.keys = new Identity(bits)
    else:
      self.keys = imported_identity
    self.nonce = 0
    
  def sign(toSign):
    return self.keys._private_key.sign(toSign)
  
  def transact(transaction, chain):
    transaction.signedMessage = self.sign(transaction)
    
