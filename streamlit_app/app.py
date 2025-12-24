import subprocess
import streamlit as st
import os
import stat

BINARY_PATH = "/app/streamlit_app/in-memory-db"

st.set_page_config(page_title="In-Memory DB", layout="wide")
st.title("In-Memory Database (C++)")

query = st.text_area(
    "Enter SQL commands",
    height=200,
    placeholder="CREATE TABLE users (id, name)\nINSERT INTO users VALUES (1, Alice)\nSELECT * FROM users"
)

if st.button("Execute"):
    try:
        # 🔥 Force executable permission at runtime (Streamlit Cloud fix)
        st.info("Preparing database engine…")
        os.chmod(BINARY_PATH, stat.S_IRWXU)

        result = subprocess.run(
            [BINARY_PATH],
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
