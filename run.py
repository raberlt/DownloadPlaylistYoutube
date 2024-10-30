import yt_dlp

# Nhập URL của playlist mà bạn muốn tải xuống
playlist_url = input("Nhập URL của playlist YouTube: ")

# Đặt thư mục lưu video
download_path = './youtube_playlist'

# Tùy chọn tải video với yt-dlp
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Chọn video và âm thanh có định dạng mp4 và m4a
    'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Đặt tên file và đường dẫn
    'noplaylist': False,  # Tải toàn bộ playlist
    'ignoreerrors': True,  # Bỏ qua các video lỗi
}

# Tải playlist
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    print("Đang tải playlist...")
    ydl.download([playlist_url])

print("Tải xuống hoàn tất!")
