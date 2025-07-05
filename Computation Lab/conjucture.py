#collatz conjucture
import numpy as np
from manim import *
import time
number=int(input("Enter no. here"))
sum=[]
def conjucture(num):
        while num !=1:
            if num%2==0:
                num/=2
            else:
                num=3*num+1
            sum.append(num)
        return sum
class manim_graph(Scene):
    def construct(self):
        start=time.time()
        self.camera.background_color = WHITE
        count=(conjucture(number))
        y_max=max(count)
        axes=Axes(x_range=[0,len(count)],y_range=[0,y_max],axis_config={'include_numbers':False},x_axis_config={'include_ticks':False},y_axis_config={'include_ticks':False}).set_color_by_gradient(RED,BLUE,GREEN)
        labels = axes.get_axis_labels(x_label='x', y_label='y')
        self.add(labels)
        self.add(axes)
        x=np.array([i for i in range(1,len(count)+1)])
        graph=axes.plot_line_graph(x,count,line_color=BLACK,add_vertex_dots=False)
        dots=VGroup(*[Dot(radius=0.075,color=BLUE).move_to(axes.c2p(i,j))for i,j in zip(x,count)])
        #self.add(dots)
        self.play(Create(graph),run_time=5,)
        self.wait(5)
        end=time.time()
        print("Runtime=",end-start)