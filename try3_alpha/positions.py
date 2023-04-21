

class obj_pos():
    clear_pos=(0,0)
    text_pos =(0,0)
    no_text_pos=(0,0)
    scroller_pos =(0,0)
    no_text_pos2=(0,0)
    answer_pos=(0,0)


    def __init__(self,name):
        if name == 'bing':

            self.clear_pos = (1530, 980)
            self.text_pos = (1700, 980)
            self.no_text_pos = (1700, 910)
            self.scroller_pos = (1850, 800)
            self.no_text_pos2 = (1840, 500)
            self.answer_pos = (1640, 650)

        else:
            print("positions are not specified")