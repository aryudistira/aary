import streamlit as st
import pandas as pd

st.header("_:blue[Hello Universe!]_")
def main():
    st.write("**:black[Terimakasih sudah berkunjung]**")
st.sidebar.header('Menu')
menu = st.sidebar.radio('klik tobol dibawah:', ['Wellcome', 'Biodata', 'Tentang', 'Kontak'])
if menu == 'Wellcome':
    header = st.image("foto_profil/header.png", use_column_width=True,)
    st.title('SAMPURASUN')
    st.write('Silahkan Diisi:')
#input
    nama = st.text_input('Nama :')
    umur = st.text_input('umur:')
    jenis_kelamin = st.text_input('Jenis Kelamin')
    st.button('Simpan')


elif menu == 'Biodata':
    st.title('Selamat datang di Beranda')
    profil_image = st.image("foto_profil/aldii.jpeg", width=300, caption="Foto Profil",)
    st.write('Nama 			: Aldi Rizki Yudistira')
    st.write('Prodi 			: Manajemen Informasi Kesehatan')
    st.write('NIM 			: B01.022.002')

elif menu == 'Tentang':
    header = st.image("foto_profil/header.png", use_column_width=True,)
    st.title('Tentang Kami')
    st.write("**:red[Silahkan klik dibawah ini untuk melihat informasi!]**")
    namaa = ['Who is he?', 'Aldi Rizki Yudistira']
    pilihan_nama = st.selectbox('', namaa)
    if pilihan_nama == 'Aldi Rizki Yudistira':
        st.write('Adalah seorang perekam medis yang handal dengan pengetahuan yang mendalam dan pengalaman yang luas dalam mengelola dan memelihara rekam medis secara efisien dan akurat. Dedikasi saya terhadap integritas data pasien dan kepatuhan terhadap privasi serta regulasi industri menjadikan saya seorang profesional yang terpercaya dalam bidang ini. Dalam peran saya sebagai perekam medis, saya memiliki keahlian dalam menggunakan sistem rekam medis elektronik (EHR) dan memahami prosedur dan standar dalam pembuatan, penyimpanan, dan pengelolaan rekam medis. Saya terampil dalam mengumpulkan, memvalidasi, dan memperbarui informasi medis, serta mengatur dan mengindeks data dengan presisi tinggi')
    else:
        st.write('')
    prodi = ['jurusan apa yang sesuai agar bisa menjadi perekam medis?', 'Manajemen Informasi Kesehatan']
    pilihan_prodi = st.selectbox('', prodi)
    if pilihan_prodi == 'Manajemen Informasi Kesehatan' :
        st.write('Manajemen Informasi Kesehatan mempelajari Sistem Informasi kesehatan untuk penyelesaian masalah di bidang kesehatan sehingga terciptanya pelayanan kesehatan yang good clinical governance. Dengan Lulusan Sarjana Manajemen Informasi Kesehatan (S.MIK)')
    else:
        st.write('')

    tugas = ['Tugas dan tanggung jawab seorang rekam medis?', 'Klik Disini']
    pilihan_prod = st.selectbox('', tugas)
    if pilihan_prod == 'Klik Disini' :
        st.write('Seorang staf rekam medis bertanggung jawab juga dalam pemanfaatan data rekam medis sebagai penelitian atau publisitas. Basis data dan informasi tersebut diolah dengan menyediakan rangkuman statistik medis dan penyakit untuk publikasi penelitian ilmiah di bidang kesehatan. Staf rekam medis juga harus bertindak cepat jika suatu waktu data rekam medis diperlukan. Oleh karena itu, menjadi staf rekam medis harus teliti dan mahir dalam pengelolaan dan penyimpanan data.')
    else: 
        st.write('')

elif menu == 'Kontak':
    header = st.image("foto_profil/header.png", use_column_width=True,)
    st.title('Hubungi Kami')
    prod = ['Contact Person', 'WhatsApp', 'Instagram', 'Email']
    pilihan_prod = st.selectbox('', prod)
    if pilihan_prod == 'WhatsApp' :
        st.write('Click Link [WhatsApp](https://wa.me/6287872624702)')
    elif pilihan_prod == 'Instagram':
        st.write('Click Link [Instagram](https://instagram.com/aryudistira_)')
    elif pilihan_prod == 'Email' :
        st.write('Email: aldiyudistira00@gmail.com')
    else:
        st.write('')
    st.write("**:blue[Jangan lupa tinggalkan pesan]**")


import streamlit as st

def main():
    st.title("Kotak Saran")
    st.write("Silakan berikan masukan, saran, atau komentar Anda:")
    message = st.text_area("Pesan")
    if st.button("Kirim"):
        save_message(message)
        st.success("Pesan berhasil dikirim. Terima kasih!")

def save_message(message):
    with open("feedback.txt", "a") as file:
        file.write(message + "\n")

if __name__ == "__main__":
	main()
