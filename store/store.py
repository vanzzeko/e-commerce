from Tkinter import *
from datetime import datetime, timedelta
import sqlite3

def login () :
    f_signup.pack_forget()
    f_profile.pack_forget()
    f_dashboard.pack_forget()
    f_login.pack()

    Label(f_login, text="Username").grid(row=0, column=0, sticky=W)
    username_entry = Entry(f_login, textvariable=username_login_var)
    username_entry.grid(row=0, column=1, sticky=W)
    Label(f_login, text="Password").grid(row=1, column=0, sticky=W)
    pass_entry = Entry(f_login, textvariable=pass_login_var, show='*')
    pass_entry.grid(row=1, column=1, sticky=W)
    Button(f_login, text="Login", command=do_login).grid(row=2, column=0, sticky=W)
    Button(f_login, text="Signup", command=signup).grid(row=2, column=1, sticky=W)

def signup () :
    f_login.pack_forget()
    f_signup.pack()

    Label(f_signup, text="Username").grid(row=0, column=0, sticky=W)
    username_entry = Entry(f_signup, textvariable=username_signup_var)
    username_entry.grid(row=0, column=1, sticky=W)
    Label(f_signup, text="Password").grid(row=1, column=0, sticky=W)
    pass_entry = Entry(f_signup, textvariable=pass_signup_var, show='*')
    pass_entry.grid(row=1, column=1, sticky=W)
    Label(f_signup, text="Email").grid(row=2, column=0, sticky=W)
    email_entry = Entry(f_signup, textvariable=email_signup_var)
    email_entry.grid(row=2, column=1, sticky=W)    
    Label(f_signup, text="Full Name").grid(row=3, column=0, sticky=W)
    fullname_entry = Entry(f_signup, textvariable=fullname_signup_var)
    fullname_entry.grid(row=3, column=1, sticky=W)    
    Button(f_signup, text="Signup", command=do_signup).grid(row=4, column=0, sticky=W)
    Button(f_signup, text="Back", command=login).grid(row=4, column=1, sticky=W)    

def do_signup() :
    conn = connect_database()
    print(conn)

    c = conn.cursor()
    a_username = username_signup_var.get()
    a_pass = pass_signup_var.get()
    a_email= email_signup_var.get()
    a_full_name = fullname_signup_var.get()
    now = datetime.now()
    c.execute("INSERT INTO users(username, password, email, full_name, created, modified) VALUES (?,?,?,?,?,?)", (a_username,a_pass,a_email,a_full_name,now,a_username))
    conn.commit()
    conn.close()
    print("Signup Successfull")
    username_signup_var.set("")
    pass_signup_var.set("")
    email_signup_var.set("")
    fullname_signup_var.set("")

    login()

def do_login() :
    conn = connect_database()
    print(conn)

    a_username = username_login_var.get()
    a_pass = pass_login_var.get()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = '" + a_username + "' AND password='" + a_pass + "'")
    rows = c.fetchall()

    for row in rows:
        data = row

        if a_username == 'admin':
            role = "admin"
            print (role)
            admin_dashboard()
            break
        else:
            role = "user"
            user_id = data[0]

            c = conn.cursor()
            c.execute("UPDATE temp SET user_id = ? WHERE id = ?", (user_id,1))
            conn.commit()
            conn.close()
            
            profile()
            break
    else:
        print("not found")
        Label(f_login, text="Invalid login", fg="red").grid(row=3, column=0, sticky=W) 

def profile() :
    f_login.pack_forget()
    f_edit_profile.pack_forget()
    f_view_barang.pack_forget()
    f_view_cart.pack_forget()
    f_konfirmasi_pembayaran.pack_forget()    
    f_profile.pack()

    Button(f_profile, text="Edit Profile", command=panel_edit_profile).grid(row=0, column=0, sticky=W)
    Button(f_profile, text="View Barang", command=panel_view_barang).grid(row=0, column=1, sticky=W)
    Button(f_profile, text="View Cart", command=view_cart).grid(row=1, column=0, sticky=W)
    Button(f_profile, text="Konfirmasi Pembayaran", command=panel_konfirmasi_pembayaran).grid(row=1, column=1, sticky=W)
    Button(f_profile, text="Logout",command=do_logout).grid(row=2, column=0, sticky=W)

