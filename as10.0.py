def user(input_list):
    return {name: number for name, number in input_list}

input_list = [("Dan Mace", 98980000), ("Connor Meyer", 077890879), ("Adam Smith", 123087699), ("John Watson", 960008779)]

output_dict = user(input_list)
print(output_dict)

