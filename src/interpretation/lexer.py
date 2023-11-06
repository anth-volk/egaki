from src.types import JiString
from src.blocks import DefaultBlocks

class Lexer:
  def __init__(self):
    self.tokens = []
    self.lexable_jis = self.construct_lexable_jis()
  
  def construct_lexable_jis(self):

    lexable_jis: dict[str, str] = {}

    for block in DefaultBlocks:
      tokens = block.tokens
      for token in tokens:
        lexable_jis[token.ji]: token.role

    return lexable_jis
  
  def lex(self, line: str):
    # Testing to see if jis can be used as keys in Python dict
    for ji in line:
      print(ji)
      if ji in self.lexable_jis.keys():
        print(f"{ji} found as key")
      else:
        print(f"{ji} not found as key")
