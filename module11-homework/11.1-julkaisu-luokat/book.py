from publication import Publication

class Book(Publication):
  def __init__(self, name, page_count, writer):
    super().__init__(name)
    self.page_count = page_count
    self.writer = writer

  def print_info(self):
    super().print_info()
    print(f"Page count: {self.page_count}")
    print(f"Writer: {self.writer}")