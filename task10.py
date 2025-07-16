### 10. 📄 **Documents**


class Document:
    def __init__(self , name_file: str):
        """_summary_

        Args:
            name_file (str): _description_
        """
        self.name_file = name_file
    
class WorldDocument(Document):
    """_summary_

    Args:
        Document (_type_): _description_
    """
    def print_preview(self):
        print(f"{self.name_file} printed with World Document...!")
        
        
class PdfDocument(Document):
    def print_preview(self):
        """_summary_
        """
        print(f"{self.name_file} printed with PDF Document...!")
        
pdf = PdfDocument("Python.pdf")
world = WorldDocument("world.file")


pdf.print_preview()
world.print_preview()