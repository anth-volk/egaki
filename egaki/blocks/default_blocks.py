from egaki.blocks.block import Block, BlockJiInterface, BlockRoleInterface
from egaki.type_files.ji import JiString

#################################################
# Numbers Block
#################################################

#### Roles ############
def number_role_formula(to_parse: JiString, lexable_jis: dict[str, str]) -> tuple(JiString, JiString):

  ROLE_NAME = "number"
  DECIMAL_CODE = ":record_button:"

  # Instantiate empty JiString for output and decimal counter
  output = JiString()
  decimal_counter: int = 0

  # While the first ji is of number type:
  cur_ji = to_parse.jis[0]
  while lexable_jis[cur_ji.code]["name"] == ROLE_NAME:

    # Increment decimal_counter if current ji is decimal
    if cur_ji.code == DECIMAL_CODE:
      decimal_counter += 1

    # Raise error if attempting to add second decimal
    if decimal_counter > 1:
      raise ValueError("Improper number type: two or more decimals utilized")

    # Push next value into output
    output.jis.append(cur_ji)

    # Shift first ji from to_parse
    to_parse.jis.pop(0)

    # Reassign cur_ji
    cur_ji = to_parse.jis[0]

  # Return input (minus lexed token) and the token itself
  return to_parse, output

#### Other ############
numbers_block_indicator = JiString("🔢")

#### Jis ##############
numbers_block_jis: list[BlockJiInterface] = [
  {
    "name": "zero",
    "ji": ":keycap_0:",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "one",
    "ji": ":keycap_1:",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "two",
    "ji": ":keycap_2:",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "three",
    "ji": ":keycap_3:",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "four",
    "ji": ":keycap_4:",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "five",
    "ji": ":keycap_5:",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "six",
    "ji": ":keycap_6:",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "seven",
    "ji": ":keycap_7:",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "eight",
    "ji": ":keycap_8:",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "nine",
    "ji": ":keycap_9:",
    "role": numbers_block_roles["digit"]
  },
]

#### Instantiator #####
NumbersBlock = Block(
  numbers_block_indicator,
  numbers_block_jis
)

#################################################
# Default Blocks Export
#################################################

DefaultBlocks = [
  NumbersBlock
]
