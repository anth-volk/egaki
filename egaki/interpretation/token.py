from egaki.type_files.ji import Ji

class Token:
  def __init__(self, ji: Ji, role: str) -> None:
    self.ji = ji
    self.role = role

  def __repr__(self):
    if (self.role):
      return f"'{self.ji.code}': {self.role}"
    else:
      return f"'{self.ji.code}': role null"
