from egaki.type_files.ji import JiString

class Token:
  def __init__(self, jis: JiString, role: str) -> None:
    self.jis = jis
    self.role = role

  def __repr__(self):
    if (self.role):
      return f"'{self.jis}': {self.role}"
    else:
      return f"'{self.jis}': role null"
