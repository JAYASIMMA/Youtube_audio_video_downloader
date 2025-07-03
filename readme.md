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
``

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
   python youtube.py
   python playlist_yt.py
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
## Screenshots
![bandicam 2025-07-01 23-17-03-679](https://github.com/user-attachments/assets/fab097d1-b1d7-4c9b-89f0-2e59a12d2a82)
![bandicam 2025-07-01 23-17-17-329](https://github.com/user-attachments/assets/5dd4c1de-dfab-40a4-b3dd-7e1a66d5ab63)
![bandicam 2025-07-01 23-17-23-332](https://github.com/user-attachments/assets/5bcc9137-dd26-4ffa-9488-f9dfbf911c4c)
![bandicam 2025-07-01 23-18-14-376](https://github.com/user-attachments/assets/cbed48ca-6f29-48f1-ae62-c51eebea9cd5)
![bandicam 2025-07-01 23-19-58-932](https://github.com/user-attachments/assets/707a4f63-b094-4ce7-9ef0-43f78dd38b1a)
![bandicam 2025-07-01 23-20-51-032](https://github.com/user-attachments/assets/41e8223c-467c-4635-ab25-5c716635de05)
![bandicam 2025-07-01 23-21-00-731](https://github.com/user-attachments/assets/cd0c43ac-2908-4467-bf99-a341621a4087)
![bandicam 2025-07-01 23-21-40-535](https://github.com/user-attachments/assets/feaacd1d-298c-41a3-84c3-5ab758784e41)
![Upload![Screenshot 2025-07-01 233255](https://github.com/user-attachments/assets/4d868510-9299-4e27-886e-6643f64f1fa4)
![Screenshot 2025-07-01 233255](https://github.com/user-attachments/assets/75916726-75a8-439a-a517-9f2306fdfdf0)
![Screenshot ![Screenshot 2025-07-01 233533](https://github.com/user-attachments/assets/ae9fae92-ffac-4e42-a802-f915e6a8e464)
2025-07-01 233542](https://github.com/user-attachments/assets/b60a53f5-7c7a-4504-8756-d452113c21c6)
ing Screenshot 2025-07-01 233533.png…]()
![Screenshot 2025-07-01 233542](https://github.com/user-attachments/assets/e57c2852-3207-4cf0-894a-e7ddea4f4e0a)
![Screenshot 2025-07-01 233533](https://github.com/user-attachments/assets/1352f4de-cedb-4d57-b4f2-60126e2f4a0c)
![Screenshot 2025-07-01 233255](https://github.com/user-attachments/assets/5cf5d096-8a42-4f00-808d-a6726eb2ebbc)
![Screenshot 2025-07-01 233602](https://github.com/user-attachments/assets/f6f3c2b7-640d-4e70-97dd-f0601dbb3f24)
![Screenshot 2025-07-01 233533](https://github.com/user-attachments/assets/3c227460-79f0-420c-90d7-fd5d9ae3e435)
![Screenshot 2025-07-01 233255](https://github.com/user-attachments/assets/d295fd80-2792-477d-9bd2-55c408e7ddf6)
![Screenshot 2025-07-01 233614](https://github.com/user-attachmen![Screenshot 2025-07-01 233542](https://github.com/user-attachments/assets/843ab2f4-59bc-41d7-b989-6d799b19638a)
ts/ass![Screenshot 2025-07-01 233602](https://github.com/user-attachments/assets/6c6d61c7-9afd-44c2-8373-01916e0c1642)
ets/21100b06-fa0a-4858-b802-3f5c56d0a8de)
![Screenshot 2025-07-01 233542](https://github.com/user-attachments/assets/9d2febb7-31fc-4fcc-9069-0249377118eb)
![Uploading Screenshot 2025-07-01 233602.png…]()
![Screenshot 2025-07-01 233614](https://github.com/user-attachments/assets/df1258c6-906b-4a6a-9b16-a792168ddb24)
![Screenshot 2025-07-01 233707](https://github.com/user-attachments/assets/2a577be1-bb28-4286-a708-e8dc45606282)
![Screenshot 2025-07-01 233757](https://github.com/user-attachments/assets/cdf92ae1-d59f-4deb-9e02-3f257eed96b2)
![Screenshot 2025-07-01 233811](https://github.com/user-attachments/assets/6995bfed-ef62-4b00-aa9b-3c6318717ad8)
![Screenshot 2025-07-01 233828](https://github.com/user-attachments/assets/0ef41760-302c-4ae9-9a2b-e457581bb670)

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
