from egaki.type_files.ji import JiString
from egaki.interpretation.token import Token
from egaki.blocks.default_blocks import DefaultBlocks

class Lexer:
  def __init__(self):
    self.tokens = []
    self.lexable_jis = self._construct_lexable_jis()
  
  def _construct_lexable_jis(self):

    lexable_jis: dict[str, str] = {}

    for block in DefaultBlocks:
      jis = block.jis
      for ji in jis:
        lexable_jis.update({ji["ji"]: ji["role"]})

    return lexable_jis
  
  def lex(self, line: str) -> list[Token]:
    # Initiate a list that will contain the tokens
    tokens: list[Token] = []

    # Convert input into a JiString of Jis
    typed_input = JiString(line).jis

    # Create an iterable list of all possible tokens
    possible_tokens: list[str] = self.lexable_jis.keys()

    # TODO: Edit below to allow for ji type formulas

    # # For each ji in the input
    # for ji in typed_input:
    #   # If the ji isn't recognized, raise error
    #   if ji.code not in possible_tokens:
    #     raise SyntaxError(f"'{ji.code}' not a valid token")

    #   # Create a new token that contains the Ji and its function
    #   cur_token = Token(ji, self.lexable_jis[ji.code])

    #   # Append that to the tokens list
    #   tokens.append(cur_token)

    # return tokens