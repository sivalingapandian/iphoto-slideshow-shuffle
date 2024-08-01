# Script to shuffle images for slideshow using iPhoto on mac
### Randomize image file meta data date and time

Why do we need this? When creating slideshow using iPhoto on mac it always goes by captured order. But at times we may want the pics to be randomized. There is no way other than changing the source file meta data. This python program copies file from one directory to other and changing create/modified time by 1 sec interval. If it is image file it also changes meta data of timestamp.

Make sure to install pillow

```shell
pip3 install pillow
```

```shell
python3 ./pyton/copy-files-with-random-date.py
```

Find AI [prompt](/ai-prompt/prompt.pdf) file to understand how this program evolved