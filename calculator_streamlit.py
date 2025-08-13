import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Calculator",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'calculation_history' not in st.session_state:
    st.session_state.calculation_history = []
if 'display_value' not in st.session_state:
    st.session_state.display_value = "0"
if 'previous_value' not in st.session_state:
    st.session_state.previous_value = None
if 'operation' not in st.session_state:
    st.session_state.operation = None
if 'waiting_for_number' not in st.session_state:
    st.session_state.waiting_for_number = False
if 'memory_value' not in st.session_state:
    st.session_state.memory_value = 0

# Custom CSS for beautiful, responsive calculator styling
st.markdown("""
<style>
/* Main container styling */
.main-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Calculator container */
.calculator-container {
    background: linear-gradient(145deg, #f0f0f0, #e6e6e6);
    padding: 30px;
    border-radius: 25px;
    box-shadow: 
        0 20px 40px rgba(0,0,0,0.1),
        inset 0 1px 0 rgba(255,255,255,0.8);
    max-width: 500px;
    margin: 0 auto;
    border: 1px solid rgba(255,255,255,0.3);
}

/* Display area */
.display-area {
    background: linear-gradient(145deg, #ffffff, #f8f9fa);
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 25px;
    text-align: right;
    font-family: 'Courier New', monospace;
    font-size: 2.5em;
    font-weight: bold;
    border: 2px solid #e9ecef;
    min-height: 80px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    box-shadow: 
        inset 0 2px 4px rgba(0,0,0,0.1),
        0 4px 8px rgba(0,0,0,0.05);
    color: #2c3e50;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* Button grid container */
.button-grid {
    display: grid;
    gap: 12px;
    margin-bottom: 20px;
}

/* Memory row */
.memory-row {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 8px;
    margin-bottom: 15px;
}

/* Function row */
.function-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 15px;
}

/* Clear row */
.clear-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 15px;
}

/* Number pad */
.number-pad {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
}

/* Button base styles */
.calc-button {
    background: linear-gradient(145deg, #e0e0e0, #d0d0d0);
    border: none;
    padding: 18px 12px;
    border-radius: 15px;
    font-size: 1.3em;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.2s ease;
    color: #2c3e50;
    box-shadow: 
        0 4px 8px rgba(0,0,0,0.1),
        inset 0 1px 0 rgba(255,255,255,0.8);
    min-height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
}

.calc-button:hover {
    background: linear-gradient(145deg, #d0d0d0, #c0c0c0);
    transform: translateY(-2px);
    box-shadow: 
        0 6px 12px rgba(0,0,0,0.15),
        inset 0 1px 0 rgba(255,255,255,0.8);
}

.calc-button:active {
    transform: translateY(0);
    box-shadow: 
        0 2px 4px rgba(0,0,0,0.1),
        inset 0 1px 0 rgba(255,255,255,0.8);
}

/* Operator buttons */
.operator-button {
    background: linear-gradient(145deg, #ff9500, #e6850e);
    color: white;
    font-size: 1.5em;
}

.operator-button:hover {
    background: linear-gradient(145deg, #e6850e, #d6750d);
}

/* Clear buttons */
.clear-button {
    background: linear-gradient(145deg, #ff3b30, #d70015);
    color: white;
}

.clear-button:hover {
    background: linear-gradient(145deg, #d70015, #b50012);
}

/* Equals button */
.equals-button {
    background: linear-gradient(145deg, #007aff, #0056b3);
    color: white;
    font-size: 1.5em;
}

.equals-button:hover {
    background: linear-gradient(145deg, #0056b3, #004499);
}

/* Memory buttons */
.memory-button {
    background: linear-gradient(145deg, #8e8e93, #7a7a7f);
    color: white;
    font-size: 0.9em;
    padding: 15px 8px;
    min-height: 50px;
}

.memory-button:hover {
    background: linear-gradient(145deg, #7a7a7f, #66666a);
}

/* Function buttons */
.function-button {
    background: linear-gradient(145deg, #a5a5a5, #959595);
    color: white;
    font-size: 1.1em;
}

.function-button:hover {
    background: linear-gradient(145deg, #959595, #858585);
}

/* History section */
.history-section {
    background: linear-gradient(145deg, #ffffff, #f8f9fa);
    padding: 25px;
    border-radius: 20px;
    margin-top: 30px;
    border: 1px solid #e9ecef;
    box-shadow: 
        0 8px 16px rgba(0,0,0,0.1),
        inset 0 1px 0 rgba(255,255,255,0.8);
}

.history-title {
    color: #2c3e50;
    font-size: 1.5em;
    font-weight: bold;
    margin-bottom: 20px;
    text-align: center;
}

.history-item {
    background: #f8f9fa;
    padding: 12px 16px;
    margin: 8px 0;
    border-radius: 10px;
    border-left: 4px solid #007aff;
    font-family: 'Courier New', monospace;
    font-size: 1.1em;
    color: #2c3e50;
}

.clear-history-btn {
    background: linear-gradient(145deg, #6c757d, #5a6268);
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 10px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.2s ease;
    margin-top: 15px;
    width: 100%;
}

.clear-history-btn:hover {
    background: linear-gradient(145deg, #5a6268, #495057);
    transform: translateY(-1px);
}

/* Responsive design */
@media (max-width: 768px) {
    .calculator-container {
        padding: 20px;
        margin: 10px;
        border-radius: 20px;
    }
    
    .display-area {
        font-size: 2em;
        padding: 20px;
        min-height: 60px;
    }
    
    .calc-button {
        padding: 15px 8px;
        font-size: 1.1em;
        min-height: 50px;
    }
    
    .memory-button {
        padding: 12px 6px;
        font-size: 0.8em;
        min-height: 40px;
    }
    
    .button-grid {
        gap: 8px;
    }
    
    .memory-row, .function-row, .clear-row, .number-pad {
        gap: 8px;
    }
}

@media (max-width: 480px) {
    .calculator-container {
        padding: 15px;
        margin: 5px;
    }
    
    .display-area {
        font-size: 1.8em;
        padding: 15px;
    }
    
    .calc-button {
        padding: 12px 6px;
        font-size: 1em;
        min-height: 45px;
    }
    
    .memory-button {
        padding: 10px 4px;
        font-size: 0.7em;
        min-height: 35px;
    }
}

/* Streamlit button overrides */
.stButton > button {
    width: 100% !important;
    height: auto !important;
    margin: 0 !important;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

.stButton > button:hover {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* Hide Streamlit default elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Custom scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb {
    background: #c1c1c1;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #a8a8a8;
}
</style>
""", unsafe_allow_html=True)

