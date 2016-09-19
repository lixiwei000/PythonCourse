def show(*args):
    for item in args:
        print(item)

def dict_show(**kwargs):
    for item in kwargs:
        print(item,kwargs[item])

if __name__ == "__main__":
    show('Niko','Belic','Helen','Tom')
    print("==============================")
    info_dict = {"name":"Tom","age":20,"sex":"Female","location":"ShangHai"}
    dict_show(name = "Niko",age = "18",sex = "Male",location = "BeiJing")
    print("==============================")
    dict_show(**info_dict)
