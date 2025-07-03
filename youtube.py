import os
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import StringProperty
from kivy.lang import Builder
import yt_dlp

FFMPEG_PATH = r"C:\ffmpeg-7.1.1-full_build\bin"

video_formats = []


class MyLogger:
    """Optional logger for yt_dlp (safe)"""
    def debug(self, msg):
        print(msg)
    def warning(self, msg):
        print(f"WARNING: {msg}")
    def error(self, msg):
        print(f"ERROR: {msg}")


class YouTubeDownloader(BoxLayout):
    status = StringProperty("")
    format_choice = StringProperty("MP4")

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=10, padding=20, **kwargs)

        Builder.load_file("you.kv")

        self.add_widget(Label(text="YouTube URL:"))
        self.url_input = TextInput(multiline=False, size_hint_y=None, height=40)
        self.add_widget(self.url_input)

        format_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        self.mp4_btn = ToggleButton(text="MP4", group="format", state="down")
        self.mp3_btn = ToggleButton(text="MP3", group="format")
        self.mp4_btn.bind(on_press=self.set_format)
        self.mp3_btn.bind(on_press=self.set_format)
        format_layout.add_widget(self.mp4_btn)
        format_layout.add_widget(self.mp3_btn)
        self.add_widget(format_layout)

        self.fetch_btn = Button(text="Fetch Resolutions", size_hint_y=None, height=40)
        self.fetch_btn.bind(on_press=self.fetch_resolutions)
        self.add_widget(self.fetch_btn)

        self.add_widget(Label(text="Select Resolution:"))
        self.res_spinner = Spinner(text="Select Resolution", values=[])
        self.add_widget(self.res_spinner)

        self.download_btn = Button(text="Download", size_hint_y=None, height=50)
        self.download_btn.bind(on_press=self.start_download)
        self.add_widget(self.download_btn)

        self.status_label = Label(text="")
        self.add_widget(self.status_label)

    def set_format(self, instance):
        self.format_choice = instance.text
        self.status = f"Format set to {self.format_choice}"
        self.status_label.text = self.status

    def fetch_resolutions(self, instance):
        url = self.url_input.text.strip()
        if not url:
            self.status = "Please enter a URL."
            self.status_label.text = self.status
            return

        def fetch():
            global video_formats
            self.status = "Fetching video info..."
            self.status_label.text = self.status

            ydl_opts = {
                'quiet': True,
                'skip_download': True,
                'ffmpeg_location': FFMPEG_PATH,
                'logger': MyLogger(),
            }

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_formats = [
                        f for f in info['formats']
                        if f['ext'] == 'mp4' and f.get('height') is not None and f.get('acodec') != 'none'
                    ]
                    video_formats.sort(key=lambda x: x['height'], reverse=True)
                    choices = [f"{f['height']}p" for f in video_formats]

                    if choices:
                        self.res_spinner.values = choices
                        self.res_spinner.text = choices[0]
                        self.status = "Resolutions loaded."
                    else:
                        self.status = "No MP4 resolutions found."

            except Exception as e:
                self.status = f"Error: {e}"

            self.status_label.text = self.status

        threading.Thread(target=fetch).start()

    def start_download(self, instance):
        threading.Thread(target=self.download).start()

    def download(self):
        url = self.url_input.text.strip()
        if not url:
            self.status = "Please enter a URL."
            self.status_label.text = self.status
            return

        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        self.status = "Downloading..."
        self.status_label.text = self.status

        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'ffmpeg_location': FFMPEG_PATH,
            'logger': MyLogger(),
        }

        if self.format_choice == "MP3":
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        else:
            selected = self.res_spinner.text.replace('p', '')
            selected_format = next((f for f in video_formats if str(f['height']) == selected), None)
            if selected_format:
                ydl_opts.update({'format': f"{selected_format['format_id']}"})
            else:
                self.status = "No valid resolution selected."
                self.status_label.text = self.status
                return

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status = "Download complete! Check downloads/"
        except Exception as e:
            self.status = f"Download failed: {e}"

        self.status_label.text = self.status


class YouTubeDownloaderApp(App):
    def build(self):
        return YouTubeDownloader()


if __name__ == '__main__':
    YouTubeDownloaderApp().run()
