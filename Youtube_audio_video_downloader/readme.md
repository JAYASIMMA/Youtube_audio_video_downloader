# 🎥 YouTube Playlist Downloader

A simple, user-friendly desktop app to download entire YouTube playlists in **MP4 (video)** or **MP3 (audio)** format — organized neatly in custom folders with a clean modern UI.

---

## ✨ **Features**

- 🔗 **Paste once, download all** — fetches every video in a playlist automatically.
- 🎞️ **Video (MP4)** or 🎵 **Audio (MP3)** — pick your preferred format.
- 📁 **Custom folder names** — each playlist is saved in its own tidy folder.
- ⚡ **Modern GUI** — intuitive and beginner-friendly, no technical steps needed.

---

## 📦 **Tech Stack**

- **Python** — simple, cross-platform.
- **Kivy** — for the responsive desktop interface.
- Uses robust open-source tools under the hood for high-quality downloads.

---

## 🚀 **How to Run**

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/playlist-downloader.git
   cd playlist-downloader
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install [FFmpeg](https://ffmpeg.org/)**

   * Download & unzip FFmpeg
   * Add its `/bin` folder to your system `PATH`
   * Or set its path in the Python script (see `FFMPEG_PATH`).

4. **Run the app**

   ```bash
   python playlist_downloader.py
   ```

---

## ✅ **Usage**

1. Paste a **YouTube playlist link**.
2. Enter a **folder name** (e.g., `MyFavSongs`).
3. Choose **MP4** or **MP3**.
4. Click **Download Playlist**.
5. Check the `downloads/` folder for all files.

---

## 📂 **Output**

Your downloads are saved like:

```
downloads/
 └── MyFavSongs/
      ├── 01 - Video Title.mp4
      ├── 02 - Video Title.mp4
      ├── ...
```

Or as `.mp3` files if you pick audio.

---

## 🛠️ **Why this project?**

Sometimes you find a goldmine of tutorials, music, or lectures — but downloading each video one by one is tedious.
This tool does it all in a single click — no fuss.

---

## 🤝 **Contributing**

Got ideas? Found a bug? Want to extend this with more formats or features?

* Open an **issue**
* Submit a **pull request**
* Or just **reach out** — happy to collaborate!

---

## 📜 **License**

Open-sourced under the **MIT License** — feel free to fork, modify, and share!

---

## 🙌 **Let’s Connect**

If you like simple, practical projects like this —
**star this repo ⭐**, share your thoughts, or connect with me here on [LinkedIn](#).

---

**Happy downloading!** 🎉

```
