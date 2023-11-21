from typing import Union

from egaki.type_files.ji import JiString

def checkJiStringEquality(object_1: JiString, object_2: JiString) -> Union[tuple[bool, str], bool]:
  """
  Checks if two JiStrings are the same,
  then returns True if they are or False if not, as well as 
  an optional error string
  """

  # Confirm that both inputs are of type JiString
  if not isinstance(object_1, JiString):
    return False, "Arg 1 is not of type 'JiString'"

  if not isinstance(object_2, JiString):
    return False, "Arg 2 is not of type 'JiString'"
    
  # Check that the jis param of both are of same length
  if len(object_1.jis) != len(object_2.jis):
    return False, "Args are of different lengths"

  # Check that each item in the JiStrings is the same
  for i in range(len(object_1.jis)):
    if object_1.jis[i].code != object_2.jis[i].code:
      return False, f"""The ji codes at index {i} do not match:
      {object_1.jis[i].code}, {object_2.jis[i].code}"""
    
  # If all of the above pass, return true
  return True