def admin_dashboard() :
    f_login.pack_forget()
    f_tambah_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_view_invoice.pack_forget()
    f_view_konfirmasi_pembayaran.pack_forget()
    f_hapus_kategori.pack_forget()
    f_view_barang_admin.pack_forget()
    f_tambah_kategori.pack_forget()
    f_edit_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_invoice_detail.pack_forget()
    f_dashboard.pack()    

    Button(f_dashboard, text="Tambah Kategori", command=panel_tambah_kategori).grid(row=0, column=0, sticky=W)
    Button(f_dashboard, text="Hapus Kategori", command=panel_hapus_kategori).grid(row=0, column=2, sticky=W)
    Button(f_dashboard, text="Tambah Barang", command=panel_tambah_barang).grid(row=1, column=0, sticky=W)
    Button(f_dashboard, text="Edit Barang", command=panel_edit_barang).grid(row=1, column=1, sticky=W)
    Button(f_dashboard, text="Hapus Barang", command=panel_hapus_barang).grid(row=1, column=2, sticky=W)
    Button(f_dashboard, text="View Barang", command=panel_view_barang_admin).grid(row=2, column=0, sticky=W)
    Button(f_dashboard, text="View Invoice",command=view_invoice).grid(row=2, column=1, sticky=W)
    Button(f_dashboard, text="View Konfirmasi Pembayaran",command=view_konfirmasi_pembayaran).grid(row=2, column=2, sticky=W)
    Button(f_dashboard, text="Logout",command=do_logout).grid(row=3, column=0, sticky=W)

def panel_view_barang_admin() :
    f_dashboard.pack_forget()
    f_tambah_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_view_invoice.pack_forget()
    f_view_konfirmasi_pembayaran.pack_forget()
    f_hapus_kategori.pack_forget()
    f_view_barang_admin.pack()
    f_tambah_kategori.pack_forget()
    f_edit_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_invoice_detail.pack_forget()    
    
    for label in f_view_barang_admin.grid_slaves():
      label.grid_forget()
      
    conn = connect_database()
    print(conn)

    c = conn.cursor()
    c.execute("SELECT * FROM barang ORDER BY id DESC")
    rows = c.fetchall()

    i = -1
    for row in rows:
        data = row
        i = i+1

        Label(f_view_barang_admin, text=row[2]).grid(row=i, column=0, sticky=W)
        Label(f_view_barang_admin, text=row[3]).grid(row=i, column=1, sticky=W)
        Label(f_view_barang_admin, text=row[4]).grid(row=i, column=2, sticky=W)

    b=Button(f_view_barang_admin, text="Back",command=back_to_dashboard).grid(row=12, column=0, sticky=W)

def panel_tambah_kategori() :
    f_dashboard.pack_forget()
    f_tambah_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_view_invoice.pack_forget()
    f_view_konfirmasi_pembayaran.pack_forget()
    f_hapus_kategori.pack_forget()
    f_view_barang_admin.pack_forget()
    f_tambah_kategori.pack()
    f_edit_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_invoice_detail.pack_forget()    

    Label(f_tambah_kategori, text="Nama").grid(row=0, column=0, sticky=W)
    nama_entry = Entry(f_tambah_kategori, textvariable=nama_kategori)
    nama_entry.grid(row=0, column=1, sticky=W)
    Button(f_tambah_kategori, text="Simpan",command=simpan_kategori).grid(row=1, column=0, sticky=W)
    Button(f_tambah_kategori, text="Kembali",command=back_to_dashboard).grid(row=1, column=1, sticky=W)

def simpan_kategori() :
    conn = connect_database()
    print(conn)

    c = conn.cursor()
    a_nama_kategori = nama_kategori.get()
    c.execute("INSERT INTO kategori(name) VALUES('" + a_nama_kategori + "')")
    conn.commit()
    conn.close()
    print("Tambah data kategori Successfull")
    nama_kategori.set("")

