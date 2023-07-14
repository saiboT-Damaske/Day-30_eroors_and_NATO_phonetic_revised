try:
    file = open("data.txt", "r")
    a_dic = {"key": "value"}
    print(a_dic["key"])
except FileNotFoundError:
    print("oops, creating file")
    file = open("data.txt", "r")
except KeyError as er_message:
    print(f"what key??? {er_message} not found")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError("lol noob")
    file.close()
    print("file closed!")

# # Key Error
# a_dic = {"key": "value"}
# a_dic["hey"]


#
