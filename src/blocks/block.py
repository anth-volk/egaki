from typing import TypedDict

from src.types.ji import JiString

class BlockTokenItem(TypedDict):
  """
  Interface for dicts that each functional code
  block will implement
  """
  name: str
  ji: str
  role: str

class BlockInterface:
  """
  Defines the interface used to 
  instantiate each functional code block
  """
  def __init__(self, indicator_ji: JiString, tokens: list[BlockTokenItem]):
    self.tokens = tokens
    self.indicator_ji = indicator_ji

  # indicator ji
  # tokens
    # token symbol
    # token role
  