def panel_hapus_kategori() :
    f_dashboard.pack_forget()
    f_tambah_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_view_invoice.pack_forget()
    f_view_konfirmasi_pembayaran.pack_forget()
    f_hapus_kategori.pack()
    f_view_barang_admin.pack_forget()
    f_tambah_kategori.pack_forget()
    f_edit_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_invoice_detail.pack_forget()    

    Label(f_hapus_kategori, text="Nama").grid(row=0, column=0, sticky=W)
    nama_entry = Entry(f_hapus_kategori, textvariable=nama_kategori)
    nama_entry.grid(row=0, column=1, sticky=W)
    Button(f_hapus_kategori, text="Hapus",command=hapus_kategori).grid(row=1, column=0, sticky=W)
    Button(f_hapus_kategori, text="Kembali",command=back_to_dashboard).grid(row=1, column=1, sticky=W)

def hapus_kategori() :
    conn = connect_database()
    print(conn)

    c = conn.cursor()
    a_nama_kategori = nama_kategori.get()
    c.execute("DELETE FROM kategori WHERE name ='" + a_nama_kategori + "'")
    conn.commit()
    conn.close()
    print("Hapus data kategori Successfull")
    nama_kategori.set("")

def panel_tambah_barang() :
    f_dashboard.pack_forget()
    f_tambah_barang.pack()
    f_hapus_barang.pack_forget()
    f_view_invoice.pack_forget()
    f_view_konfirmasi_pembayaran.pack_forget()
    f_hapus_kategori.pack_forget()
    f_view_barang_admin.pack_forget()
    f_tambah_kategori.pack_forget()
    f_edit_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_invoice_detail.pack_forget()

    Label(f_tambah_barang, text="Nama Kategori").grid(row=0, column=0, sticky=W)
    nama_kategori_entry = Entry(f_tambah_barang, textvariable=nama_kategori)
    nama_kategori_entry.grid(row=0, column=1, sticky=W)
    Label(f_tambah_barang, text="Nama Barang").grid(row=1, column=0, sticky=W)
    nama_barang_entry = Entry(f_tambah_barang, textvariable=nama_barang)
    nama_barang_entry.grid(row=1, column=1, sticky=W)
    Label(f_tambah_barang, text="Qty").grid(row=2, column=0, sticky=W)
    qty_entry = Entry(f_tambah_barang, textvariable=qty)
    qty_entry.grid(row=2, column=1, sticky=W)
    Label(f_tambah_barang, text="Harga").grid(row=3, column=0, sticky=W)
    harga_entry = Entry(f_tambah_barang, textvariable=harga)
    harga_entry.grid(row=3, column=1, sticky=W)    
    Button(f_tambah_barang, text="Simpan",command=simpan_barang).grid(row=4, column=0, sticky=W)
    Button(f_tambah_barang, text="Kembali",command=back_to_dashboard).grid(row=4, column=1, sticky=W)

def panel_edit_barang() :
    f_dashboard.pack_forget()
    f_tambah_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_view_invoice.pack_forget()
    f_view_konfirmasi_pembayaran.pack_forget()
    f_hapus_kategori.pack_forget()
    f_view_barang_admin.pack_forget()
    f_tambah_kategori.pack_forget()
    f_edit_barang.pack()
    f_hapus_barang.pack_forget()
    f_invoice_detail.pack_forget()    
    

    Label(f_edit_barang, text="Nama Barang").grid(row=0, column=0, sticky=W)
    nama_barang_entry = Entry(f_edit_barang, textvariable=nama_barang)
    nama_barang_entry.grid(row=0, column=1, sticky=W)
    Label(f_edit_barang, text="Nama Kategori").grid(row=1, column=0, sticky=W)
    nama_kategori_entry = Entry(f_edit_barang, textvariable=nama_kategori)
    nama_kategori_entry.grid(row=1, column=1, sticky=W)
    Label(f_edit_barang, text="Qty").grid(row=2, column=0, sticky=W)
    qty_entry = Entry(f_edit_barang, textvariable=qty)
    qty_entry.grid(row=2, column=1, sticky=W)
    Label(f_edit_barang, text="Harga").grid(row=3, column=0, sticky=W)
    harga_entry = Entry(f_edit_barang, textvariable=harga)
    harga_entry.grid(row=3, column=1, sticky=W)    
    Button(f_edit_barang, text="Update",command=update_barang).grid(row=4, column=0, sticky=W)
    Button(f_edit_barang, text="Kembali",command=back_to_dashboard).grid(row=4, column=1, sticky=W)