# Calculator functions
def clear_display():
    st.session_state.display_value = "0"
    st.session_state.previous_value = None
    st.session_state.operation = None
    st.session_state.waiting_for_number = False

def append_number(num):
    if st.session_state.waiting_for_number:
        st.session_state.display_value = str(num)
        st.session_state.waiting_for_number = False
    else:
        if st.session_state.display_value == "0":
            st.session_state.display_value = str(num)
        else:
            st.session_state.display_value += str(num)

def set_operation(op):
    try:
        if st.session_state.previous_value is not None and not st.session_state.waiting_for_number:
            calculate()
        st.session_state.previous_value = float(st.session_state.display_value)
        st.session_state.operation = op
        st.session_state.waiting_for_number = True
    except ValueError:
        st.error("Invalid number format!")

def calculate():
    try:
        if st.session_state.operation and st.session_state.previous_value is not None:
            current = float(st.session_state.display_value)
            if st.session_state.operation == "+":
                result = st.session_state.previous_value + current
            elif st.session_state.operation == "-":
                result = st.session_state.previous_value - current
            elif st.session_state.operation == "×":
                result = st.session_state.previous_value * current
            elif st.session_state.operation == "÷":
                if current == 0:
                    st.error("Cannot divide by zero!")
                    return
                result = st.session_state.previous_value / current
            
            # Add to history
            calculation_string = f"{st.session_state.previous_value} {st.session_state.operation} {current} = {result}"
            if calculation_string not in st.session_state.calculation_history:
                st.session_state.calculation_history.append(calculation_string)
            
            st.session_state.display_value = str(result)
            st.session_state.previous_value = None
            st.session_state.operation = None
    except ValueError:
        st.error("Invalid calculation!")

