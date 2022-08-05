# YouTube-Video-Statistic-Gathering
## !!ATTENTION!! This repo is archived, and will no longer be updated.
## Description
This repo can read YouTube links from markdown files on the designated local folder, gather all the links and export them into a markdown file with the links categorised internally by filename, and export gathered statistics about both the YouTube links and the process itself.

## File Structure
- export
  - all_video_link.md
  - console_log.txt
  - video_statistic.txt
- src
  - video_statistic_1.py
  - video_statistic_2.py
- .gitattributes
- .gitignore
- LICENSE
- README.md
- requirements.txt

The folder "export" wan't included in this repo because the included links are unlisted videos.</br>
"video_statistic_1.py" Reads content-limited links from provided markdown file.
"video_statistic_2.py" Reads links from random markdown file, generate markdown file with read links in it, and generate related stats in a txt file.

## Export File Content
### all_video_link.md
```
# file 1.md</br>
http...</br>
http...</br>
http...</br>
# file 2.md</br>
http...</br>
http...</br>
http...</br>
......</br>
```
### video_statistic.txt
```
Total video count: ?</br>
Total video length(s): ? seconds</br>
Total video length(hms): ? hours ? minutes ? seconds</br>
Execute at ?-?-? ?:?:?</br>
```

## Requirement
pytube==12.1.0
