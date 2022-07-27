from os import system, walk
from pytube import YouTube
from timeit import default_timer
from time import strftime, localtime
from datetime import date

# General parameter
export_path = './export/'
# Link gathering parameters
note_path = 'D:/Note_Database/Subject/GPII General Physics II/Note/'
filename_wrong_order = [] # Filename in wrong order
filename_extract = [] # Extracted file number in wrong order
filename_right_order = [] # Correct order filename
index = [] # Wrong filename order index
f_cnt = 0 # File count
links = [] # Link list
link_filename = export_path + 'all_video_link.md'
# Video statistics gathering parameters
Total_video_count = 0
Load_video_count = 0
Part_video_count = 0
Total_video_length = 0 # in seconds
s = 0 # seconds
m = 0 # minutes
h = 0 # hours
error_count = 0
stats_filename = export_path + 'video_statistic.txt'

# Startup
start = default_timer()
system('cls')
print("[LOG] Start executing video_statistic.py\n")

# Sort file name
for (dirpath, dirnames, filenames) in walk(note_path):
    filename_wrong_order.extend(filenames)
    break
f_cnt = len(filename_wrong_order)
for element in filename_wrong_order:
    filename_extract.append(int(element[2:4]))
for i in range(f_cnt):
    index.append(filename_extract.index(i + 1))
for i in range(f_cnt):
    filename_right_order.append(filename_wrong_order[index[i]])
# print(filename_right_order)
# print()

# Read all links
for i in range(f_cnt):
    link_buf = [] # Link buffer
    print("[LOG] " + filename_right_order[i])
    file = open(note_path + filename_right_order[i], 'r', encoding='utf-8')
    lines = file.read()
    file.close()
    lines = list(lines.split('\n'))
    # print(lines)
    for j in range(len(lines)):
        if "https://www.youtube.com/watch?v=" in lines[j] and len(lines[j]) < 70: # 44
            print("[LOG] " + lines[j])
            link_buf.append(lines[j])
    links.append([filename_right_order[i], link_buf])
# print()
# print(links[0])
# print(len(links))
# print(len(links[0]))
# print(len(links[0][1]))

# Write links to file
file = open(link_filename, 'w', encoding='utf-8')
for i in range(len(links)):
    file.write("# " + links[i][0] + '\n')
    for j in range(len(links[i][1])):
        file.write(links[i][1][j] + '\n')
file.close()
print("[LOG] Export all video link to file " + link_filename + " successfully!\n")

# Data Gathering
for i in range(len(links)):
    Total_video_count += len(links[i][1])
    Part_video_count = len(links[i][1])
    Load_video_count = 0
    for j in range(len(links[i][1])):
        Load_video_count += 1
        print("[LOG] Loading video stats from " + links[i][0] + " " + str(Load_video_count) + "/" + str(Part_video_count) + " : " + links[i][1][j])
        try:
            yt = YouTube(links[i][1][j])
        except:
            print("[LOG] Error: " + links[i][1][j])
            error_count += 1
            continue
        Total_video_length += yt.length

# Time Conversion
h = Total_video_length // 3600
m = (Total_video_length - h * 3600) // 60
s = Total_video_length - h * 3600 - m * 60

# Show Data
export_lines = [
    "Total video count: " + str(Total_video_count),
    "Total video length(s): " + str(Total_video_length) + " seconds",
    "Total video length(hms): " + str(h) + " hours " + str(m) + " minutes " + str(s) + " seconds",
    "Execute at " + str(date.today()) + " " + strftime("%H:%M:%S", localtime())
]
print("\n")
for i in range(4):
    print("[LOG] " + export_lines[i])

# Write statistics to file
file = open(stats_filename, 'w', encoding='utf-8')
for i in range(4):
    file.write(export_lines[i] + '\n')
file.close()

# End
stop = default_timer()
print("[LOG] Operation Time: " + str(stop - start) + " seconds\n")
print("[LOG] End executing video_statistic.py\n")