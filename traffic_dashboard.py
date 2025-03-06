import streamlit as st
import matplotlib.pyplot as plt

def plot_traffic(vehicle_counts):
    lanes = ['Lane 1', 'Lane 2', 'Lane 3', 'Lane 4']
    plt.bar(lanes, vehicle_counts, color=['red', 'blue', 'green', 'orange'])
    plt.xlabel('Lanes')
    plt.ylabel('Vehicle Count')
    plt.title('Live Traffic Visualization')
    st.pyplot(plt)

st.title("🚦 AI-Powered Traffic Management")
st.write("Real-time traffic control using AI!")


vehicle_counts = [10, 15, 20, 25]
plot_traffic(vehicle_counts)
