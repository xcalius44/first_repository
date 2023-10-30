class TV:
    def channel(self ,choise1):
        channel_max = 723 
        channel_min = 0
        self.choise1 = choise1
        if choise1 == channel_min or choise1 == channel_max:
            print("we dont have a channel like that")
        else:
            print("now it a chanel " ,choise1)
            
    
    def volume(self ,choise2):
        volume_max = 100 
        volume_min = 0
        self.choise2 = choise2 
        if choise2 == volume_min or choise2 == volume_max:
            print("we dont have a channel like that")
        else:
            print("now it a chanel " ,choise2)
        
def main():
    tv=TV()
    while True:
        choise = int(input('0: quit\
                           1: change channel\
                           2: change volume\
                           yuor choise:'))
        if choise == 1:
            choise1 = int(input("what channel: "))
            tv.volume(choise1)

        elif choise == 2:
            choise2 = int(input("what channel: "))
            tv.volume(choise2)
        elif choise == 0:
            break

        else:
            print("we dont have thes channel")
main()
