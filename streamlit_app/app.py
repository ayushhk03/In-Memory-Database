import subprocess
import streamlit as st
import shutil
import os

REPO_BINARY = "/app/streamlit_app/in-memory-db"
TMP_BINARY = "/tmp/in-memory-db"

st.set_page_config(page_title="In-Memory DB", layout="wide")
st.title("In-Memory Database (C++)")

query = st.text_area(
    "Enter SQL commands",
    height=200,
    placeholder="CREATE TABLE users (id, name)\nINSERT INTO users VALUES (1, Alice)\nSELECT * FROM users"
)

if st.button("Execute"):
    try:
        # 🔥 Copy binary to executable filesystem
        if not os.path.exists(TMP_BINARY):
            shutil.copy(REPO_BINARY, TMP_BINARY)
            os.chmod(TMP_BINARY, 0o755)

        result = subprocess.run(
            [TMP_BINARY],
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
