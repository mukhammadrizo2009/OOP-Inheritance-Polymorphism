### 7. 🎵 **Media Player**

class Media:
    """_summary_
    """
    def __init__(self , name: str , kind: str , author: str):
        """_summary_

        Args:
            name (str): _description_
            kind (str): _description_
            author (str): _description_
        """
        self.name   = name
        self.kind   = kind
        self.author = author
        
class Song(Media):
    """_summary_

    Args:
        Media (_type_): _description_
    """
    def play(self):
        """_summary_
        """
        print(f"{self.kind} | {self.author} | {self.name}: playing ...🎶")
        
class Movie(Media):
    """_summary_

    Args:
        Media (_type_): _description_
    """
    def play(self):
        """_summary_
        """
        print(f"{self.name} | {self.author} | {self.kind}: showing ...🎥")
        
class Podcast(Media):
    """_summary_

    Args:
        Media (_type_): _description_
    """
    def play(self):
        """_summary_
        """
        print(f"{self.name} | {self.author} | {self.kind}: playing ...🎙️")
        
        
song = Song("Eski Do'stlar" , "Classic" , "Sherali Jo'rayev")
movie = Movie("Osmondagi bolalar" , "Badiy Film" , "Zulfuqor Musoqov")
podcast = Podcast("NQE" , "Scientific" , "Teacher Azam and Kunduziy")


song.play()
movie.play()
podcast.play()