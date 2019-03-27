def read_csv_as_dict_v2(path):
    with open(path, 'r') as f:
        DATA = {}
        i = 0
        for line in f:   
            if i==0:
                #create the column for our dict...
                i=i+1
                col_header = line.split(',')
                new_col = []
                number_of_col = len(col_header)
                for j in range(0,number_of_col):
                    col_j = col_header[j]
                    col_j = str(col_j.strip("\n"))
                    DATA[col_j] = []
                    new_col.append(col_j)
            else:
                for i in range(0,number_of_col):
                    row_i = line.split(',')
                    value = row_i[i].strip("\n")
                    DATA[str(new_col[i])].append(value)
        return(DATA)