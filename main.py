def check_two_list(list_one,list_two):
    for i in list_one:
        for j in list_two:
            if i == j:
                print(f"i : {i}\nj : {j}")

def new_check():
    pass
if __name__ == '__main__':
    check_two_list([1,2,3],[1,2,3,4])
