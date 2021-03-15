from tkinter import *
def generateBubbles(canvas, bubbleList):
    # It seems no information about canvas setting, so I create a canvas w.
    master = Tk()
    canvas_width = 500 # I set it 300, you can change
    canvas_height = 500
    w = Canvas(master, width=canvas_width,height=canvas_height)
    w.pack()

    for bubbleDetails in bubbleList:
        left_coordinate = bubbleDetails["left"]
        top_coordinate = bubbleDetails["top"]
        diameter_size = bubbleDetails["size"]
        bubble_color = bubbleDetails["color"]
        r = diameter_size/2
        x0 = left_coordinate - r
        y0 = top_coordinate - r
        x1 = left_coordinate + r
        y1 = top_coordinate + r
        w.create_oval(x0,y0,x1,y1, fill=bubble_color)
    mainloop()


if __name__ == '__main__':
    bubbleList1 = [{"left": 150, "top":150, "size": 100, "color": "green"}]
    bubbleList2 = [
        {"left": 317, "top":269, "size": 45, "color": "red"},
        {"left": 118, "top":27, "size": 90, "color": "orange"},
        {"left": 101, "top":321, "size": 65, "color": "yellow"},
        {"left": 231, "top":219, "size": 25, "color": "pink"},
        {"left": 50, "top":12, "size": 20, "color": "blue"}
    ]
    generateBubbles(1,bubbleList1)

