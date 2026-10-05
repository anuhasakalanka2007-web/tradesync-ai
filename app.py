import streamlit as st
import google.generativeai as genai

# 1. Page Configuration (වෙබ් පිටුවේ පෙනුම සැකසීම)
st.set_page_config(page_title="TradeSync AI - Export Matchmaker", page_icon="🌐", layout="centered")

# 2. API Key සැකසීම (මෙහි ඔයාගේ Gemini Key එක ඇතුළත් කරන්න)
GEMINI_API_KEY = st.secrets["KEY_PART1"] + st.secrets["KEY_PART2"]
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# 3. අපනයනකරුවන්ගේ දත්ත (Suppliers Database)
SUPPLIERS_DATA = """
1. Company: Ceylon Premium Exports
   Products: Fresh Coconut, Coconut Husk Chips, Spices (Cinnamon, Black Pepper, Cloves, Turmeric), Mushroom Grow Bags.
   Specialty: 100% Traceable, Premium Grade, Low EC Coir substrates, Direct supply chain.
   Contact: ceylonpremiumexports1@gmail.com
   WhatsApp: +94782892202

2. Company: Lanka Agro Organics
   Products: Organic Tea, Cardamom, Vanilla.
   Specialty: EU Organic Certified.
   Contact: info@lankaagro.com
"""

# AI System Instruction
SYSTEM_INSTRUCTION = f"""
You are TradeSync AI, the world's first Standalone Smart Export Matchmaker Application.
Your job is to analyze international buyers' sourcing requirements (products, specific technical specs like Low EC, pH, volume) and instantly match them with the best supplier from the database.

Suppliers Database:
{SUPPLIERS_DATA}

Instructions:
- Be highly professional, welcoming, and concise.
- Clearly present the matched supplier's details (Company Name, Contact Email/WhatsApp).
- Highlight WHY this supplier is the best match based on the buyer's query.
- Never mention product samples unless requested.
"""

# 4. User Interface (UI) සැලසුම
st.title("🌐 TradeSync AI")
st.subheader("The Global B2B Export Matchmaker Platform")
st.write("Source premium materials and products directly from verified exporters instantly.")

st.divider()

# Buyer Input Section
st.write("### 📝 Enter Your Sourcing Requirements")
buyer_query = st.text_area(
    "What products or specifications are you looking for?", 
    placeholder="e.g., 'Looking for bulk orders of Low EC Coconut Husk Chips for Orchid cultivation' or 'Need Premium Grade Ceylon Cinnamon Alba'..."
)

# Match Button
if st.button("Find Best Match ✨", type="primary"):
    if buyer_query.strip() == "":
        st.warning("Please enter your requirements first!")
    else:
        with st.spinner("Analyzing global database and matching..."):
            try:
                # Gemini AI Processing
                prompt = f"{SYSTEM_INSTRUCTION}\n\nBuyer Request: {buyer_query}\n\nProvide the best match with dynamic explanation:"
                response = model.generate_content(prompt)
                
                # Display Results
                st.success("Match Found Successfully!")
                st.write("### 🤝 Recommended Match")
                st.info(response.text)
                
            except Exception as e:
                st.error("An error occurred while connecting to the AI core. Please check your API key.")

st.divider()
st.caption("© 2026 TradeSync AI. Powered by Ceylon Premium Exports.") 
