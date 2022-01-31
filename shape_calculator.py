import math

class Rectangle:

  def __init__(self,width,height):
    self.width = width
    self.height = height
  
  def __str__(self):
    return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'
  
  def set_width(self,width):
    self.width = width 

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return self.width*self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  
  def get_diagonal(self):
    return  math.sqrt(pow(self.height,2) + pow(self.width,2))
  
  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return 'Too big for picture.'
    res = ''
    for x in range(self.height):
      for y in range(self.width):
        res += '*'
      res += '\n'
    return res 
  
  def get_amount_inside (self,shape):
    if (self.width < shape.width or self.height < shape.height):
      return 0
    else:
      return math.floor(self.get_area()/shape.get_area())

class Square(Rectangle):
  
  def __init__(self,height):
    super().__init__(height,height)

  def __str__(self):
    return 'Square(side='+str(self.width)+')'
  
  def set_side(self, height):
	  self.height = height
	  self.width = height



