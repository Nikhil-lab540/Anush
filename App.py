
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel to Text", layout="wide")

st.title("📊 Excel Row & Column → Text Converter")

uploaded_file = st.file_uploader(
    "Upload Excel file",
    type=["xlsx", "xls"]
)

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.subheader("Preview Excel Data")
    st.dataframe(df, use_container_width=True)

    st.divider()

    # ---------- Column Selection ----------
    st.subheader("Select Columns")
    selected_columns = st.multiselect(
        "Choose columns to include",
        df.columns.tolist(),
        default=df.columns.tolist()
    )

    # ---------- Row Selection ----------
    st.subheader("Select Rows")

    row_indices = df.index.tolist()

    selected_rows = st.multiselect(
        "Choose rows",
        options=row_indices,
        format_func=lambda x: f"Row {x + 1}"
    )

    if st.button("Generate Text", type="primary"):
        if not selected_rows:
            st.warning("Please select at least one row.")
        elif not selected_columns:
            st.warning("Please select at least one column.")
        else:
            filtered_df = df.loc[selected_rows, selected_columns]

            text_output = ""

            for idx, row in filtered_df.iterrows():
                text_output += f"Row {idx + 1}\n"
                for col in selected_columns:
                    text_output += f"- {col}: {row[col]}\n"
                text_output += "\n"

            st.subheader("Generated Text")

            st.text_area(
                "Copy the text below",
                text_output,
                height=300
            )

            st.download_button(
                "⬇️ Download as TXT",
                data=text_output,
                file_name="output.txt",
                mime="text/plain"
            )
