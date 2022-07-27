import pytube
import timeit
import os

# Parameters
Total_video_count = 0
Total_video_length = 0 # in seconds
s = 0 # seconds
m = 0 # minutes
h = 0 # hours
error_count = 0

# Startup
start = timeit.default_timer()
os.system('cls')
print("[LOG] Start executing video_statistic.py\n")

# Read file
f = open('all_video_link.md', 'r', encoding='utf-8')
links = f.read()
f.close()

# Data Inspection and Transformation
# print("[LOG] " + str(type(links)))
# print("[LOG] Data: \n\n" + links + "\n")
links = list(links.split('\n'))
links = list(filter(None, links)) # remove empty string/line
# print("[LOG] " + str(type(links)))
# print("[LOG] Data: \n")
# print(links)
# print()
for element in links:
    # element = element.rstrip('</br>')
    if "# CH" in element:
        links.remove(element)
# print("[LOG] " + str(type(links)))
# print("[LOG] Data: \n")
# print(links)
# print()

# Data Gathering
Total_video_count = len(links)
for i in range(Total_video_count):
    # print("[LOG] Loading video stats " + str(i+1) + "/" + str(Total_video_count) + " : " + links[i])
    try:
        yt = pytube.YouTube(links[i])
    except:
        print("[LOG] Error: " + links[i])
        error_count += 1
        continue
    Total_video_length += yt.length

# Time Conversion
h = Total_video_length // 3600
m = (Total_video_length - h * 3600) // 60
s = Total_video_length - h * 3600 - m * 60

# Show Data
print("\n")
print("[LOG] Total video count: " + str(Total_video_count))
print("[LOG] Total video length(s): " + str(Total_video_length) + " seconds")
print("[LOG] Total video length(hms): " + str(h) + " hours " + str(m) + " minutes " + str(s) + " seconds")

# End
stop = timeit.default_timer()
print("[LOG] Operation Time: " + str(stop - start) + " seconds\n")
print("[LOG] End executing video_statistic.py\n")