def panel_hapus_barang() :
    f_dashboard.pack_forget()
    f_tambah_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_view_invoice.pack_forget()
    f_view_konfirmasi_pembayaran.pack_forget()
    f_hapus_kategori.pack_forget()
    f_view_barang_admin.pack_forget()
    f_tambah_kategori.pack_forget()
    f_edit_barang.pack_forget()
    f_hapus_barang.pack()
    f_invoice_detail.pack_forget()    

    Label(f_hapus_barang, text="Nama").grid(row=0, column=0, sticky=W)
    nama_entry = Entry(f_hapus_barang, textvariable=nama_barang)
    nama_entry.grid(row=0, column=1, sticky=W)
    Button(f_hapus_barang, text="Hapus",command=hapus_barang).grid(row=1, column=0, sticky=W)
    Button(f_hapus_barang, text="Kembali",command=back_to_dashboard).grid(row=1, column=1, sticky=W)

def simpan_barang() :
    conn = connect_database()
    print(conn)

    a_nama_kategori = nama_kategori.get().lower()
    a_nama_barang = nama_barang.get()
    a_qty = qty.get()
    a_harga = harga.get()
    
    # get category id
    c = conn.cursor()
    c.execute("SELECT * FROM kategori WHERE LOWER(name) = '" + a_nama_kategori + "'")
    row = c.fetchone()

    if row is None:
        print("Kategori tidak ditemukan")
    elif len(a_nama_barang) > 0 and a_qty > 0 and a_harga > 0:
        kategori_id = row[0]
        c = conn.cursor()
        c.execute("INSERT INTO barang(kategori_id, nama, qty, harga) VALUES (?,?,?,?)", (kategori_id,a_nama_barang,a_qty,a_harga))
        conn.commit()
        conn.close()
        print("Tambah data barang Successfull")
        nama_kategori.set("")
        nama_barang.set("")
        qty.set("")
        harga.set("")

def update_barang() :
    conn = connect_database()
    print(conn)

    a_nama_kategori = nama_kategori.get().lower()
    a_nama_barang = nama_barang.get()
    a_qty = qty.get()
    a_harga = harga.get()

    if len(a_nama_kategori) > 0 and len(a_nama_barang) > 0 and a_qty > 0 and a_harga > 0:
        # get category id
        c = conn.cursor()
        c.execute("SELECT * FROM kategori WHERE LOWER(name) = '" + a_nama_kategori + "'")
        row = c.fetchone()

        if row is None:
            print("Kategori tidak ditemukan")
        else:
            kategori_id = row[0]

        # get id barang
        c = conn.cursor()
        c.execute("SELECT * FROM barang WHERE LOWER(nama) = '" + a_nama_barang + "'")
        row = c.fetchone()
        if row is None:
            print("Barang tidak ditemukan")
        else:
            barang_id = row[0]


        c = conn.cursor()
        c.execute("UPDATE barang SET kategori_id = ?, qty=?, harga = ? WHERE id = ?", (kategori_id,a_qty,a_harga, barang_id))
        conn.commit()
        conn.close()
        print("Update barang Successfull")
        nama_kategori.set("")
        nama_barang.set("")
        qty.set("")
        harga.set("")

def hapus_barang() :
    conn = connect_database()
    print(conn)

    c = conn.cursor()
    a_nama_barang = nama_barang.get()
    c.execute("DELETE FROM barang WHERE nama ='" + a_nama_barang + "'")
    conn.commit()
    conn.close()
    print("Hapus data barang Successfull")
    nama_barang.set("")

