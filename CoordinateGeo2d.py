import math

class CooGeo:
#Function to create a point in define a point in 2-D
    def __init__(self,x,y):
        self.x=x
        self.y=y

#Funtion to denote distance between two points in 2-D
    def dist_bet_points(self,other):
        dis= round(pow( pow(self.x-other.x,2) + pow(self.y-other.y,2) , 0.5),2)
        return dis

#returns the reflection of a point along x axis
    def reflection_x(self):
        return self.x, -self.y

    def reflection_y(self):
        return -self.x, self.y

#section formula, diving the distance between two points in the ratio of m:n internally
    def section_int(self,other,m,n):
        temp_x= (m*other.x + n*self.x)/(m+n)
        temp_y= (m*other.y + n*self.y)/(m+n)
        return temp_x,temp_y

    def section_ext(self,other,m,n):
        temp_x= (m*other.x - n*self.x)/(m-n)
        temp_y= (m*other.y - n*self.y)/(m-n)
        return temp_x,temp_y

    def is_collinear(self,other,other2):
        area= abs(self.x*(other.y-other2.y) + other.x*(other2.y-self.y) + other2.x*(self.y-other.y))
        if area==0:
            return True
        else:
            return False

    def area_triangle(self,other,other2):

        area= abs(self.x*(other.y-other2.y) + other.x*(other2.y-self.y) + other2.x*(self.y-other.y))/2
        return area

    def check_quadrant(self):

        if self.x<0:
            if self.y<0:
                return 3
            else:
                return 2
        else:
            if self.y<0:
                return 4
            else:
                return 1


    def centroid(self,other,other2):
        area = abs(self.x*(other.y-other2.y) + other.x*(other2.y-self.y) + other2.x*(self.y-other.y))/2
        if area==0:
            return "Invalid Input"
        else:
            return round((self.x+other.x+other2.x)/3,2),round((self.y+other.y+other2.y)/3,2)

    def slope(self,other):
        return (other.y-self.y)/(other.x-self.x)

class lines:
    def __init__(self,a,b,c):

        self.coeffx=a
        self.coeffy=b
        self.constant=c

        print("The equaton of your line is {}x + {}y = {}".format(self.coeffx,self.coeffy,self.constant))
        return
















