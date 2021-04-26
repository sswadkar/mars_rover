from pymongo import MongoClient #pip install pymongo
import matplotlib.pyplot as plt #pip install matplotlib

def on_pick(event):
    artist = event.artist
    xmouse, ymouse = event.mouseevent.xdata, event.mouseevent.ydata
    x, y = artist.get_xdata(), artist.get_ydata()
    ind = event.ind
    print('x, y of mouse: {:.2f},{:.2f}'.format(xmouse, ymouse))
    print('Data point:', x[ind[0]], y[ind[0]])
    xcoor = int(x[ind[0]])
    ycoor = int(y[ind[0]])
    #finding the right data point according to coordinates
    if (ycoor/60 - 1) % 2 == 1:
        try:
            print("Day Of Week: " + arduino_data[((2820-xcoor)/60-1 + (ycoor / 60 - 1)*(46))]['dayOfWeek'])
            print("Date: " + arduino_data[((2820-xcoor)/60-1 + (ycoor / 60 - 1)*(46))]['date'])
            print("Time: " + arduino_data[((2820-xcoor)/60-1 + (ycoor / 60 - 1)*(46))]['time'])
            print("Temperature (C): " + arduino_data[((2820-xcoor)/60-1 + (ycoor / 60 - 1)*(46))]['temp'])
            print("Humidity: " + arduino_data[((2820-xcoor)/60-1 + (ycoor / 60 - 1)*(46))]['humidity'])
            print("Wind Speed: " + arduino_data[((2820-xcoor)/60-1 + (ycoor / 60 - 1)*(46))]['wspeed'])
            print()
        except Exception as e:
            print(e)
            print(xcoor, ycoor)
    else:
        try:
            print("Day Of Week: " + arduino_data[(xcoor/60-1 + (ycoor / 60 - 1)*(46))]['dayOfWeek'])
            print("Date: " + arduino_data[(xcoor/60-1 + (ycoor / 60 - 1)*(46))]['date'])
            print("Time: " + arduino_data[(xcoor/60-1 + (ycoor / 60 - 1)*(46))]['time'])
            print("Temperature (C): " + arduino_data[(xcoor/60-1 + (ycoor / 60 - 1)*(46))]['temp'])
            print("Humidity: " + arduino_data[(xcoor/60-1 + (ycoor / 60 - 1)*(46))]['humidity'])
            print("Wind Speed: " + arduino_data[(xcoor/60-1 + (ycoor / 60 - 1)*(46))]['wspeed'])
            print()
        except Exception as e:
            print(e)
            print(xcoor, ycoor)

client = MongoClient("mongodb://admin:password@localhost:27017")
db=client["mars_data"]
collection = db["time"]

arduino_data = list(collection.find({}))

fig, ax = plt.subplots()
tolerance =  len(arduino_data) # points
im = plt.imread("images/mars.png")

x = 60
y = 60
intervalx = 60
intervaly = 60
direction = True
for data in range(len(arduino_data)):
    #TODO check for temperature and add if statements
    if x+intervalx >= 2880:
        x = 60
        y += intervaly
    if y >= 1880:
        break
    if (y/60-1) % 2 == 1:
        temp = arduino_data[((2820-x)/60-1 + (y / 60 - 1)*(46))]['temp']
    else:
        temp = arduino_data[(x/60-1 + (y / 60 - 1)*(46))]['temp']
    temp = float(temp)
    if temp > 0:
        ax.plot(x,y,'ro-', picker=tolerance)
    elif temp < 0 and temp > -20:
        ax.plot(x,y,'yo-', picker=tolerance)
    else:
        ax.plot(x,y,'co-', picker=tolerance)
    x+=intervalx

fig.canvas.callbacks.connect('pick_event', on_pick)
ax = plt.imshow(im)
plt.show()
