from typing import TypedDict

from egaki.type_files.ji import JiString

class BlockRoleInterface(TypedDict):
  """
  Interface for defining block roles, to be utilized
  inside of block jis
  """
  name: str
  formula: function

class BlockJiInterface(TypedDict):
  """
  Interface for dicts that each functional code
  block will implement
  """
  name: str
  ji: str
  role: BlockRoleInterface

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
  
