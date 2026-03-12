import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Monte Carlo Pi Simulator", layout="wide")

# --- Theory Section ---
st.title("🧮 Monte Carlo Estimation of π")

st.markdown(r"""
### The Mathematical Foundation

The Monte Carlo method is a stochastic technique based on **probability** and **random sampling**. 
To estimate the value of $\pi$, we use the geometric relationship between a square and an inscribed quarter-circle.

#### 1. Geometric Setup
Consider a square with side length $r = 1$ placed in the first quadrant of a Cartesian plane. Inside this square, we draw a quarter-circle centered at the origin $(0,0)$.

*   **Area of the Square ($A_s$):**
    $$A_s = r^2 = 1^2 = 1$$
*   **Area of the Quarter-Circle ($A_c$):**
    $$A_c = \frac{1}{4} \pi r^2 = \frac{\pi}{4}$$

#### 2. The Probability Ratio
If we randomly scatter $N$ points within the square, the probability $P$ that a point falls inside the quarter-circle is proportional to the ratio of their areas:

$$\frac{\text{Points Inside Circle}}{\text{Total Points}} \approx \frac{A_c}{A_s} = \frac{\pi/4}{1}$$

#### 3. Deriving $\pi$
From the ratio above, we can isolate $\pi$:
$$\pi \approx 4 \times \frac{N_{inside}}{N_{total}}$$

#### 4. The Algorithm
For each random point $(x, y)$ where $0 \le x, y \le 1$:
1. Calculate the distance from the origin: $d = \sqrt{x^2 + y^2}$.
2. If $d \le 1$, the point is **Inside** (using the circle equation $x^2 + y^2 \le r^2$).
3. If $d > 1$, the point is **Outside**.
""")

st.divider() # Adds a nice visual line before the simulation


# --- Sidebar Inputs ---
st.sidebar.header("Simulation Settings")
num_obs = st.sidebar.number_input("How many observations?", min_value=100, max_value=50000, value=1000, step=500)
run_btn = st.sidebar.button("Run Simulation")

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
        fig2, ax2 = plt.subplots(figsize=(5, 5))
        ax2.plot(counts, pi_values, color='black')
        ax2.axhline(y=np.pi, color='green', linestyle='--')
        ax2.set_ylim(2.5, 3.8)
        ax2.set_title(f"Current π ≈ {current_pi:.4f}")
        graph_placeholder.pyplot(fig2)
        plt.close(fig2)
        
        time.sleep(0.05) # Control animation speed

    st.success(f"Final Estimation after {num_obs} points: {current_pi:.6f}")