def view_invoice() :
    f_dashboard.pack_forget()
    f_tambah_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_view_invoice.pack()
    f_view_konfirmasi_pembayaran.pack_forget()
    f_hapus_kategori.pack_forget()
    f_view_barang_admin.pack_forget()
    f_tambah_kategori.pack_forget()
    f_edit_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_invoice_detail.pack_forget()    
    
    for label in f_view_invoice.grid_slaves():
      label.grid_forget()
      
    conn = connect_database()
    print(conn)

    c = conn.cursor()
    c.execute("SELECT h.id, h.total, u.full_name FROM hbeli h, users u WHERE u.id = h.user_id ORDER BY h.id DESC")
    rows = c.fetchall()

    i = 0
    Label(f_view_invoice, text="Full Name").grid(row=0, column=0, sticky=W)
    Label(f_view_invoice, text="Total").grid(row=0, column=1, sticky=W)
    for row in rows:
        data = row
        i = i+1

        Label(f_view_invoice, text=row[2]).grid(row=i, column=0, sticky=W)
        Label(f_view_invoice, text=row[1]).grid(row=i, column=1, sticky=W)
        b=Button(f_view_invoice, text="Detail",command=lambda idx = row[0]: view_invoice_detail(idx)).grid(row=i, column=2, sticky=W)

    b=Button(f_view_invoice, text="Back",command=back_to_dashboard).grid(row=12, column=0, sticky=W)

def view_invoice_detail(idx) :
    f_dashboard.pack_forget()
    f_tambah_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_view_invoice.pack_forget()
    f_view_konfirmasi_pembayaran.pack_forget()
    f_hapus_kategori.pack_forget()
    f_view_barang_admin.pack_forget()
    f_tambah_kategori.pack_forget()
    f_edit_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_invoice_detail.pack()    
    
    for label in f_invoice_detail.grid_slaves():
      label.grid_forget()
      
    conn = connect_database()
    print(conn)

    c = conn.cursor()
    c.execute("SELECT b.nama, d.qty, d.price, d.subtotal FROM hbeli h, dbeli d, barang b WHERE h.id = d.hbeli_id AND b.id = d.barang_id AND h.id = " + str(idx) + " ORDER BY h.id DESC")
    rows = c.fetchall()

    i = 0
    Label(f_invoice_detail, text="Nama").grid(row=i, column=0, sticky=W)
    Label(f_invoice_detail, text="Qty").grid(row=i, column=1, sticky=W)
    Label(f_invoice_detail, text="Harga").grid(row=i, column=2, sticky=W)
    Label(f_invoice_detail, text="Subtotal").grid(row=i, column=3, sticky=W)    
    for row in rows:
        data = row
        i = i+1

        Label(f_invoice_detail, text=row[0]).grid(row=i, column=0, sticky=W)
        Label(f_invoice_detail, text=row[1]).grid(row=i, column=1, sticky=W)
        Label(f_invoice_detail, text=row[2]).grid(row=i, column=2, sticky=W)
        Label(f_invoice_detail, text=row[3]).grid(row=i, column=3, sticky=W)

    b=Button(f_invoice_detail, text="Back",command=view_invoice).grid(row=20, column=0, sticky=W)


def view_konfirmasi_pembayaran() :
    f_dashboard.pack_forget()
    f_tambah_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_view_invoice.pack_forget()
    f_view_konfirmasi_pembayaran.pack()
    f_hapus_kategori.pack_forget()
    f_view_barang_admin.pack_forget()
    f_tambah_kategori.pack_forget()
    f_edit_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_invoice_detail.pack_forget()    
    
    for label in f_view_konfirmasi_pembayaran.grid_slaves():
      label.grid_forget()
      
    conn = connect_database()
    print(conn)

    c = conn.cursor()
    c.execute("SELECT p.invoice_id, u.full_name, p.total FROM payment_confirmation p, hbeli h,users u WHERE h.id = p.invoice_id AND u.id = p.user_id ORDER BY p.id DESC")
    rows = c.fetchall()

    i = 0
    Label(f_view_konfirmasi_pembayaran, text="Invoice ID").grid(row=0, column=0, sticky=W)
    Label(f_view_konfirmasi_pembayaran, text="Nama Lengkap").grid(row=0, column=1, sticky=W)
    Label(f_view_konfirmasi_pembayaran, text="Total").grid(row=0, column=2, sticky=W)
    for row in rows:
        data = row
        i = i+1

        Label(f_view_konfirmasi_pembayaran, text=row[0]).grid(row=i, column=0, sticky=W)
        Label(f_view_konfirmasi_pembayaran, text=row[1]).grid(row=i, column=1, sticky=W)
        Label(f_view_konfirmasi_pembayaran, text=row[2]).grid(row=i, column=2, sticky=W)        

    b=Button(f_view_konfirmasi_pembayaran, text="Back",command=back_to_dashboard).grid(row=20, column=0, sticky=W)

