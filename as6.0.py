def lists(name_list,number_list):
    output_list=[]
    for i in range(len(name_list)):
        output_list.append((name_list[i],number_list[i]))
    return output_list

name_list=["Dan Mace", "Connor Meyer", "Adam Smith", "John Watson"]
number_list = [98980000, 777890879, 123087699, 960008779]
output_list = lists(name_list,number_list)
print(output_list)
