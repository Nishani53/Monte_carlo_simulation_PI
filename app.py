import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Monte Carlo Pi Simulator", layout="wide")

# --- Theory Section with Static Diagram ---
st.title("🧮 Monte Carlo Estimation of π")

# 1. Create a static explanatory diagram
fig_theory, ax_t = plt.subplots(figsize=(4, 4))
ax_t.set_xlim(0, 1.1)
ax_t.set_ylim(0, 1.1)
ax_t.set_aspect('equal')

# Draw Square and Circle
square = plt.Rectangle((0, 0), 1, 1, color='lightgray', alpha=0.3, label='Square (Area = 1)')
ax_t.add_patch(square)
theta = np.linspace(0, np.pi/2, 100)
ax_t.plot(np.cos(theta), np.sin(theta), color='black', lw=2, label='Circle (Area = π/4)')
ax_t.fill_between(np.cos(theta), 0, np.sin(theta), color='blue', alpha=0.1)

# Annotations
ax_t.text(0.5, 0.5, r'$x^2 + y^2 \leq 1$', fontsize=12, ha='center', color='blue')
ax_t.set_title("Geometric Model")
ax_t.set_xlabel("x")
ax_t.set_ylabel("y")

# Display the diagram and the text side-by-side
col_a, col_b = st.columns([1, 2])
with col_a:
    st.pyplot(fig_theory)
with col_b:
    st.markdown(r"""
    ### The Mathematical Foundation
    The Monte Carlo method uses **random sampling** to solve deterministic problems. 
    To estimate $\pi$, we use the ratio between a square and an inscribed quarter-circle.

    **1. Areas:**
    - Square ($A_s$): $r^2 = 1$
    - Quarter-Circle ($A_c$): $\frac{1}{4} \pi r^2 = \frac{\pi}{4}$

    **2. The Logic:**
    By scattering $N$ random points, the ratio of points inside the circle to total points equals the ratio of their areas:
    $$\frac{N_{in}}{N_{total}} \approx \frac{A_c}{A_s} = \frac{\pi}{4}$$
    
    **3. The Result:**
    $$\pi \approx 4 \times \frac{N_{in}}{N_{total}}$$
    """)

st.divider() # Adds a nice visual line before the simulation


# --- Main Body Inputs (Replaces Sidebar) ---
st.subheader("Simulation Settings")

# Using columns so it looks good on wide screens, but stacks on mobile
input_col1, input_col2 = st.columns([2, 1])

with input_col1:
    num_obs = st.number_input(
        "How many observations?", 
        min_value=100, 
        max_value=100000, 
        value=1000, 
        step=500
    )

with input_col2:
    # Adding a bit of padding so the button aligns with the input field
    st.write("##") 
    run_btn = st.button("🚀 Run Simulation", use_container_width=True)

# Everything below this (the if run_btn: logic) stays exactly the same!

if run_btn:
    # Setup Plotting
    col1, col2 = st.columns(2)
    with col1:
        sim_placeholder = st.empty()
    with col2:
        graph_placeholder = st.empty()
    
    # Simulation Data
    x_in, y_in, x_out, y_out = [], [], [], []
    pi_values = []
    counts = []
    
    # Run loop in batches for "animation" effect
    batch_size = max(1, num_obs // 50)
    for i in range(0, num_obs, batch_size):
        x = np.random.rand(batch_size)
        y = np.random.rand(batch_size)
        hits = (x**2 + y**2) <= 1
        
        x_in.extend(x[hits]); y_in.extend(y[hits])
        x_out.extend(x[~hits]); y_out.extend(y[~hits])
        
        current_total = len(x_in) + len(x_out)
        current_pi = 4 * (len(x_in) / current_total)
        pi_values.append(current_pi)
        counts.append(current_total)

        # Draw Simulation Frame
        fig1, ax1 = plt.subplots(figsize=(5, 5))
        ax1.set_xlim(0, 1); ax1.set_ylim(0, 1)
        ax1.scatter(x_in, y_in, color='blue', s=2, alpha=0.5)
        ax1.scatter(x_out, y_out, color='red', s=2, alpha=0.5)
        theta = np.linspace(0, np.pi/2, 100)
        ax1.plot(np.cos(theta), np.sin(theta), color='black')
        ax1.set_title(f"Points: {current_total}")
        sim_placeholder.pyplot(fig1)
        plt.close(fig1)

        # Draw Graph Frame
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        ax2.plot(counts, pi_values, color='black')
        ax2.axhline(y=np.pi, color='green', linestyle='--')
        ax2.set_ylim(2.5, 3.8)
        ax2.set_title(f"Current π ≈ {current_pi:.4f}")
        graph_placeholder.pyplot(fig2)
        plt.close(fig2)
        
        time.sleep(0.05) # Control animation speed

    st.success(f"Final Estimation after {num_obs} points: {current_pi:.6f}")