def back_to_dashboard():
    f_tambah_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_view_invoice.pack_forget()
    f_view_konfirmasi_pembayaran.pack_forget()
    f_hapus_kategori.pack_forget()
    f_view_barang_admin.pack_forget()
    f_tambah_kategori.pack_forget()
    f_edit_barang.pack_forget()
    f_hapus_barang.pack_forget()
    f_invoice_detail.pack_forget()    
    
    f_dashboard.pack()

def panel_edit_profile() :
    f_profile.pack_forget()
    f_edit_profile.pack()

    Label(f_edit_profile, text="Email").grid(row=0, column=0, sticky=W)
    email_entry = Entry(f_edit_profile, textvariable=email_signup_var)
    email_entry.grid(row=0, column=1, sticky=W)

    Label(f_edit_profile, text="Nama Lengkap").grid(row=1, column=0, sticky=W)
    fullname_entry = Entry(f_edit_profile, textvariable=fullname_signup_var)
    fullname_entry.grid(row=1, column=1, sticky=W)
    
    Label(f_edit_profile, text="Alamat").grid(row=2, column=0, sticky=W)
    address_entry = Entry(f_edit_profile, textvariable=address)
    address_entry.grid(row=2, column=1, sticky=W)

    
    Label(f_edit_profile, text="Telp").grid(row=3, column=0, sticky=W)
    phonenumber_entry = Entry(f_edit_profile, textvariable=phone_number)
    phonenumber_entry.grid(row=3, column=1, sticky=W)
    
    Button(f_edit_profile, text="Update",command=update_profile).grid(row=4, column=0, sticky=W)
    Button(f_edit_profile, text="Kembali",command=back_to_profile).grid(row=4, column=1, sticky=W)

def update_profile() :
    conn = connect_database()
    print(conn)

    a_email = email_signup_var.get().lower()
    a_fullname = fullname_signup_var.get()
    a_address = address.get()
    a_phone_number = phone_number.get()

    c = conn.cursor()
    c.execute("SELECT * FROM temp WHERE id = 1")
    row = c.fetchone()

    if row is None:
        print("Error")
    else:
        user_id = row[1]

    print(user_id)
    if len(a_email) > 0 and len(a_fullname) > 0:
        c = conn.cursor()
        c.execute("UPDATE users SET email = ?, full_name = ?, address=?, phone_number = ? WHERE id = ?", (a_email,a_fullname,a_address, a_phone_number, user_id))
        conn.commit()
        conn.close()
        print("Update user Successfull")

def panel_view_barang() :
    f_profile.pack_forget()
    f_view_barang.pack()

    for label in f_view_barang.grid_slaves():
      label.grid_forget()
      
    conn = connect_database()
    print(conn)

    c = conn.cursor()
    c.execute("SELECT * FROM barang ORDER BY id DESC")
    rows = c.fetchall()

    i = -1
    for row in rows:
        data = row
        i = i+1

        Label(f_view_barang, text=row[2]).grid(row=i, column=0, sticky=W)
        Label(f_view_barang, text=row[4]).grid(row=i, column=1, sticky=W)
        b=Button(f_view_barang, text="Add to Cart",command=lambda idx = row[0]: add_to_cart(idx)).grid(row=i, column=2, sticky=W)
        b=Button(f_view_barang, text="Back",command=back_to_profile).grid(row=12, column=0, sticky=W)

