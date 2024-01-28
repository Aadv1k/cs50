from fpdf import FPDF

def get_name():
  name = input("Enter your name: ")
  return name.strip()

class CS50Shirtificate(FPDF):
  def add_header(self):
    self.add_page()
    self.set_font("helvetica", "B", 45)
    self.cell(0, 60, "CS50 Shirtificate", align="C")

  def add_body(self, name):
      self.image("./shirtificate.png", x=0, y=65)
      font_size = 30 - (len(name) % 30)
      self.set_font_size(font_size)
      self.set_text_color(255, 255, 255)
      self.text(x=47.5 + (font_size if font_size < 15 else 20), y=120, text=f"{name.title()} took CS50")

name = get_name()

pdf = CS50Shirtificate()

pdf.add_header()
pdf.add_body(name)

pdf.output("shirtificate.pdf")

print("Your 'shirtificate.pdf' is ready!")
