import datetime
basename = "image"
suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
filename = "_".join([basename, suffix])
filename = filename + ".jpg"
print(filename)
print(type(filename))