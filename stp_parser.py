import os

names = []
def get_name_from_string(line):
    if len(line) > 2:
        names.append(line[2])

def get_rid_of_space(line):
    file_string = line.rstrip()
    return(' '.join(file_string.split())).split(' ')


if __name__ == '__main__':
    print('Введите имя файла: ')
    stp_file_name = input()
    #stp_file_name = "MLS_3.txt"

    # Insert exception case
    names_area = 0
    samples_area = 0

    with open(stp_file_name) as file:
        for line in file:
            if("Signal Name" in line):
                names_area = 1
                continue
            if ("Data Table:" in line):
                names_area = 0
                continue

            if("sample" in line):
                samples_area = 1
                data_lines = [''] * len(names)
                continue

            mycollapsedstring = get_rid_of_space(line)

            if(names_area):
                get_name_from_string(mycollapsedstring)


            incr = 0
            if(samples_area):
                if len(mycollapsedstring) > 2:
                    for name in names:
                        data_lines[incr] += mycollapsedstring[incr+1] + ' '
                        incr += 1

        incr = 0
        stp_file_name = stp_file_name.replace(".", '')
        os.mkdir(stp_file_name)
        for name in names:
            name_fix =  name.replace('|', '_')
            name_fix = name_fix.replace(':', '_')
            wr_file = open( "./" + stp_file_name + "/" + name_fix + ".txt", 'w')
            wr_file.write(data_lines[incr])
            incr += 1
            wr_file.close()



        #print(names)