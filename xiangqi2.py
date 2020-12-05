import pygame
from pygame.locals import *
from sys import exit
class Qizi:
    def __init__(self,qipan,type,location,index,picture,black_red,is_died):
        self.type = type
        self.location = location
        self.index = index
        self.picture = picture
        self.is_died = is_died
        self.black_red = black_red
        self.qipan = qipan

    def jiang(self,location):
        same_line_number = 0
        for i in range(14):
            if qipan.get_location(i)[1] == location[1]:
                same_line_number = same_line_number+1
        for i in range(16,32,1):
            if qipan.get_location(i)[1] == location[1]:
                same_line_number = same_line_number+1

        if self.qipan.locationtoqizi(location) == -1:
            if location[1] == 4 or location[1] == 5 or location[1] == 6:
                if self.black_red == 1:

                    if same_line_number!=0 or self.qipan.get_location(31)[1]!=location[1]:

                        if location[0] <= 3:
                            if self.location[0] - location[0] == 1 or self.location[0] - location[0] == -1 and \
                                    self.location[1] - location[1] == 0:
                                return True
                            if self.location[1] - location[1] == 1 or self.location[1] - location[1] == -1 and \
                                    self.location[0] - location[0] == 0:
                                return True
                elif self.black_red != 1:
                    if same_line_number != 0 or self.qipan.get_location(15)[1] != location[1]:
                        if same_line_number != 1 or self.qipan.get_location(31):
                            if location[0] >= 7:
                                if self.location[0] - location[0] == 1 or self.location[0] - location[0] == -1 and \
                                        self.location[1] - location[1] == 0:
                                    return True
                                if self.location[1] - location[1] == 1 or self.location[1] - location[1] == -1 and \
                                        self.location[0] - location[0] == 0:
                                    return True
    def shi(self,location):
        if self.qipan.locationtoqizi(location)==-1:
            if location[1] == 4 or location[1] == 5 or location[1] == 6:
                if self.black_red == 1:
                    if location[0] <= 3:

                        if abs(self.location[0]-location[0])==1 and abs(self.location[1]-location[1])==1:
                            return True
                elif self.black_red != 1:
                    if location[0] >= 7:
                        if abs(self.location[0]-location[0])==1 and abs(self.location[1]-location[1])==1:
                            return True

    def xiang(self,location,func):
        if self.black_red == 1:
            if location[0] > 5:
                return False
        elif self.black_red == 2:
            if location[0] < 6:
                return False
        if abs(self.location[0] - location[0]) != 2 or abs(self.location[1] - location[1])!= 2:
            return False
        if self.qipan.locationtoqizi(((self.location[0]+location[0])/2,(self.location[1]+location[1])/2)) != -1:
            if func == 1:
                self.qipan.out_info[1] = u"    蹩象眼了"
            return False
        return True

    def ma(self,location,func):
        if abs(self.location[0]-location[0])==1 and abs(self.location[1]-location[1])==2:
            if self.qipan.locationtoqizi(((self.location[1]+location[1])/2,self.location[0]))==-1:
                return True
            else:
                if func == 1:
                    self.qipan.out_info[1] = u"    蹩马脚了"
        elif abs(self.location[0]-location[0])==2 and abs(self.location[1]-location[1])==1:
            if self.qipan.locationtoqizi(((self.location[0]+location[0])/2,self.location[1]))==-1:
                return True
            else:
                if func == 1:
                    self.qipan.out_info[1] = u"    蹩马脚了"

        else:
            if func == 1:
                self.qipan.out_info[1] = u"    选中位置不可走"

        return False

    def ju(self,location,func):
        if location[0] == self.location[0]:
            if location[1] < self.location[1]:
                for i in range(location[1] + 1, self.location[1]):
                    if qipan.locationtoqizi((location[0],i )) != -1:
                        if func == 1:
                            self.qipan.out_info[1] = u"    选中位置不可走"

                        return False
            elif location[1] > self.location[1]:
                for i in range(self.location[1] + 1, location[1]):
                    if qipan.locationtoqizi((location[0], i)) != -1:
                        if func == 1:
                            self.qipan.out_info[1] = u"    选中位置不可走"

                        return False

            return True
        if location[1] == self.location[1]:
            if location[0]<self.location[0]:
                for i in range(location[0]+1,self.location[0]):
                    if qipan.locationtoqizi((i,location[1]))!=-1:
                        if func == 1:
                            self.qipan.out_info[1] = u"    选中位置不可走"

                        return False

            elif location[0] >self.location[0]:
                for i in range(self.location[0]+1,location[0]):
                    if qipan.locationtoqizi((i,location[1]))!=-1:
                        if func == 1:
                            self.qipan.out_info[1] = u"    选中位置不可走"

                        return False

            return True
        if func == 1:
            self.qipan.out_info[1] = u"    选中位置不可走"

    def zu(self,location,func):
        if self.black_red == 1:
            if self.location[0] <= 5:
                if location[0] - self.location[0] == 1 and location[1] == self.location[1]:
                    return True
                if func == 1:
                    self.qipan.out_info[1] = u"    选中位置不可走"
                return False
            elif self.location[0] >= 6:
                if location[0] - self.location[0] == 1 and location[1] == self.location[1] or abs(location[1] - self.location[1]) == 1 and location[0] == self.location[0]:
                    return True
                if func == 1:
                    self.qipan.out_info[1] = u"    选中位置不可走"
                return False
        if self.black_red == 2:
            if self.location[0] >= 6:
                if location[0] - self.location[0] == -1 and location[1] == self.location[1]:
                    return True
                if func == 1:
                    self.qipan.out_info[1] = u"    选中位置不可走"
                return False
            elif self.location[0] <= 5:
                if location[0] - self.location[0] == -1 and location[1] == self.location[1] or abs(location[1] - self.location[1]) == 1 and location[0] == self.location[0]:
                    return True
                if func == 1:
                    self.qipan.out_info[1] = u"    选中位置不可走"
                return False

    def pao(self,location,func):
        if self.location[0]<location[0]:
            a = 0
            for i in range(self.location[0]+1,location[0]):
                if self.qipan.locationtoqizi((i,location[1])) != -1:
                    a = a+1
            if a <=1:
                return True
            else:
                if func == 1:
                    self.qipan.out_info[1] = u"    选中位置不可走"
                return False
        elif self.location[0]>location[0]:
            a = 0
            for i in range(location[0]+1,self.location[0]):
                if self.qipan.locationtoqizi((i,location[1])) != -1:
                    a = a+1
            if a <=1:
                return True
            else:
                if func == 1:
                    self.qipan.out_info[1] = u"    选中位置不可走"
                return False
        else:
            if location[1]<self.location[1]:
                a = 0
                for i in range(location[1] + 1, self.location[1]):
                    if self.qipan.locationtoqizi((location[0],i)) != -1:
                        a = a + 1
                if a <= 1:
                    return True
                else:
                    if func == 1:
                        self.qipan.out_info[1] = u"    选中位置不可走"
                    return False
            elif location[1]>self.location[1]:
                a = 0
                for i in range(self.location[1] + 1, location[1]):
                    if self.qipan.locationtoqizi((location[0],i)) != -1:
                        a = a + 1
                if a <= 1:
                    return True
                else:
                    if func == 1:
                        self.qipan.out_info[1] = u"    选中位置不可走"
                    return False
        if func == 1:
            self.qipan.out_info[1] = u"    选中位置不可走"

    def is_movable(self,location,func=1):#func is used for output or not,1means output 0 means not output
        if self.type == "jiang":
            return self.jiang(location)
        if self.type == "shi":
            return self.shi(location)
        if self.type == "xiang":
            return self.xiang(location,func)
        if self.type == "ma":
            return self.ma(location,func)
        if self.type == "ju":
            return self.ju(location,func)
        if self.type == "zu":
            return self.zu(location,func)
        if self.type == "pao":
            return self.pao(location,func)

    def move_to(self,location):
        if self.is_movable(location):
            self.location = location
        #print(self.qipan.locationtoqizi(location))


