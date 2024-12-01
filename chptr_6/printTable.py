tableData = [['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]

def printTable (data):
    colWidths = [0] * len(tableData)
    #print(colWidths)

    for i, col in enumerate(tableData):
        widestInRow = 0;
        for j, v in enumerate(col):
            # print(v)
            if len(v) > widestInRow:
                widestInRow = len(v)
        colWidths[i] = widestInRow

    for y, v in enumerate(data[0]):
        for x in data:
            print(x[y].rjust(max(colWidths)), ' ', end='')
        print()
        

        
        
 


    


printTable(tableData)