def percentage():
    try:
        current = float(st.session_state.display_value)
        result = current / 100
        st.session_state.display_value = str(result)
    except ValueError:
        st.error("Invalid number!")

def square_root():
    try:
        current = float(st.session_state.display_value)
        if current < 0:
            st.error("Cannot calculate square root of negative number!")
            return
        result = current ** 0.5
        st.session_state.display_value = str(result)
    except ValueError:
        st.error("Invalid number!")

def square():
    try:
        current = float(st.session_state.display_value)
        result = current ** 2
        st.session_state.display_value = str(result)
    except ValueError:
        st.error("Invalid number!")

def reciprocal():
    try:
        current = float(st.session_state.display_value)
        if current == 0:
            st.error("Cannot calculate reciprocal of zero!")
            return
        result = 1 / current
        st.session_state.display_value = str(result)
    except ValueError:
        st.error("Invalid number!")

def plus_minus():
    try:
        current = float(st.session_state.display_value)
        st.session_state.display_value = str(-current)
    except ValueError:
        st.error("Invalid number!")

def decimal():
    if "." not in st.session_state.display_value:
        st.session_state.display_value += "."

# Memory functions
def memory_clear():
    st.session_state.memory_value = 0
    st.success("Memory cleared!")

def memory_recall():
    st.session_state.display_value = str(st.session_state.memory_value)
    st.session_state.waiting_for_number = False

def memory_add():
    try:
        current = float(st.session_state.display_value)
        st.session_state.memory_value += current
        st.success(f"Added {current} to memory!")
    except ValueError:
        st.error("Invalid number!")

def memory_subtract():
    try:
        current = float(st.session_state.display_value)
        st.session_state.memory_value -= current
        st.success(f"Subtracted {current} from memory!")
    except ValueError:
        st.error("Invalid number!")

def memory_store():
    try:
        current = float(st.session_state.display_value)
        st.session_state.memory_value = current
        st.success(f"Stored {current} in memory!")
    except ValueError:
        st.error("Invalid number!")

def memory_power():
    try:
        current = float(st.session_state.display_value)
        if st.session_state.memory_value != 0:
            result = st.session_state.memory_value ** current
            st.session_state.display_value = str(result)
        else:
            st.error("Memory value is 0!")
    except ValueError:
        st.error("Invalid number!")

# Main calculator interface
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Title with better styling
st.markdown("""
<div style="text-align: center; margin-bottom: 30px;">
    <h1 style="color: #2c3e50; font-size: 3em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);">
        🧮 Calculator
    </h1>
    <p style="color: #7f8c8d; font-size: 1.2em; margin: 10px 0 0 0;">
        Professional Calculator with Memory & History
    </p>
</div>
""", unsafe_allow_html=True)

# Calculator container
st.markdown('<div class="calculator-container">', unsafe_allow_html=True)

# Display area
st.markdown(f'<div class="display-area">{st.session_state.display_value}</div>', unsafe_allow_html=True)

