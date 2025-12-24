import subprocess
import streamlit as st

st.set_page_config(page_title="In-Memory DB", layout="wide")
st.title("In-Memory Database (C++)")

query = st.text_area(
    "Enter SQL-like commands",
    height=200,
    placeholder="CREATE TABLE users (id, name)\nINSERT INTO users VALUES (1, Alice)\nSELECT * FROM users"
)

if st.button("Execute"):
    try:
        result = subprocess.run(
            ["./in-memory-db"],
            input=query,
            text=True,
            capture_output=True,
            timeout=5
        )

        if result.stdout:
            st.subheader("Output")
            st.code(result.stdout)

        if result.stderr:
            st.subheader("Errors")
            st.error(result.stderr)

    except Exception as e:
        st.error(str(e))
