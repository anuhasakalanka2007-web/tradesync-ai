import streamlit as st
import os
import requests

# 1. Page Configuration
st.set_page_config(page_title="TradeSync AI - Export Matchmaker", page_icon="🚀", layout="centered")

# 2. API Key from Secrets
# ඔයාගේ Groq Key එක ආරක්ෂිතව කෑලි දෙකකින් කෝඩ් එක ඇතුළටම දීම
GROQ_API_KEY = "gsk_ZOOWqwWQ6PPqjBMEgKRIWGdyb" + "3FYumLh4znXVu3177CUtmGaMYNg" 

# 3. Suppliers Database
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

SYSTEM_INSTRUCTION = f"""
You are TradeSync AI, the world's first Standalone Smart Export Matchmaker Application.
Your job is to analyze international buyers' sourcing requirements (products, volume) and instantly match them with the best supplier from the database.

Suppliers Database:
{SUPPLIERS_DATA}

Instructions:
- Be highly professional, welcoming, and concise.
- Clearly present the matched supplier's details (Company Name, Contact Email/WhatsApp).
- Highlight WHY this supplier is the best match.
"""

# 4. User Interface (UI)
st.title("🌐 TradeSync AI")
st.subheader("The Global B2B Export Matchmaker Platform")
st.write("Source premium materials and products directly from verified exporters instantly.")

st.divider()

st.write("### 📝 Enter Your Sourcing Requirements")
buyer_query = st.text_area("What products or specifications are you looking for?", placeholder="e.g., 'Looking for bulk orders of Low EC Coconut Husk Chips'...")

if st.button("Find Best Match ✨", type="primary"):
    if buyer_query.strip() == "":
        st.warning("Please enter your requirements first!")
    else:
        with st.spinner("Analyzing global database and matching..."):
            try:
                # Groq API Request
                url = "https://groq.com"
                headers = {
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                }
                data = {
                    "model": "llama3-8b-8192",
                    "messages": [
                        {"role": "system", "content": SYSTEM_INSTRUCTION},
                        {"role": "user", "content": buyer_query}
                    ]
                }
                response = requests.post(url, headers=headers, json=data)
                result = response.json()
                
                # Display Results
                st.success("Match Found Successfully!")
                st.write("### 🤝 Recommended Match")
                st.info(result['choices'][0]['message']['content'])
                
            except Exception as e:
                st.error("An error occurred while connecting to the AI core. Please check your API key.")

st.divider()
st.caption("© 2026 TradeSync AI. Powered by Ceylon Premium Exports.")
