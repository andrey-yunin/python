class Music:
    music_is_playing = True

class Music_style(Music):

    style = ""
    list_style = []
    
    
   
    def insert_style(self):
        return input("Insert style:")

    def create_style(self):
        self.style = input("Enter style: ")

    def create_list_stiles(self):
        self.list_style.append(self.style)
        
        for i in self.list_style:
            print ("Music style: ", i)    


music_style = Music_style()
music_style.create_style()
music_style.create_list_stiles()

print(music_style.style)

for i in music_style.list_style:
    print (i)

        

