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
from datetime import datetime as dt
from storage import allergies_list
from storage import medical_hist
from storage import meds_list
from storage import surgical_site
from storage import blood_type
from storage import pre_op_checklist
from storage import pre_op_not_checked

def checklist():
    pre_op_checks = ["Correct Patient?", "Reviewed patient's medical history?", "Reviewed patient's medications?", "Reviewed patient's most recent test results?", "Received patient consent documentation?", "Confirmed patient was NPO as appropriate?", "Confirmed correct surgical site?", "Had someone else confirm correct surgical site?", "Checked availability of suitable blood products?", "Sterile practice observed?", "\"Time-out\" completed?", "Documented plan?"]
    st.markdown("")
    st.subheader("Checklist: ")

    for check in pre_op_checks:
        if st.checkbox(check):
            if check not in pre_op_checklist:
                pre_op_checklist.append(check) 
            if check in pre_op_not_checked:
                pre_op_not_checked.remove(check)
        else:
            if check in pre_op_checklist: 
                pre_op_checklist.remove(check) 
            if check not in pre_op_not_checked:
                pre_op_not_checked.append(check) 
    st.markdown("\n\n\n\n")
         

## Allergies Check
def listAllergies():
    if "mytsks" not in st.session_state:
        st.session_state.mytsks = []

    if "tskclk" not in st.session_state:
        st.session_state.tskclk = []

    if "chkarr" not in st.session_state:
        st.session_state.chkarr = []

    if "rerun" not in st.session_state:
        st.session_state.rerun = False

    st.subheader("Patient's Allergies: ")
    if st.session_state.rerun == True:
        st.session_state.rerun = False
        st.experimental_rerun()

    else:
        allg = st.text_input("Enter patient's allergies (one at a time) or enter NONE if none: ", value="")
        if st.button('Add Allergy'):
            if allg != "":
                allergies_list.append(allg)
                st.session_state.mytsks.append(allg)
                st.session_state.chkarr.append(False)
    st.session_state.tskclk = []

    st.markdown("")
    for allergy in allergies_list:
        st.markdown(f"- **{allergy}**")
    st.markdown("\n\n\n\n")
    st.session_state.rerun = False

def listMedHx():
    if "mytsks" not in st.session_state:
        st.session_state.mytsks = []

    if "tskclk" not in st.session_state:
        st.session_state.tskclk = []

    if "chkarr" not in st.session_state:
        st.session_state.chkarr = []

    if "rerun" not in st.session_state:
        st.session_state.rerun = False

    st.subheader("Patient's Medical History: ")
    if st.session_state.rerun == True:
        st.session_state.rerun = False
        st.experimental_rerun()

    else:
        cond = st.text_input("Enter patient's medical conditions (one at a time) or enter NONE if none: ", value="")
        if st.button('Add Condition'):
            if cond != "":
                medical_hist.append(cond)
                st.session_state.mytsks.append(cond)
                st.session_state.chkarr.append(False)
    st.session_state.tskclk = []

    st.markdown("")
    for condition in medical_hist:
        st.markdown(f"- **{condition}**")
    st.markdown("\n\n\n\n")


def listMeds():
    if "mymeds1" not in st.session_state:
        st.session_state.mymeds1 = []

    if "mymeds2" not in st.session_state:
        st.session_state.mymeds2 = []

    if "mymeds3" not in st.session_state:
        st.session_state.mymeds3 = []

    if "mymeds4" not in st.session_state:
        st.session_state.mymeds4 = False

    st.subheader("Patient's Medications: ")
    if st.session_state.mymeds4 == True:
        st.session_state.mymeds4 = False
        st.experimental_rerun()

    else:
        med = st.text_input("Enter patient's medications (one at a time) or enter NONE if none: ", value="")
        if st.button('Add Medication'):
            if med != "":
                meds_list.append(med)
                st.session_state.mymeds1.append(med)
                st.session_state.mymeds3.append(False)
    st.session_state.mymeds2 = []

    st.markdown("")
    for medication in meds_list:
        st.markdown(f"- **{medication}**")
    st.markdown("\n\n\n\n")


def listSurgicalSites():
    if "mytsks" not in st.session_state:
        st.session_state.mytsks = []

    if "tskclk" not in st.session_state:
        st.session_state.tskclk = []

    if "chkarr" not in st.session_state:
        st.session_state.chkarr = []

    if "rerun" not in st.session_state:
        st.session_state.rerun = False

    st.subheader("Surgical Site(s): ")
    if st.session_state.rerun == True:
        st.session_state.rerun = False
        st.experimental_rerun()

    else:
        site = st.text_input("Enter patient's surgical site(s): ", value="")
        if st.button('Add Surgical Site'):
            if site != "":
                surgical_site.append(site)
                st.session_state.mytsks.append(site)
                st.session_state.chkarr.append(False)
    st.session_state.tskclk = []

    st.markdown("")
    for s_site in surgical_site:
        st.markdown(f"- **{s_site}**")
    st.markdown("\n\n\n\n")


def listBloodType():
    if "mytsks" not in st.session_state:
        st.session_state.mytsks = []

    if "tskclk" not in st.session_state:
        st.session_state.tskclk = []

    if "chkarr" not in st.session_state:
        st.session_state.chkarr = []

    if "rerun" not in st.session_state:
        st.session_state.rerun = False

    st.subheader("Patient's Blood Type: ")
    if st.session_state.rerun == True:
        st.session_state.rerun = False
        st.experimental_rerun()

    else:
        type = st.text_input("Enter patient's blood type: ", value="")
        if st.button('Add Blood Type'):
            if type != "":
                blood_type.append(type)
                st.session_state.mytsks.append(type)
                st.session_state.chkarr.append(False)
    st.session_state.tskclk = []
    st.markdown("")
    if (len(blood_type)!=0):
        st.markdown(f"- **{blood_type[len(blood_type)-1]}**")
    st.markdown("\n\n\n\n")

st.title("Pre-Op Checks")
st.markdown("*Confirm the following immediately prior to surgery*")

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

checklist()
listAllergies()
listMedHx()
listMeds()
listSurgicalSites()
listBloodType()