from blocks.block import BlockInterface, BlockTokenItem
from type_files.ji import JiString

#################################################
# Numbers Block
#################################################

numbers_block_indicator = JiString("🔢")
numbers_block_roles = {
  "digit": "DIGIT"
}
numbers_block_tokens: list[BlockTokenItem] = [
  {
    "name": "zero",
    "ji": "0️⃣",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "one",
    "ji": "1️⃣",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "two",
    "ji": "2️⃣",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "three",
    "ji": "3️⃣",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "four",
    "ji": "4️⃣",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "five",
    "ji": "5️⃣",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "six",
    "ji": "6️⃣",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "seven",
    "ji": "7️⃣",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "eight",
    "ji": "8️⃣",
    "role": numbers_block_roles["digit"]
  },
  {
    "name": "nine",
    "ji": "9️⃣",
    "role": numbers_block_roles["digit"]
  },
]

NumbersBlock = BlockInterface(
  numbers_block_indicator,
  numbers_block_tokens
)

#################################################
# Default Blocks Export
#################################################

DefaultBlocks = [
  NumbersBlock
]


  