from publication import Publication

class Magazine(Publication):
  def __init__(self, name, editor):
    super().__init__(name)
    self.editor = editor

  def print_info(self):
    super().print_info()
    print(f"Editor: {self.editor}")