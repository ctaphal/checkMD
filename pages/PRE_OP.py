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
from storage import tools_list

# some of this file's code is from another source (Google how to make a checklist using Streamlit to try to find the source)

pre_op_checks = ["Correct Patient?", "Reviewed patient's medical history?", "Reviewed patient's medications?", "Reviewed patient's most recent test results?", "Received patient consent documentation?", "Confirmed patient was NPO as appropriate?", "Confirmed correct surgical site?", "Had someone else confirm correct surgical site?", "Checked availability of suitable blood products?", "Sterile practice observed?", "'Time-out' completed?", "Documented plan?"]

def listTasks():
    st.markdown("")
    st.subheader("Pre-Op Checklist: ")
    for check in pre_op_checks:
        st.checkbox(check)

listTasks()