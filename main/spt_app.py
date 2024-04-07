import pandas as pd
import streamlit as st
from pathlib import Path
import time
import base64
import cv2

st.set_page_config(
    page_title="SPT app",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": "mailto:konigmatt@googlemail.com",
        "Report a bug": "https://github.com/matthiaskoenig/spt-app/issues/new",
        "About": """
        SPT web application.
        """,
    },
)
st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 1rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)


data_path = Path(__file__).parent.parent / "data"
simulations_path = data_path / "simulations.tsv"

@st.cache_data
def load_data():
    """Load data."""
    df = pd.read_csv(simulations_path, sep="\t")
    simulations = df.sim_key.values
    patterns = df.pattern_name.unique()
    pattern2simulations = {}
    for pattern in patterns:
        pattern2simulations[pattern] = df[df.pattern_name == pattern].sim_key.values.tolist()

    return df, simulations, patterns, pattern2simulations


df, simulations, patterns, pattern2simulations = load_data()

# --- Side bar ------------------------------------------------------------------------
st.sidebar.title("SPT model simulations")
selected_pattern = st.sidebar.selectbox(
    "Select zonation pattern",
    index=3,  # default: linear increase
    options=patterns,
)
selected_flow = st.sidebar.select_slider(
    'Select substrate flow',
    value=3,  # default
    options=[0, 1, 2, 3, 4, 5, 6],
)
simulation_id = df[(df.pattern_name == selected_pattern) & (df.boundary_flow_key == selected_flow)].sim_key.values[0]

st.sidebar.header("References")
st.sidebar.markdown(
"""
**Simulation of zonation-function relationships in the liver using coupled multiscale models: Application to drug-induced liver injury**.
Steffen Gerhäusser, Lena Lambers, Luis Mandl, Julian Franquinet, Tim Ricken, Matthias König.
bioRxiv 2024.03.26.586870; doi: https://doi.org/10.1101/2024.03.26.586870
"""
)
st.sidebar.markdown(
"""
**SPT model (0.5.4)**.
König, M. (2024).
Zenodo. https://doi.org/10.5281/zenodo.10853538
"""
)

# --- Main ----------------------------------------------------------------------------

row = df[df.sim_key == simulation_id]
st.markdown(f"**simulation**: `{simulation_id}`, **pattern**: `{row.pattern_name.values[0]}`, **substrate flow**: `Sv{row.boundary_flow_key.values[0]}`")

# video rendering
url = f"https://github.com/matthiaskoenig/spt-app/raw/main/data/{simulation_id}_h264.mp4"
video_placeholder = st.empty()
video_html = f"""
    <video width="80%" controls="false" autoplay loop="true" align="middle">
      <source src="{url}" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
"""
video_placeholder.empty()
time.sleep(0.1)
video_placeholder.markdown(video_html, unsafe_allow_html=True)
st.divider()

# image
def render_img_html(image_b64):
    st.markdown(f"<img style='max-width: 80%;max-height: 100%;' src='data:image/png;base64, {image_b64}'/>", unsafe_allow_html=True)

def image_to_base64(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    _, encoded_image = cv2.imencode(".png", image)
    base64_image = base64.b64encode(encoded_image.tobytes()).decode("utf-8")
    return base64_image


image_path = data_path / f"{simulation_id}.png"
render_img_html(image_to_base64(str(image_path)))
