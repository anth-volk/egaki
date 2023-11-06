from type_files.ji import JiString
from blocks.default_blocks import DefaultBlocks

class Lexer:
  def __init__(self):
    self.tokens = []
    self.lexable_jis = self.construct_lexable_jis()
  
  def construct_lexable_jis(self):

    lexable_jis: dict[str, str] = {}

    for block in DefaultBlocks:
      tokens = block.tokens
      for token in tokens:
        lexable_jis[token["ji"]]: token.role

    return lexable_jis
  
  def lex(self, line: str):
    pass