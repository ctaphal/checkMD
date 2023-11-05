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

from typing import Any
import numpy as np
import streamlit as st
from datetime import datetime as dt
import altair as alt
import pandas as pd
import io
from storage import allergies_list
from storage import medical_hist
from storage import meds_list
from storage import surgical_site
from storage import blood_type

def surgery_data_display():
        st.subheader("Allergies")
        allg_df = pd.DataFrame(allergies_list, columns=["Allergies"])
        st.dataframe(allg_df)

        st.subheader("Medical History")
        medHx_df = pd.DataFrame(medical_hist, columns=["Medical History"])
        st.dataframe(medHx_df)

        st.subheader("Medications")
        meds_df = pd.DataFrame(meds_list, columns=["Medications"])
        st.dataframe(meds_df)

        st.subheader("Surgical Site(s)")
        ssite_df = pd.DataFrame(surgical_site, columns=["Surgical Site(s)"])
        st.dataframe(ssite_df)
        
        st.subheader("Blood Type")
        bt_df = pd.DataFrame(blood_type, columns=["Blood Type"])
        st.dataframe(bt_df)


st.set_page_config(page_title="OR Display")
st.markdown("# OR Display")
st.sidebar.header("")
st.markdown("*Most critical patient info to display on an OR TV screen*")

custom_styles = """
    body {
        font-family: "Times New Roman", Times, serif;
        color: #000;
        font-size: 16px;
    }
    h1 {
        color: #89CFF0;
        font-family: "Times New Roman", Times, serif;
    }
    h3 {
        color: #89CFF0;
        font-family: "Times New Roman", Times, serif;
    }
    p {
        font-size: 16px;
        font-family: "Times New Roman", Times, serif;
    }
"""

st.markdown(f"<style>{custom_styles}</style>", unsafe_allow_html=True)

surgery_data_display()