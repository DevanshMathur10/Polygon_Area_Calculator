class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def set_width(self,newwidth):
        self.width=newwidth

    def set_height(self,newheight):
        self.height=newheight

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*(self.width+self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        picture= ["*"*self.width for i in range(self.height)]
        return "\n".join(picture)+"\n"
                        

    def get_amount_inside(self,shape):
        amt=int(self.get_area()/shape.get_area())
        if amt<1:
            return 0
        else:
            return amt

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self,side):
        self.side=side
        super().__init__(side,side)
    def set_side(self,side):
        self.side=self.width=self.height=side

    def set_width(self,side):
        self.set_side(side)

    def set_height(self,side):
        self.set_side(side)

    def __repr__(self):
        return f"Square(side={self.side})"