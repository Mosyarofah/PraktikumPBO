import tkinter as tk
from tkinter import messagebox, ttk, simpledialog


class Tugas:
    def __init__(self, judul, status="Belum Selesai"):
        self.judul = judul
        self.status = status


class AplikasiTodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Tugas (To-Do List)")
        self.root.geometry("600x400")

        # =========================
        # b. List of objects
        # =========================
        self.daftar_tugas = []

        # Frame input
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Nama Tugas:").grid(row=0, column=0, sticky=tk.W)
        self.entry_tugas = tk.Entry(frame_input, width=40)
        self.entry_tugas.grid(row=0, column=1, padx=5)

        # Frame tombol
        frame_tombol = tk.Frame(root, padx=10, pady=10)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Tambah", command=self.tambah_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Edit", command=self.edit_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus", command=self.hapus_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Tandai Selesai", command=self.tandai_selesai).pack(side=tk.LEFT, padx=5)

        # =========================
        # d. Treeview
        # =========================
        frame_tabel = tk.Frame(root, padx=10, pady=10)
        frame_tabel.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(
            frame_tabel,
            columns=("Tugas", "Status"),
            show="headings"
        )
        self.tree.heading("Tugas", text="Nama Tugas")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame_tabel, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # =========================
    # c. Fitur tambah tugas
    # =========================
    def tambah_tugas(self):
        judul = self.entry_tugas.get()
        if judul:
            tugas_baru = Tugas(judul)
            self.daftar_tugas.append(tugas_baru)
            self.tree.insert("", tk.END, values=(judul, tugas_baru.status))
            self.entry_tugas.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Nama tugas tidak boleh kosong!")

    # =========================
    # c. Fitur hapus tugas
    # =========================
    def hapus_tugas(self):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            judul = item["values"][0]

            self.daftar_tugas = [t for t in self.daftar_tugas if t.judul != judul]
            self.tree.delete(selected[0])
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!")

    # =========================
    # c. Fitur edit tugas
    # =========================
    def edit_tugas(self):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            judul_lama = item["values"][0]

            judul_baru = simpledialog.askstring("Edit Tugas", "Masukkan nama tugas baru:")
            if judul_baru:
                for tugas in self.daftar_tugas:
                    if tugas.judul == judul_lama:
                        tugas.judul = judul_baru
                        break

                status = item["values"][1]
                self.tree.item(selected[0], values=(judul_baru, status))
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan diedit!")

    # =========================
    # c. Tandai selesai
    # =========================
    def tandai_selesai(self):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            judul = item["values"][0]

            for tugas in self.daftar_tugas:
                if tugas.judul == judul:
                    tugas.status = "Selesai"
                    break

            self.tree.item(selected[0], values=(judul, "Selesai"))
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiTodoList(root)
    root.mainloop()
