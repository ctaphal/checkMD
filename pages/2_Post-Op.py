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
from streamlit.hello.utils import show_code

import streamlit as st
from datetime import datetime as dt
from storage import or_items

if "mytsks" not in st.session_state:
    st.session_state.mytsks = []

if "tskclk" not in st.session_state:
    st.session_state.tskclk = []

if "chkarr" not in st.session_state:
    st.session_state.chkarr = []

if "rerun" not in st.session_state:
    st.session_state.rerun = False


def cmpltTask(or_item):
    idx = st.session_state.mytsks.index(or_item)
    st.session_state.chkarr[idx] = not st.session_state.chkarr[idx]
    st.session_state.rerun = True

def listTasks():
    st.session_state.tskclk = []
    st.markdown("")
    st.subheader("OR Items: ")
    st.caption("*Check off each item after it's been accounted for post-op*")
    for or_item in or_items:
        st.checkbox(f"- **{or_item}**")

st.title("Post-Op Surgical Tool Tracker")

if st.session_state.rerun == True:
    st.session_state.rerun = False
    st.experimental_rerun()

else:
    item = st.text_input("Enter items brought into the OR (one at a time): ", value="")
    if st.button('Add Item'):
        if item != "":
            or_items.append(item)
            st.session_state.mytsks.append(item)
            st.session_state.chkarr.append(False)

listTasks()