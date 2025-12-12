import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import random  # Random data for demo

st.set_page_config(page_title="Hamro Suraksha - by KING", layout="wide", page_icon="🇳🇵")

st.title("🇳🇵 Hamro Suraksha")
st.markdown("### Real-time Public Safety Dashboard for Nepal\n**Created by KING**")

# Demo data for Nepal districts (तिम्रो accident data जोड्न सकिन्छ)
districts = ['Kathmandu', 'Pokhara', 'Birgunj', 'Itahari', 'Dharan', 'Butwal', 'Janakpur', 'Nepalgunj', 'Hetauda', 'Dhangadhi']
data = pd.DataFrame({
    'place': random.choices(districts, k=20),
    'type': random.choices(['Accident', 'Theft', 'Flood Alert', 'Landslide', 'Robbery'], k=20),
    'risk': [random.randint(60, 100) for _ in range(20)],
    'lat': [random.uniform(26, 30) for _ in range(20)],  # Nepal lat range
    'lon': [random.uniform(80, 88) for _ in range(20)]   # Nepal lon range
})

# Nepal map
m = folium.Map(location=[28.3949, 84.1240], zoom_start=7, tiles="CartoDB dark_matter")

# Add markers
for i, row in data.iterrows():
    color = "red" if row['risk'] > 85 else "orange" if row['risk'] > 70 else "green"
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=row['risk']/5,
        color=color,
        fill=True,
        fill_opacity=0.7,
        popup=f"<b>{row['place']}</b><br>Type: {row['type']}<br>Risk: {row['risk']}/100"
    ).add_to(m)

st_folium(m, width=1200, height=500)

# Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Highest Risk", max(data['risk']), "94 🔥")
with col2:
    st.metric("Total Alerts", len(data), "+5")
with col3:
    st.metric("Safest District", min(data['risk']), "68 ✅")

st.markdown("---")
phone = st.text_input("तपाईंको मोबाइल नम्बर (९८xxxxxxxxxx)")
if st.button("सुरक्षा अलर्ट सक्रिय गर्नुहोस् 🚨"):
    st.success(f"Alert सक्रिय! {phone} मा SMS पठाइयो।")

st.caption("Made with ❤️ by KING • 2025 | Nepal's First Safety App")