# Memory row
st.markdown('<div class="button-grid memory-row">', unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    if st.button("MC", key="mc", help="Memory Clear"):
        memory_clear()
with col2:
    if st.button("MR", key="mr", help="Memory Recall"):
        memory_recall()
with col3:
    if st.button("M+", key="mplus", help="Memory Add"):
        memory_add()
with col4:
    if st.button("M-", key="mminus", help="Memory Subtract"):
        memory_subtract()
with col5:
    if st.button("MS", key="ms", help="Memory Store"):
        memory_store()
with col6:
    if st.button("M^", key="mpower", help="Memory Power"):
        memory_power()
st.markdown('</div>', unsafe_allow_html=True)

# Function row
st.markdown('<div class="button-grid function-row">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("%", key="percent", help="Percentage"):
        percentage()
with col2:
    if st.button("√", key="sqrt", help="Square Root"):
        square_root()
with col3:
    if st.button("x²", key="square", help="Square"):
        square()
with col4:
    if st.button("1/x", key="reciprocal", help="Reciprocal"):
        reciprocal()
st.markdown('</div>', unsafe_allow_html=True)

# Clear row
st.markdown('<div class="button-grid clear-row">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("CE", key="ce", help="Clear Entry"):
        st.session_state.display_value = "0"
with col2:
    if st.button("C", key="clear", help="Clear"):
        clear_display()
with col3:
    if st.button("⌫", key="backspace", help="Backspace"):
        if len(st.session_state.display_value) > 1:
            st.session_state.display_value = st.session_state.display_value[:-1]
        else:
            st.session_state.display_value = "0"
with col4:
    if st.button("÷", key="divide", help="Divide"):
        set_operation("÷")
st.markdown('</div>', unsafe_allow_html=True)

# Number pad and operators
st.markdown('<div class="button-grid number-pad">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("7", key="7"):
        append_number(7)
with col2:
    if st.button("8", key="8"):
        append_number(8)
with col3:
    if st.button("9", key="9"):
        append_number(9)
with col4:
    if st.button("×", key="multiply", help="Multiply"):
        set_operation("×")

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("4", key="4"):
        append_number(4)
with col2:
    if st.button("5", key="5"):
        append_number(5)
with col3:
    if st.button("6", key="6"):
        append_number(6)
with col4:
    if st.button("-", key="subtract", help="Subtract"):
        set_operation("-")

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("1", key="1"):
        append_number(1)
with col2:
    if st.button("2", key="2"):
        append_number(2)
with col3:
    if st.button("3", key="3"):
        append_number(3)
with col4:
    if st.button("+", key="add", help="Add"):
        set_operation("+")

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("±", key="plusminus", help="Plus/Minus"):
        plus_minus()
with col2:
    if st.button("0", key="0"):
        append_number(0)
with col3:
    if st.button(".", key="decimal", help="Decimal"):
        decimal()
with col4:
    if st.button("=", key="equals", help="Equals"):
        calculate()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Calculation History Section
st.markdown('<div class="history-section">', unsafe_allow_html=True)
st.markdown('<div class="history-title">📚 Calculation History</div>', unsafe_allow_html=True)

if st.session_state.calculation_history:
    # Display history in reverse order (most recent first)
    for i, calc in enumerate(reversed(st.session_state.calculation_history)):
        st.markdown(f'<div class="history-item">{len(st.session_state.calculation_history) - i}. {calc}</div>', unsafe_allow_html=True)
    
    # Add clear history button
    if st.button("🗑️ Clear History", key="clear_history"):
        st.session_state.calculation_history.clear()
        st.rerun()
else:
    st.info("No calculations yet. Start calculating to see your history here!")
    st.markdown('<div style="text-align: center; color: #7f8c8d; font-style: italic; margin-top: 20px;">Try some calculations above! 🧮</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer with better styling
st.markdown("""
<div style="text-align: center; margin-top: 40px; padding: 20px; color: #7f8c8d; border-top: 1px solid #ecf0f1;">
    <p style="margin: 0; font-size: 1.1em;">
        Built with ❤️ using Streamlit • Professional Calculator App 🎉
    </p>
    <p style="margin: 5px 0 0 0; font-size: 0.9em;">
        Responsive design for desktop and mobile devices
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
