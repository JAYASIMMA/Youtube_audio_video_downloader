import os
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.properties import StringProperty
import yt_dlp
from kivy.lang import Builder

FFMPEG_PATH = r"E:\youtube _video downloader\upload\bin"


class PlaylistDownloader(BoxLayout):
    status = StringProperty("")
    format_choice = StringProperty("MP4")

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=10, padding=20, **kwargs)
        Builder.load_file("playlist.kv")
        self.add_widget(Label(text="YouTube Playlist URL:"))
        self.url_input = TextInput(multiline=False, size_hint_y=None, height=40)
        self.add_widget(self.url_input)

        self.add_widget(Label(text="Output Folder Name:"))
        self.folder_input = TextInput(multiline=False, size_hint_y=None, height=40)
        self.add_widget(self.folder_input)

        format_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        self.mp4_btn = ToggleButton(text="MP4", group="format", state="down")
        self.mp3_btn = ToggleButton(text="MP3", group="format")
        self.mp4_btn.bind(on_press=self.set_format)
        self.mp3_btn.bind(on_press=self.set_format)
        format_layout.add_widget(self.mp4_btn)
        format_layout.add_widget(self.mp3_btn)
        self.add_widget(format_layout)

        self.download_btn = Button(text="Download Playlist", size_hint_y=None, height=50)
        self.download_btn.bind(on_press=self.start_download)
        self.add_widget(self.download_btn)

        self.status_label = Label(text="")
        self.add_widget(self.status_label)

    def set_format(self, instance):
        self.format_choice = instance.text
        self.status = f"Format set to {self.format_choice}"
        self.status_label.text = self.status

    def start_download(self, instance):
        threading.Thread(target=self.download).start()

    def download(self):
        url = self.url_input.text.strip()
        folder_name = self.folder_input.text.strip()

        if not url:
            self.status = "Please enter a Playlist URL."
            self.status_label.text = self.status
            return

        if not folder_name:
            self.status = "Please enter an output folder name."
            self.status_label.text = self.status
            return

        out_folder = os.path.join("downloads", folder_name)
        os.makedirs(out_folder, exist_ok=True)

        self.status = "Downloading playlist..."
        self.status_label.text = self.status

        ydl_opts = {
            'outtmpl': os.path.join(out_folder, '%(playlist_index)s - %(title)s.%(ext)s'),
            'ffmpeg_location': FFMPEG_PATH,
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
            ydl_opts.update({'format': 'best'})

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status = f"Download complete! Check the folder: downloads/{folder_name}"
        except Exception as e:
            self.status = f"Download failed: {e}"

        self.status_label.text = self.status


class PlaylistDownloaderApp(App):
    def build(self):
        return PlaylistDownloader()


if __name__ == '__main__':
    PlaylistDownloaderApp().run()
