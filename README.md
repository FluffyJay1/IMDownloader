# ImDownloader

Small python script to bypass login requirements to download galleries from IMHentai

I wrote this out of spite for the people who coded IMHentai's download function, maybe also for the 2 other people in the world who would find a use for this

## Usage

`python imdownloader.py <url>`

Takes in only 1 argument, which is the url of the gallery you want (like https://imhentai.xxx/gallery/######)

Creates a folder in the same directory with the name of the gallery, and downloads the images inside.

Requires the `requests` module.