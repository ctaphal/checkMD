# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger


LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="CheckMD",
        page_icon="👩‍⚕️"
    )

    '''alternate option for home page header
    col1, col2 = st.columns([1, 2])

    # Add text to the first column
    with col1:
        st.markdown("""<h1><b>CheckMD</b></h1>""", unsafe_allow_html=True)
    # Add an image to the second column
    with col2:
        st.image("checkMDLogo.png", use_column_width=False, width=85)
    '''

    # Use st.markdown with HTML to make the text "CheckMD" bold and bigger
    st.markdown("""<h1 style = "font-family:new roman;"><b>👩‍⚕️CheckMD</b></h1>""", unsafe_allow_html=True)

    st.markdown(
    """
    <em style = "font-size:15px">Patient Safety Technology to Prevent Errors In the Operating Room</em>
    """,
    unsafe_allow_html=True
)


if __name__ == "__main__":
    run()

custom_styles = """
    body {
        background-color: #3498db;
        font-family: "Times New Roman", Times, serif;
    }

    h1 {
        color: #89CFF0;
        font-family: "Times New Roman", Times, serif;
    }

    p {
        font-size: 16px;
    }
"""

st.markdown(f"<style>{custom_styles}</style>", unsafe_allow_html = True)

st.markdown(f"- Refreshes surgeons on the **most critical patient/surgery info**")
st.markdown(f"- Keeps **track of surgical items** in the OR")
st.markdown(f"- Provides a **display page for OR TVs** containing the most critical patient info to monitor during the surgery")
st.markdown(f"- Keeps **surgeons accountable** for all of these checks via a surgery data download page which records the patient safety measures taken during the operation")