import streamlit as st
import math
import random

# Set page configuration
st.set_page_config(
    page_title="Fun with Numbers Calculator",
    page_icon="🧮",
    layout="centered"
)

# Custom CSS for fun effects and better readability
st.markdown("""
<style>
/* Fun gradient background */
.main .block-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}

/* Fun title styling */
h1 {
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4);
    background-size: 400% 400%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradient 3s ease infinite;
    text-align: center;
    font-size: 3em;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    font-weight: 800;
    letter-spacing: 2px;
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Fun sidebar styling */
.sidebar .sidebar-content {
    background: linear-gradient(180deg, #ff9a9e 0%, #fecfef 100%);
    border-radius: 15px;
    padding: 1rem;
    margin: 1rem;
}

/* Fun button effects */
.stButton > button {
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
    border: none;
    border-radius: 25px;
    color: white;
    font-weight: bold;
    padding: 0.5rem 1rem;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    font-size: 1.1em;
    letter-spacing: 1px;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    background: linear-gradient(45deg, #4ecdc4, #ff6b6b);
}

/* Fun success message */
.stSuccess {
    background: linear-gradient(45deg, #4ecdc4, #44a08d);
    border-radius: 15px;
    padding: 1rem;
    border: none;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    font-weight: 600;
    font-size: 1.1em;
    letter-spacing: 0.5px;
}

/* Fun error message */
.stError {
    background: linear-gradient(45deg, #ff6b6b, #ee5a52);
    border-radius: 15px;
    padding: 1rem;
    border: none;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    font-weight: 600;
    font-size: 1.1em;
    letter-spacing: 0.5px;
}

/* Fun number input styling */
.stNumberInput > div > div > input {
    border-radius: 15px;
    border: 2px solid #4ecdc4;
    background: #ffffff !important;
    color: #2c3e50 !important;
    padding: 0.5rem;
    transition: all 0.3s ease;
    font-size: 1.1em;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.stNumberInput > div > div > input:focus {
    border-color: #ff6b6b;
    box-shadow: 0 0 15px rgba(255,107,107,0.3);
    transform: scale(1.02);
    background: #ffffff !important;
}

/* Fun selectbox styling */
.stSelectbox > div > div > div {
    border-radius: 15px;
    border: 2px solid #4ecdc4;
    background: #ffffff !important;
    color: #2c3e50 !important;
    font-size: 1.1em;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

/* Celebration animation */
@keyframes celebrate {
    0% { transform: scale(1) rotate(0deg); }
    25% { transform: scale(1.1) rotate(5deg); }
    50% { transform: scale(1.2) rotate(-5deg); }
    75% { transform: scale(1.1) rotate(5deg); }
    100% { transform: scale(1) rotate(0deg); }
}

.celebrate {
    animation: celebrate 0.5s ease-in-out;
}

/* Enhanced text readability */
h2, h3 {
    color: white;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.9);
    font-weight: 800;
    letter-spacing: 1px;
    text-align: center;
    background: rgba(0,0,0,0.7);
    padding: 0.5rem 1rem;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.2);
}

/* Better subheader styling */
.subheader {
    background: linear-gradient(45deg, rgba(0,0,0,0.8), rgba(0,0,0,0.6));
    padding: 1rem;
    border-radius: 15px;
    border: 2px solid rgba(255,255,255,0.3);
    margin: 1rem 0;
    text-align: center;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* Enhanced result display */
.result-box {
    background: linear-gradient(45deg, rgba(0,0,0,0.8), rgba(0,0,0,0.6));
    padding: 1.5rem;
    border-radius: 20px;
    border: 2px solid rgba(255,255,255,0.3);
    margin: 1rem 0;
    backdrop-filter: blur(15px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* Better button text */
.button-text {
    font-family: 'Arial', sans-serif;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Enhanced math fact display */
.math-fact-box {
    background: linear-gradient(45deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
    padding: 1.5rem;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.3);
    margin: 1rem 0;
    backdrop-filter: blur(10px);
    font-size: 1.1em;
    line-height: 1.6;
    text-align: center;
}

/* Better input labels */
.input-label {
    background: rgba(0,0,0,0.8);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.3);
    font-weight: 600;
    text-align: center;
    margin: 0.5rem 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

st.title("🧮 Fun with Numbers Calculator")
st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <p style="color: white; font-size: 1.3em; text-shadow: 2px 2px 4px rgba(0,0,0,0.7); font-weight: 600; letter-spacing: 1px;">
        🎉 A fun and interactive calculator with basic arithmetic operations and advanced math functions! 🚀
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar operation
st.sidebar.header("🎯 Choose Operation")
operation = st.sidebar.selectbox(
    "Select an operation:",
    ["➕ Addition", "➖ Subtraction", "✖️ Multiplication", "➗ Division", "📈 Exponential", "√ Square Root", "🔢 Absolute Value", "💯 Percentage"]
)

# Number inputs
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="subheader">', unsafe_allow_html=True)
    st.subheader("🔢 Input Numbers")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if operation in ["➕ Addition", "➖ Subtraction", "✖️ Multiplication", "➗ Division"]:
        st.markdown('<div class="input-label">First Number</div>', unsafe_allow_html=True)
        num1 = st.number_input("", value=0.0, step=0.1, key="num1")
        st.markdown('<div class="input-label">Second Number</div>', unsafe_allow_html=True)
        num2 = st.number_input("", value=0.0, step=0.1, key="num2")
    else:
        st.markdown('<div class="input-label">Enter Number</div>', unsafe_allow_html=True)
        num1 = st.number_input("", value=0.0, step=0.1, key="num1")
        num2 = None

with col2:
    st.markdown('<div class="subheader">', unsafe_allow_html=True)
    st.subheader("📊 Result")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    if operation == "➕ Addition":
        result = num1 + num2
        st.success(f"**{num1} + {num2} = {result}** 🎉")
        if random.random() < 0.3:  # 30% chance for balloons
            st.balloons()
    elif operation == "➖ Subtraction":
        result = num1 - num2
        st.success(f"**{num1} - {num2} = {result}** ✨")
        if random.random() < 0.3:
            st.balloons()
    elif operation == "✖️ Multiplication":
        result = num1 * num2
        st.success(f"**{num1} × {num2} = {result}** 🚀")
        if random.random() < 0.3:
            st.balloons()
    elif operation == "➗ Division":
        if num2 == 0:
            st.error("❌ Cannot divide by zero! 💥")
        else:
            result = num1 / num2
            st.success(f"**{num1} ÷ {num2} = {result}** 🎊")
            if random.random() < 0.3:
                st.balloons()
    elif operation == "📈 Exponential":
        result = math.exp(num1)
        st.success(f"**e^{num1} = {result:.6f}** 🌟")
        if random.random() < 0.4:  # Higher chance for advanced functions
            st.balloons()
            st.snow()
    elif operation == "√ Square Root":
        if num1 < 0:
            st.error("❌ Cannot calculate square root of negative number! 💥")
        else:
            result = math.sqrt(num1)
            st.success(f"**√{num1} = {result}** 🌈")
            if random.random() < 0.4:
                st.balloons()
                st.snow()
    elif operation == "🔢 Absolute Value":
        result = abs(num1)
        st.success(f"**|{num1}| = {result}** ⭐")
        if random.random() < 0.4:
            st.balloons()
            st.snow()
    elif operation == "💯 Percentage":
        result = num1 / 100
        st.success(f"**{num1}% = {result}** 🎯")
        if random.random() < 0.4:
            st.balloons()
            st.snow()
    st.markdown('</div>', unsafe_allow_html=True)

# Fun celebration section
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <h3 style="color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.7); font-weight: 700; letter-spacing: 1px;">
        🎉 Celebration Zone! 🎉
    </h3>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎈 Launch Balloons!", key="balloons_btn"):
        st.balloons()
        st.success("🎈 Balloons launched! Yay!")

with col2:
    if st.button("❄️ Make it Snow!", key="snow_btn"):
        st.snow()
        st.success("❄️ It's snowing! Winter magic!")

with col3:
    if st.button("🎊 Party Time!", key="party_btn"):
        st.balloons()
        st.snow()
        st.success("🎊 Party mode activated! Woo-hoo!")

# Fun math facts with random selection
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <h3 style="color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.7); font-weight: 700; letter-spacing: 1px;">
        🌟 Fun Math Facts! 🌟
    </h3>
</div>
""", unsafe_allow_html=True)

math_facts = [
    "🎯 **42**: The answer to life, the universe, and everything! (Douglas Adams)",
    "🔢 **0**: Zero is the hero of mathematics!",
    "✨ **1**: Unity is the building block of numbers!",
    "🥧 **π**: Pi is approximately 3.14159...",
    "📈 **e**: Euler's number is approximately 2.71828...",
    "🚀 **∞**: Infinity is not a number, it's a concept!",
    "🌈 **i**: The imaginary unit, where i² = -1",
    "🎲 **φ**: The golden ratio is approximately 1.618..."
]

if st.button("🎲 Show Random Math Fact!", key="fact_btn"):
    random_fact = random.choice(math_facts)
    st.markdown(f'<div class="math-fact-box">{random_fact}</div>', unsafe_allow_html=True)
    st.balloons()

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.7);">
    <p style="font-size: 1.2em; margin: 0; font-weight: 600; letter-spacing: 1px;">
        Built with ❤️ using Streamlit • Fun with Numbers Calculator 🎉
    </p>
    <p style="font-size: 1em; margin: 8px 0 0 0; font-weight: 500; letter-spacing: 0.5px;">
        🚀 Making math fun, one calculation at a time! ✨
    </p>
</div>
""", unsafe_allow_html=True)
