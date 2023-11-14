from egaki.blocks.block import Block, BlockJiInterface, BlockRoleInterface
from egaki.type_files.ji import JiString

#################################################
# Numbers Block
#################################################

#### Roles ############
def number_role_formula(input: JiString) -> tuple(JiString, JiString):

  # Instantiate empty JiString for output

  # While there is a next ji and it's a number type:

    # Raise error if attempting to add second decimal

    # Push next value into output

  # Return input minus lexed token and the token itself


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
