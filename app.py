
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

#
# # ---- HEADER SECTION ----
# with st.container():
#     with st.container():
#         st.write("---")
#         st.title("Shira Tamari")
#         st.write("---")
#
# # art
#
# # work
#         urls = [
#             "https://photos.app.goo.gl/ihT5Sty7Yx3NUsVL8",
#             "https://photos.app.goo.gl/fuAaCVfaQq6TthMf9",
#             "https://photos.app.goo.gl/ihT5Sty7Yx3NUsVL8",
#             "https://photos.app.goo.gl/ihT5Sty7Yx3NUsVL8",
#         ]
#
#         image_paths = [
#             "art.png",
#             "wall.png",
#             "wall.png",
#             "wall.png",
#             # "rishum.png",
#             # "grafiti.png",
#
#         ]
#         titels = ["sf"
#
#         ]
#         col1, col2= st.columns(2)
#
#         for url, path, titels, col in zip(urls, image_paths,titels, [col1,col2,col2,col2]):
#             with col:
#                 st.write(titels)
#                 link = f'<a href="{url}" target="_blank"><img src="data:image/jpeg;base64,{base64.b64encode(open(path, "rb").read()).decode()}" alt="Description of the image" width="222"></a>'
#                 st.markdown(link, unsafe_allow_html=True)
#
# with st.container():
#     with st.container():
#         st.write("---")
#         st.write("054-8000524")
#         st.write("shirgilboatamari@gmail.com")
#         st.write("---")
#


