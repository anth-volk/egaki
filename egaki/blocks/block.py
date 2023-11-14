from typing import TypedDict

from egaki.type_files.ji import JiString

class 

class BlockJiInterface(TypedDict):
  """
  Interface for dicts that each functional code
  block will implement
  """
  name: str
  ji: str
  role: str

class Block:
  """
  Instantiates a functional code block
  """
  def __init__(self, indicator_ji: JiString, jis: list[BlockJiInterface]):
    self.jis = jis
    self.indicator_ji = indicator_ji

  # indicator ji
  # tokens
    # token symbol
    # token role
  
