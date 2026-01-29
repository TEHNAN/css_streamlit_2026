import streamlit as st
import pandas as pd
import numpy as np

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Dr. Tehnan Mohamed | Researcher Profile",
    layout="wide"
)

# --------------------------------------------------
# Sidebar Navigation (UPDATED)
# --------------------------------------------------
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "Contact"],
)

# --------------------------------------------------
# Researcher Profile
# --------------------------------------------------
if menu == "Researcher Profile":
    st.title("Researcher Profile")

    name = "Dr. Tehnan Mohamed"
    position = "Postdoctoral Research Fellow"
    field = "Computer Science | Artificial Intelligence"
    institution = "North-West University (NWU), South Africa"
    location = "Durban, KwaZulu-Natal, South Africa"

    st.write(f"**Name:** {name}")
    st.write(f"**Position:** {position}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    st.write(f"**Location:** {location}")

    st.subheader("Professional Summary")
    st.write("""
    PhD in Computer Science with a strong background in artificial intelligence,
    machine learning, and data analysis. Proficient in Python, deep learning
    frameworks, and data visualization tools. Experienced in applying AI
    solutions to real-world problems, with a strong publication record and
    collaborative research experience.
    """)

    st.subheader("Technical Skills")
    st.markdown("""
    - **Programming:** Python  
    - **ML/DL Frameworks:** TensorFlow, PyTorch, Scikit-learn  
    - **Tools:** SQL, Tableau, SPSS, Hadoop, Excel  
    - **Platforms:** Windows, Linux  
    - **Techniques:** Data Analysis, Feature Engineering, Model Evaluation, Visualization
    """)

    st.image(
        "https://cdn.pixabay.com/photo/2019/03/21/03/38/artificial-intelligence-4070976_1280.jpg",
        caption="Artificial Intelligence & Data Science"
    )

# --------------------------------------------------
# Publications
# --------------------------------------------------
elif menu == "Publications":
    st.title("Publications")

    publications = pd.DataFrame({
        "Title": [
            "Enhancing lung cancer classification and prediction with deep learning and multi-omics data",
            "A novel feature selection algorithm for identifying hub genes in lung cancer",
            "A bio-inspired convolution neural network for breast cancer detection",
            "Automatic detection and classification of lung cancer CT scans using deep learning and EOSA",
            "Ebola optimization search algorithm: A new metaheuristic optimization algorithm"
        ],
        "Journal / Publisher": [
            "IEEE",
            "Scientific Reports",
            "Scientific Reports",
            "PLOS ONE",
            "IEEE Access"
        ],
        "Year": [2024, 2023, 2023, 2023, 2022]
    })

    st.dataframe(publications, use_container_width=True)

    st.subheader("Publication Timeline")
    year_counts = publications["Year"].value_counts().sort_index()
    st.bar_chart(year_counts)

    st.markdown("""
    **Research Areas**
    - Lung cancer detection using deep learning  
    - Multi-omics data integration  
    - Feature selection and bio-inspired optimization  
    - Medical image analysis  
    - Metaheuristic optimization algorithms
    """)

# --------------------------------------------------
# Contact
# --------------------------------------------------
elif menu == "Contact":
    st.title("Contact Information")

    st.write("**Dr. Tehnan Mohamed**")
    st.write("Postdoctoral Research Fellow – North-West University")

    st.write("📍 Durban, KwaZulu-Natal, South Africa")
    st.write("📧 Email: tehnanibrahem35@gmail.com | 56209045@mynwu.ac.za")
    st.write("📞 Phone: +27 83 411 5292")
    st.write("🔗 LinkedIn: https://linkedin.com/in/tehnan-mohamed-a22a08167")
    st.write("🔗 ResearchGate: https://www.researchgate.net/profile/Tehnan-Mohamed")
