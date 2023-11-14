from egaki.blocks.block import Block, BlockJiInterface
from egaki.type_files.ji import JiString

#################################################
# Numbers Block
#################################################

numbers_block_indicator = JiString("🔢")
numbers_block_roles = {
  "digit": "DIGIT"
}

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
