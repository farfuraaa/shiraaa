
import base64
import streamlit as st

# n_sounds = 6
# # Define the audio file path
# audio_file = open(f"{random.randint(0,n_sounds)}.mp3", "rb").read()
#
# # Play the audio file using the st_player function
# st_player(audio_file)




def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# # # ---- LOAD ASSETS ----
# lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# img_contact_form = Image.open("images/yt_contact_form.png")
# img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    with st.container():
        st.write("---")
        st.title("Shira Tamari")
        st.write("---")

# art

