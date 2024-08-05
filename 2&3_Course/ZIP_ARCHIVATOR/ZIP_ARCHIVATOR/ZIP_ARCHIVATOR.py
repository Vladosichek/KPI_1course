import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo
import zipfile
import subprocess
import shutil
import os
import hashlib
import bencodepy


class ZipArchivator:
    def __init__(self, root):
        self.root = root
        self.root.title("ZIP Archivator (Alpha version)")

        self.file_tree = ttk.Treeview(self.root)
        self.file_tree.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

        self.scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.file_tree.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_tree.configure(yscrollcommand=self.scrollbar.set)

        self.file_tree.bind("<Double-1>", self.expand_file_contents)

        zip_button = tk.Button(self.root, text="Zip Files", width=20, command=self.zip_files)
        zip_button.pack(pady=5)

        unzip_button = tk.Button(self.root, text="Unzip Archive", width=20, command=self.unzip_archive)
        unzip_button.pack(pady=5)

        view_button = tk.Button(self.root, text="View Archive Contents", width=20, command=self.view_archive_contents)
        view_button.pack(pady=5)

        share_button = tk.Button(self.root, text="Share Archive", width=20, command=self.share_archive)
        share_button.pack(pady=5)

        create_torrent_button = tk.Button(self.root, text="Create Torrent", width=20, command=self.create_torrent)
        create_torrent_button.pack(pady=5)

        change_button = tk.Button(self.root, text="Change format", width=20, command=self.share_archive)
        change_button.pack(pady=5)

    def zip_files(self):
        files = filedialog.askopenfilenames(title="Select files to zip", filetypes=(("All files", "*.*"),))
        if files:
            save_path = filedialog.askdirectory(title="Select folder to save the archive")
            if save_path:
                archive_name = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=(("ZIP files", "*.zip"),),
                                                            initialdir=save_path, initialfile="archive.zip")
                if archive_name:
                    with zipfile.ZipFile(archive_name, "w") as zip_file:
                        for file in files:
                            zip_file.write(file, os.path.basename(file))

    def unzip_archive(self):
        archive_path = filedialog.askopenfilename(title="Select archive to unzip", filetypes=(("ZIP files", "*.zip"),))
        if archive_path:
            extract_path = filedialog.askdirectory(title="Select extraction folder")
            if extract_path:
                with zipfile.ZipFile(archive_path, "r") as zip_file:
                    zip_file.extractall(extract_path)

    def view_archive_contents(self):
        archive_path = filedialog.askopenfilename(title="Select archive to view contents", filetypes=(("ZIP files", "*.zip"),))
        if archive_path:
            self.file_tree.delete(*self.file_tree.get_children())
            with zipfile.ZipFile(archive_path, "r") as zip_file:
                for file in zip_file.namelist():
                    self.file_tree.insert("", "end", text=file, values=(file,))

    def expand_file_contents(self, event):
        item = self.file_tree.selection()[0]
        file_path = self.file_tree.item(item)["values"][0]

        if file_path:
            archive_path = filedialog.askopenfilename(title="Select archive to view file contents",
                                                      filetypes=(("ZIP files", "*.zip"),))
            if archive_path:
                with zipfile.ZipFile(archive_path, "r") as zip_file:
                    file_content = zip_file.read(file_path).decode("utf-8", errors="ignore")

                content_window = tk.Toplevel(self.root)
                content_window.title("File Content")

                text_area = tk.Text(content_window)
                text_area.pack(fill=tk.BOTH, expand=True)
                text_area.insert(tk.END, file_content)
                text_area.config(state=tk.DISABLED)

                replace_button = tk.Button(content_window, text="Replace File",
                                           command=lambda: self.replace_file(archive_path, file_path))
                replace_button.pack(pady=5)

    def replace_file(self, archive_path, file_path):
        new_file_path = filedialog.askopenfilename(title="Select new file to replace",
                                                   filetypes=(("All files", "*.*"),))
        if new_file_path:
            temp_path = os.path.join(os.path.dirname(archive_path), "temp.zip")
            with zipfile.ZipFile(archive_path, "r") as zip_file, zipfile.ZipFile(temp_path, "w") as temp_zip:
                for item in zip_file.infolist():
                    if item.filename != file_path:
                        temp_zip.writestr(item, zip_file.read(item.filename))
                temp_zip.write(new_file_path, file_path)

            shutil.move(temp_path, archive_path)

            # Update the archive contents view
            self.view_archive_contents()

    def share_archive(self):
        showinfo("Error!", "This option is not allowed in demo version!")
        #archive_path = filedialog.askopenfilename(title="Select archive to share", filetypes=(("ZIP files", "*.zip"),))
        #if archive_path:
        #    subprocess.Popen(['xdg-open', archive_path])  # Opens the archive with the default application

    def create_torrent(self):
        archive_path = filedialog.askopenfilename(title="Select archive to create a torrent", filetypes=(("ZIP files", "*.zip"),))
        if archive_path:
            save_path = filedialog.askdirectory(title="Select folder to save the torrent")
            if save_path:
                torrent_name = filedialog.asksaveasfilename(defaultextension=".torrent", filetypes=(("Torrent files", "*.torrent"),),
                                                            initialdir=save_path, initialfile="archive.torrent")
                if torrent_name:
                    info = {
                        'length': os.path.getsize(archive_path),
                        'name': os.path.basename(archive_path),
                        'piece length': 2**19,  # 512 KB
                        'pieces': b''.join(self.calculate_piece_hashes(archive_path))
                    }

                    torrent = {
                        'announce': '',
                        'info': info
                    }

                    with open(torrent_name, 'wb') as torrent_file:
                        torrent_file.write(bencodepy.encode(torrent))

    def calculate_piece_hashes(self, file_path):
        piece_hashes = []
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(2**19)  # 512 KB
                if not data:
                    break
                piece_hashes.append(hashlib.sha1(data).digest())
        return piece_hashes


if __name__ == "__main__":
    root = tk.Tk()
    zip_archivator = ZipArchivator(root)
    root.mainloop()
