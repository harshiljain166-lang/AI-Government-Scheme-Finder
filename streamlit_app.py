# import streamlit as st

# st.title("🇮🇳 AI Government Scheme Finder")

# age = st.number_input("Enter Your Age", min_value=0, max_value=120)
# income = st.number_input("Enter Annual Income (₹)")
# occupation = st.selectbox("Select Occupation", ["farmer", "student", "labor", "any"])

# schemes = [
#     {"name": "PM Kisan Samman Nidhi", "min_age": 18, "max_income": 200000, "occupation": "farmer"},
#     {"name": "PM Awas Yojana", "min_age": 18, "max_income": 300000, "occupation": "any"},
#     {"name": "PM Ujjwala Yojana", "min_age": 18, "max_income": 150000, "occupation": "any"},
# ]

# if st.button("Find My Schemes"):
#     st.subheader("Eligible Schemes:")

#     found = False
#     for scheme in schemes:
#         if (age >= scheme["min_age"] and
#             income <= scheme["max_income"] and
#             (scheme["occupation"] == occupation or scheme["occupation"] == "any")):

#             st.success(f"✅ {scheme['name']}")
#             found = True

#     if not found:
#         st.warning("No schemes found based on your details.")
   

import streamlit as st

# Page Config
st.set_page_config(page_title="AI Government Scheme Finder 🇮🇳", layout="wide")

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(to right, #FF9933, white, #138808);
}

/* Header */
.main-header {
    text-align:center;
    font-size:40px;
    font-weight:900;
    color:black;
    margin-bottom:10px;
}

/* Sub header */
.sub-header {
    text-align:center;
    font-size:18px;
    font-weight:600;
    color:#222222;
}

/* Home Steps */
.home-steps {
    background:white;
    padding:20px;
    border-radius:12px;
    font-size:18px;
    font-weight:700;
    color:black;
    box-shadow:0 4px 12px rgba(0,0,0,0.2);
}

/* Scheme Card */
.scheme-card {
    background:white;
    padding:20px;
    border-radius:15px;
    margin:15px 0;
    box-shadow:0 4px 15px rgba(0,0,0,0.2);
    transition:0.3s;
}

.scheme-card:hover {
    transform:scale(1.03);
    box-shadow:0 6px 25px rgba(0,0,0,0.4);
}

/* Scheme Title */
.scheme-title {
    font-size:22px;
    font-weight:900;
    color:black;
}

/* Apply Button */
.apply-btn {
    background:#138808;
    color:white;
    padding:8px 15px;
    border-radius:8px;
    text-decoration:none;
    font-weight:700;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown('<div class="main-header">🇮🇳 AI Government Scheme Finder</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Find schemes you are eligible for in simple Hindi & English</div>', unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
page = st.sidebar.radio("🏛 Navigation", ["🏠 Home", "🔎 Find Schemes"])

# ---------------- HOME PAGE ---------------- #
if page == "🏠 Home":
    st.markdown("""
    <div class="home-steps">
    <h3>📌 How to Use This Portal</h3>
    <br>
    1️⃣ Go to <b>Find Schemes</b><br><br>
    2️⃣ Enter your details (Age, Income, Category, Occupation)<br><br>
    3️⃣ Click <b>Find My Schemes</b><br><br>
    4️⃣ View eligible government schemes<br><br>
    </div>
    """, unsafe_allow_html=True)

    st.info("This platform helps citizens easily discover government welfare schemes without middlemen.")

# ---------------- FIND SCHEMES PAGE ---------------- #
elif page == "🔎 Find Schemes":

    language = st.selectbox("🌐 Select Language / भाषा चुनें", ["English", "Hindi"])

    age = st.number_input("Age / आयु", 0, 100)
    income = st.number_input("Annual Income / वार्षिक आय", 0)
    category = st.selectbox("Category / वर्ग", ["General", "OBC", "SC", "ST"])
    occupation = st.selectbox("Occupation / व्यवसाय", ["Student", "Farmer", "Unemployed", "Worker"])

    if st.button("🔍 Find My Schemes"):

        schemes = []

        if occupation == "Student":
            schemes.append({
                "name_en": "National Scholarship Scheme",
                "name_hi": "राष्ट्रीय छात्रवृत्ति योजना",
                "desc_en": "Financial support for students.",
                "desc_hi": "छात्रों के लिए आर्थिक सहायता।",
                "link": "https://scholarships.gov.in"
            })

        if occupation == "Farmer":
            schemes.append({
                "name_en": "PM Kisan Yojana",
                "name_hi": "प्रधानमंत्री किसान योजना",
                "desc_en": "₹6000 yearly financial support for farmers.",
                "desc_hi": "किसानों को ₹6000 वार्षिक सहायता।",
                "link": "https://pmkisan.gov.in"
            })

        if income < 300000:
            schemes.append({
                "name_en": "Ayushman Bharat",
                "name_hi": "आयुष्मान भारत योजना",
                "desc_en": "Free health insurance up to ₹5 lakh.",
                "desc_hi": "₹5 लाख तक मुफ्त स्वास्थ्य बीमा।",
                "link": "https://pmjay.gov.in"
            })

        if schemes:
            for scheme in schemes:
                name = scheme["name_hi"] if language == "Hindi" else scheme["name_en"]
                desc = scheme["desc_hi"] if language == "Hindi" else scheme["desc_en"]

                st.markdown(f"""
                <div class="scheme-card">
                    <div class="scheme-title">📜 {name}</div>
                    <p>{desc}</p>
                    <a href="{scheme['link']}" target="_blank" class="apply-btn">Apply Here</a>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No schemes found based on provided details.")