class Qipan:
    def __init__(self):
        background_image_film = 'foils/qipan_ext.jpg'
        background = pygame.image.load(background_image_film).convert()
        self.picture = background
        self.qizib = []
        self.qizir = []
        self.selected_qizi = -1
        self.order_index = 1 # varible use to decide which side can go ahedd, 1 means red 0 means black
        self.out_info =[u"提示：",""]
        self.out_info_pos = (448,370)
        self.out_info_size = (180,100)
        type_list = ["zu"]*5 + ["pao"]*2 + ["ju"]*2 + ["ma"]*2 + ["xiang"]*2 + ["shi"]*2 + ["jiang"]
        rlocation_list = [(4,1),(4,3),(4,5),(4,7),(4,9),(3,2),
                          (3,8),(1,1),(1,9),(1,2),(1,8),(1,3),
                          (1,7),(1,4),(1,6),(1,5)]
        blocation_list = [(7,1),(7,3),(7,5),(7,7),(7,9),(8,2),(8,8),(10,1),(10,9),
                          (10,2),(10,8),(10,3),(10,7),(10,4),(10,6),(10,5)]
        sprite_film = 'foils/qizi.png'
        sprite_image = pygame.image.load(sprite_film).convert_alpha()
        for i in range(16):
            qizi = Qizi(self,type_list[i],rlocation_list[i],i,sprite_image.subsurface((6 + i * 41, 60), (40, 40)),1,False)
            self.qizir.append(qizi)
            qizi = Qizi(self,type_list[i], blocation_list[i], i, sprite_image.subsurface((6 + i * 41, 15), (40, 40)),2, False)
            self.qizib.append(qizi)

    def location2xy(self,location):
        x = 19+44*(location[1]-1)
        y = 10+43*(location[0]-1)
        if location[0] > 5:
            y = y+ 40
        return (x,y)

    def xy2location(self,x,y):
        location1= int((x-19)/44+1)
        if y < 225:
            location0 = int((y-10)/44+1)
        else:
            location0 = int((y-10-20)/44+1)
        if location0 > 10:
            location0 = 10
        return (location0,location1)

    def locationtoqizi(self,location):
        for i in range(16):
            if self.qizir[i].location == location:
                return i
            if self.qizib[i].location == location:
                return 16+i
        return -1


    def qizi_movable(self,qizi,location,index):
        if qizi.black_red==1:
            qizi2 = self.qizib[index]
            if location[1] != qizi2.location[1]:
                return True
            else:
                for i in range(location[0]+1,qizi2.location[0]-1):
                    if self.locationtoqizi((i,location[1])) != -1:
                        return True

            self.out_info[1]=u"    老将会面"
            return False
        if qizi.black_red==2:
            qizi2 = self.qizir[index-16]
            if location[1] != qizi2.location[1]:
                return True
            else:
                for i in range(qizi2.location[0]+1,location[0]-1):
                    if self.locationtoqizi((i,location[1])) != -1:
                        return True
        self.out_info[1]=u"    老将会面"
        return False

    def isjiangjun(self):
        if self.order_index==1:
            for i in range(16):
                if self.qizib[i].is_movable(self.qizir[15].location,0) == True:
                    self.out_info[1] = u"    将军"
        elif self.order_index==0:
            for i in range(16):
                if self.qizir[i].is_movable(self.qizib[15].location,0) == True:
                    self.out_info[1] = u"    将军"
        return

    def get_location(self,index):
        if index < 16:
            return self.qizir[index].location
        elif index >=16:
            return self.qizib[index-16].location

    def is_there_qizi(self,location):
        col = self.locationtoqizi(location)
        if col < 16:
            for i in range(16):
                if self.qizir[i].location == location:
                    return False
        elif col > 15:
            for i in range(16):
                if self.qizib[i].location == location:
                    return False
        return True

    def eat(self,location):
        col = self.locationtoqizi(location)
        if col < 16:
            for i in range(16):
                if self.qizib[i].location == location:
                    self.qizib[i].location == (10,10)
                    self.qizib[i].is_died == True
        elif col>15:
            for i in range(16):
                if self.qizir[i].location == location:
                    self.qizir[i].location == (10,10)
                    self.qizir[i].is_died == True

    def moveqizi(self, index, location):
        if index > 16 and self.order_index == 0:
            qizi = self.qizib[index - 16]
            if qizi.is_movable(location) and self.qizi_movable(qizi,location,index) and self.is_there_qizi(location):
                qizi.move_to(location)
                self.order_index = 1
                self.isjiangjun()
                self.eat(location)
        elif index <=16 and self.order_index == 1:
            qizi = self.qizir[index]
            if qizi.is_movable(location) and self.qizi_movable(qizi,location,index):
                qizi.move_to(location)
                self.order_index = 0
                self.isjiangjun()
                self.eat(location)

