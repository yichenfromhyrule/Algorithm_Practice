# Decode Message with Uppercase Letters
# author @Yichen

def getBadEdge(g,limit):
    result_list = []
    for point in g.keys():
        result_line = [point]
        lines = g[point]
        for line in lines:
            if(line[1]>limit):
                result_line+=line
                result_list.append(result_line)
    print(result_list)

if __name__ == '__main__':
    g = {
        "A": [["C", 30]],
        "B": [["D", 15]],
        "C": [["B", 25],["D",5]],
        "D": [["C", 20]],
        "E": [["C", 10]],

    }
    getBadEdge(g, 15)


