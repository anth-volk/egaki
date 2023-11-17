from typing import Union

from egaki.type_files.ji import Ji, JiString
from egaki.interpretation.token import Token
from egaki.blocks.block import BlockRoleInterface
from egaki.blocks.default_blocks import DefaultBlocks

class Lexer:
  def __init__(self):
    self.tokens = []
    self.lexable_jis = self._construct_lexable_jis()
  
  def _construct_lexable_jis(self):

    lexable_jis: dict[str, BlockRoleInterface] = {}

    for block in DefaultBlocks:
      jis = block.jis
      for ji in jis:
        lexable_jis.update({ji["ji"]: ji["role"]})

    return lexable_jis
  
  def lex(self, line: str) -> list[Token]:
    # Initiate a list that will contain the tokens
    tokens: list[Token] = []

    # Convert input into a JiString of Jis
    jiStringed_line = JiString(line).jis

    # Create an iterable list of all possible tokens
    possible_jis: list[str] = self.lexable_jis.keys()

    # Begin to iterate through line, processing and removing
    # until no more characters remain
    while len(jiStringed_line) > 0:
      cur_ji: Ji = jiStringed_line[0]
      if cur_ji.code not in possible_jis:
        raise SyntaxError(f"'{cur_ji.code}' not a valid input")
      
      # Run the current ji's role formula, updating our line and 
      # producing the JiString we'll make into a Token
      cur_ji_role = self.lexable_jis[cur_ji.code]
      jiStringed_line, token_to_create = cur_ji_role["formula"]()

      # Create a new Token from the output
      new_token = Token(token_to_create, cur_ji_role["name"])

      # Append that to the tokens list
      tokens.append(new_token)

    return tokens