def add_to_cart(idx) :
    conn = connect_database()
    print(conn)

    c = conn.cursor()
    c.execute("SELECT * FROM temp WHERE id = 1")
    row = c.fetchone()

    if row is None:
        print("Error")
    else:
        user_id = row[1]    


    # check if exist update qty or insert new
    c = conn.cursor()
    c.execute("SELECT * FROM carts WHERE user_id = ? AND barang_id = ?", (user_id, idx))    
    rows = c.fetchall()

    is_exist = False
    for row in rows:
        is_exist = True
        qty = row[3]

    c = conn.cursor()
    if is_exist == False:
        c.execute("INSERT INTO carts(user_id, barang_id, qty) VALUES (?,?,?)", (user_id, idx, 1))
    else:
        qty = qty + 1
        c.execute("UPDATE carts SET qty = ? WHERE user_id = ? AND barang_id = ?", (qty, user_id, idx))            

    conn.commit()
    conn.close()
      
    panel_view_barang()

def view_cart() :
    f_profile.pack_forget()
    f_view_cart.pack()

    conn = connect_database()
    print(conn)


    c = conn.cursor()
    c.execute("SELECT * FROM temp WHERE id = 1")
    row = c.fetchone()

    if row is None:
        print("Error")
    else:
        user_id = row[1]
        

    c = conn.cursor()
    c.execute("SELECT b.*, c.qty FROM barang b, carts c WHERE b.id = c.barang_id AND c.user_id = " + str(user_id))
    rows = c.fetchall()

    
    i = -1
    for row in rows:
        data = row
        i = i+1

        l1=Label(f_view_cart, text=row[2]).grid(row=i, column=0, sticky=W)
        l2=Label(f_view_cart, text=row[5]).grid(row=i, column=1, sticky=W)
        l3=Label(f_view_cart, text=row[4]).grid(row=i, column=2, sticky=W)
        b=Button(f_view_cart, text="Delete",command=lambda idx = row[0]: delete_cart(idx)).grid(row=i, column=3, sticky=W)
        b=Button(f_view_cart, text="Checkout",command=checkout).grid(row=12, column=0, sticky=W)

    b=Button(f_view_cart, text="Back",command=back_to_profile).grid(row=12, column=1, sticky=W)    

def delete_cart(idx) :
    conn = connect_database()
    print(conn)

    c = conn.cursor()
    c.execute("SELECT * FROM temp WHERE id = 1")
    row = c.fetchone()

    if row is None:
        print("Error")
    else:
        user_id = row[1]    


    c = conn.cursor()
    c.execute("DELETE FROM carts WHERE user_id = ? AND barang_id = ?", (user_id, idx))

    conn.commit()
    conn.close()

    for label in f_view_cart.grid_slaves():
      label.grid_forget()


    view_cart()

def checkout() :
    f_view_cart.pack_forget()
    f_checkout.pack()
    
    conn = connect_database()
    print(conn)

    c = conn.cursor()
    c.execute("SELECT * FROM temp WHERE id = 1")
    row = c.fetchone()

    if row is None:
        print("Error")
    else:
        user_id = row[1]    


    #count total
    c = conn.cursor()
    c.execute("SELECT b.harga, c.qty FROM barang b, carts c WHERE b.id = c.barang_id AND c.user_id = " + str(user_id))
    rows = c.fetchall()

    total = 0
    for row in rows:
        subtotal = row[0] * row[1]
        total = total + subtotal


    c = conn.cursor()
    c.execute("INSERT INTO hbeli(user_id, total) VALUES (?,?)", (user_id, total))
    max_id = c.lastrowid


    # save to dbeli
    c = conn.cursor()
    c.execute("SELECT b.id, c.qty, b.harga FROM barang b, carts c WHERE b.id = c.barang_id AND c.user_id = " + str(user_id))
    rows = c.fetchall()

    total = 0
    for row in rows:
        subtotal = row[1] * row[2]
        total = total + subtotal
        c = conn.cursor()
        c.execute("INSERT INTO dbeli VALUES (?,?,?,?,?)", (max_id, row[0], row[1], row[2], subtotal))

    c = conn.cursor()
    c.execute("DELETE FROM carts WHERE user_id = " + str(user_id))
    
    conn.commit()
    conn.close()

    Label(f_checkout, text="Invoice id : " + str(max_id)).grid(row=0, column=0, sticky=W)
    Label(f_checkout, text="Total : " + str(total)).grid(row=1, column=0, sticky=W)
    b=Button(f_checkout, text="Back",command=back_to_profile).grid(row=12, column=1, sticky=W)    


