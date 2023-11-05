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
import xlsxwriter

from storage import pre_op_items
from storage import post_op_items
from storage import pre_op_checklist
from storage import pre_op_not_checked
from storage import allergies_list
from storage import medical_hist
from storage import meds_list
from storage import surgical_site
from storage import blood_type

def surgery_data_download():
        st.subheader("Items Brought Into OR")
        preItems_df = pd.DataFrame(pre_op_items, columns=["OR Items: Pre-Op"])
        st.dataframe(preItems_df)
        
        st.subheader("Items Accounted for Post-Op")
        postItems_df = pd.DataFrame(post_op_items, columns=["OR Items: Post-Op"])
        st.dataframe(postItems_df)

        st.subheader("Checked Pre-Op")
        preChecked_df = pd.DataFrame(pre_op_checklist, columns=["Checked Pre-Op"])
        st.dataframe(preChecked_df)
        
        st.subheader("Not Checked Pre-Op")
        preNotChecked_df = pd.DataFrame(pre_op_not_checked, columns=["Not Checked Pre-Op"])
        st.dataframe(preNotChecked_df)

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

        save_to_Excel(preItems_df, postItems_df, preChecked_df, preNotChecked_df, allg_df, medHx_df, meds_df, ssite_df, bt_df)

def save_to_Excel(preItems_df, postItems_df, preChecked_df, preNotChecked_df, allg_df, medHx_df, meds_df, ssite_df, bt_df):
    # Write files to in-memory strings using BytesIO
    # See: https://xlsxwriter.readthedocs.io/workbook.html?highlight=BytesIO#constructor
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet("OR Surgery Record")

    if pre_op_items!=[]:
        for i in range(0, len(pre_op_items)):
            worksheet.write('B1', "Pre-Op Items (brought into OR)")
            cell = 'B'+str(i+2)
            worksheet.write(cell, str(pre_op_items[i]))

    if post_op_items!=[]:
        for i in range(0, len(post_op_items)):
            worksheet.write('C1', "Post-Op Accounted Items")
            cell = 'C'+str(i+2)
            worksheet.write(cell, str(post_op_items[i]))

    if pre_op_checklist!=[]:
        for i in range(0, len(pre_op_checklist)):
            worksheet.write('D1', "Checked Pre-Op")
            cell = 'D'+str(i+2)
            worksheet.write(cell, str(pre_op_checklist[i]))

    if pre_op_not_checked!=[]:
        for i in range(0, len(pre_op_not_checked)):
            worksheet.write('E1', "Not Checked Pre-Op")
            cell = 'E'+str(i+2)
            worksheet.write(cell, str(pre_op_not_checked[i]))
    
    if allergies_list!=[]:
        for i in range(0, len(allergies_list)):
            worksheet.write('F1', "Allergies Noted")
            cell = 'F'+str(i+2)
            worksheet.write(cell, str(allergies_list[i]))

    if medical_hist!=[]:
        for i in range(0, len(medical_hist)):
            worksheet.write('G1', "Noted Medical Conditions")
            cell = 'G'+str(i+2)
            worksheet.write(cell, str(medical_hist[i]))
    
    if meds_list!=[]:
        for i in range(0, len(meds_list)):
            worksheet.write('H1', "Noted Medications")
            cell = 'H'+str(i+2)
            worksheet.write(cell, str(meds_list[i]))

    if surgical_site!=[]:
        for i in range(0, len(surgical_site)):
            worksheet.write('I1', "Noted Surgical Site(s)")
            cell = 'I'+str(i+2)
            worksheet.write(cell, str(surgical_site[i]))

    if blood_type!=[]:
        for i in range(0, len(blood_type)):
            worksheet.write('J1', "Blood Type (w/ Update History)")
            cell = 'J'+str(i+2)
            worksheet.write(cell, str(blood_type[i]))


    workbook.close()
    st.download_button(
        label="Download as Excel Sheet",
        data=output.getvalue(),
        file_name="SurgeryRecord.xlsx",
        mime="application/vnd.ms-excel"
    )   

st.set_page_config(page_title="Surgery Data Download", page_icon="🖥️")
st.markdown("# Surgery Data Download")
st.sidebar.header("")
st.markdown("*Click the button at the bottom of this page to download the surgery's patient safety data*")

surgery_data_download()