"""Entry point for the COMP4415/5415 Streamlit app.

Configures the Streamlit page, displays a sidebar logo, and registers
app subpages (Text, Layout, Images, Audio, Videos) for navigation.
"""

import streamlit as st

st.set_page_config(
    page_title="COMP4415/5415", #title on the tab
    page_icon="🎬",
    layout="wide",
)

# with st.sidebar:
#     #st.code('''st.image('assets/logo.png')''')
#     st.image('assets/logo.png')

# pages = {
#     "Text": [
#         st.Page("pages/4_text.py", title="Text"),
#     ],
#     "Layout": [
#         st.Page("pages/Cols.py", title="Columns"),
#         st.Page("pages/Tabs.py", title="Tabs"),
#         st.Page("pages/Container.py", title="Container"),
#     ],
#     "Images": [
#         st.Page("pages/Poster.py", title="Poster"),
#         st.Page("pages/Story.py", title="Storyboard"),
#         st.Page("pages/Gallery.py", title="Gallery"),
#         st.Page("pages/banner.py", title="Banner"),
#         st.Page("pages/Image_map.py", title="Image Map"),
#     ],
#     "Audio": [
#         st.Page("pages/Audio.py", title="Audio"),
#     ],
#     "Videos": [
#         st.Page("pages/2_Video.py", title="Animation"),
#         st.Page("pages/Chapter.py", title="Video Chapter"),
#     ],
#     "Widgets": [
#         st.Page("pages/widgets.py", title="Widgets"),
#     ],
#     "Streamlit VS HTML/CSS/JS": [
#         st.Page("pages/compare_style.py", title="Showcase"),
#     ],
#     "Questions": [
#         st.Page("pages/discussion.py", title="Discussion"),
#     ],


pages=[st.Page('pages/discussion.py',title="Discussion"),
       st.Page('pages/videonaudio.py',title="Video"),
       st.Page('pages/audios.py',title="Audio")]

pg = st.navigation(pages)

pg.run()