def panel_konfirmasi_pembayaran() :
    f_profile.pack_forget()
    f_checkout.pack_forget()
    f_view_barang.pack_forget()
    f_view_cart.pack_forget()
    f_konfirmasi_pembayaran.pack()

    Label(f_konfirmasi_pembayaran, text="Invoice id").grid(row=0, column=0, sticky=W)
    nama_entry = Entry(f_konfirmasi_pembayaran, textvariable=invoice_id)
    nama_entry.grid(row=0, column=1, sticky=W)
    Label(f_konfirmasi_pembayaran, text="Total").grid(row=1, column=0, sticky=W)
    nama_entry = Entry(f_konfirmasi_pembayaran, textvariable=total)
    nama_entry.grid(row=1, column=1, sticky=W)    
    Button(f_konfirmasi_pembayaran, text="Submit",command=simpan_konfirmasi_pembayaran).grid(row=2, column=0, sticky=W)
    Button(f_konfirmasi_pembayaran, text="Back",command=back_to_profile).grid(row=2, column=1, sticky=W)

def simpan_konfirmasi_pembayaran() :    
    conn = connect_database()
    print(conn)

    c = conn.cursor()
    c.execute("SELECT * FROM temp WHERE id = 1")
    row = c.fetchone()

    if row is None:
        print("Error")
    else:
        user_id = row[1]
        
    c = conn.cursor()
    c.execute("INSERT INTO payment_confirmation(user_id, invoice_id, total) VALUES (?, ?, ?)", (user_id, invoice_id.get(), total.get()))

    conn.commit()
    conn.close()

    back_to_profile()
    
    
def back_to_profile():
    f_edit_profile.pack_forget()
    f_view_barang.pack_forget()
    f_view_cart.pack_forget()
    f_checkout.pack_forget()
    f_konfirmasi_pembayaran.pack_forget()
    
    
    f_profile.pack()

def do_logout() :
    f_profile.pack_forget()
    login()

def connect_database() :
    database = "d://store/store.db"
    conn = sqlite3.connect(database)
      
    return conn

def makeWindow () :
    global username_login_var, pass_login_var, username_signup_var, pass_signup_var, email_signup_var, fullname_signup_var, role,nama_kategori, nama_barang, qty, harga, kategori_id, address, phone_number, user_id, i, btn_list, is_exist, total, max_id, invoice_id
    global f_login, f_signup, f_profile, f_dashboard, f_tambah_kategori, f_hapus_kategori, f_tambah_barang, f_edit_barang, f_hapus_barang, f_edit_profile, f_view_barang, f_view_cart, f_konfirmasi_pembayaran, f_checkout, f_view_barang_admin, f_view_invoice, f_view_konfirmasi_pembayaran, f_invoice_detail
    win = Tk()
    username_login_var = StringVar()
    pass_login_var = StringVar()
    username_signup_var = StringVar()
    pass_signup_var = StringVar()
    email_signup_var = StringVar()
    fullname_signup_var = StringVar()
    role = StringVar()
    nama_kategori = StringVar()
    nama_barang = StringVar()
    qty = IntVar()
    harga = IntVar()
    address = StringVar()
    phone_number = StringVar()
    user_id = IntVar()
    total = IntVar()
    invoice_id = IntVar()
    user_id = 0
    btn_list = []

    f_login = Frame(win)
    f_signup = Frame(win)
    f_profile = Frame(win)
    f_dashboard = Frame(win)
    f_tambah_kategori = Frame(win)
    f_hapus_kategori = Frame(win)
    f_tambah_barang = Frame(win)
    f_edit_barang = Frame(win)
    f_hapus_barang = Frame(win)
    f_edit_profile = Frame(win)
    f_view_barang = Frame(win)
    f_view_cart = Frame(win)
    f_konfirmasi_pembayaran = Frame(win)
    f_checkout = Frame(win)
    f_view_barang_admin = Frame(win)
    f_view_invoice = Frame(win)
    f_view_konfirmasi_pembayaran = Frame(win)
    f_invoice_detail = Frame(win)

    login()

    return win

win = makeWindow()
win.mainloop()
