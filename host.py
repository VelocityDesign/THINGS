from rsa_verify import rsa_verify

class host:
  def __init__(sourceNode=false)
    if sourceNode=false:
      # TO-DO! ADD NODE CONNECTIONS!
    else:
      self.chain=[]
      
  def addTransaction(transaction):
    pubkey = transaction.from.publickey
    signedmessage = transaction.signed
    orginmessage = transaction.unsigned
    rsa_verify(orginmessage, signedmessage, pubkey)
    