if __name__ == "__main__":
    pygame.init()
    #screen = pygame.display.set_mode((424, 480), 0, 32)
    screen = pygame.display.set_mode((638, 480), 0, 32)
    pygame.display.set_caption(u"中国象棋")
    font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 16);

    # follow method is workable also
    # font = pygame.font.Font("C:/Windows/Fonts/STXINWEI.TTF", 16);
    font_height = font.get_linesize()
    qipan = Qipan()
    go_type = 1
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    location = qipan.xy2location(event.pos[0], event.pos[1])
                    if qipan.selected_qizi != -1:
                        qipan.moveqizi(qipan.selected_qizi, location)
                        qipan.selected_qizi = -1
                    else:
                        qipan.selected_qizi = qipan.locationtoqizi(location)
                        qipan.out_info[1] = ""

        screen.blit(qipan.picture, (0, 0))
        for i in range(16):
            qizi = qipan.qizir[i]
            screen.blit(qizi.picture,qipan.location2xy(qizi.location))
            qizi = qipan.qizib[i]
            screen.blit(qizi.picture,qipan.location2xy(qizi.location))

        y = qipan.out_info_pos[1]
        # 找一个合适的起笔位置，最下面开始但是要留一行的空
        for text in qipan.out_info:
            screen.blit(font.render(text, True, (255, 255, 0)), (qipan.out_info_pos[0], y))
            # 以后会讲
            y += font_height
            # 把笔提一行

        pygame.display.update()