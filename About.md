# 🧮 Monte Carlo Simulation: Estimating π

An interactive web application that uses a stochastic **Monte Carlo method** to approximate the value of $\pi$ through random sampling and geometric probability.

## 🚀 Live Demo
**Click here to run the simulation in your browser:**  
👉 [**Monte Carlo Pi Estimator**](https://montecarlosimulationpi-mzappmoyflghurm3wjgjclr.streamlit.app/)

---

## 📖 The Theory

The Monte Carlo method is a mathematical technique used to estimate numerical results by using repeated random sampling. To find $\pi$, we use the relationship between a **unit square** and an **inscribed quarter-circle**.

### 1. Geometric Model
Imagine a square with a side length of $r = 1$. Inside this square, we draw a quarter-circle with a radius of $r = 1$.

*   **Area of the Square ($A_{square}$):** 
    $$A_s = r^2 = 1 \times 1 = 1$$
*   **Area of the Quarter-Circle ($A_{circle}$):** 
    $$A_c = \frac{1}{4} \pi r^2 = \frac{\pi}{4}$$

### 2. The Probability Ratio
If we randomly scatter $N$ points within the square, the probability ($P$) that a point lands inside the circle is equal to the ratio of the area of the circle to the area of the square:

$$\frac{\text{Points Inside Circle}}{\text{Total Points}} \approx \frac{\text{Area of Circle}}{\text{Area of Square}}$$

$$\frac{N_{in}}{N_{total}} \approx \frac{\pi / 4}{1}$$

### 3. Calculating π
By rearranging the formula, we can estimate $\pi$ using only the counts of our random points:

$$\pi \approx 4 \times \frac{N_{in}}{N_{total}}$$

---

## 🛠️ How it Works
The simulation follows these steps:
1.  **Generate** a random coordinate $(x, y)$ where $0 \le x, y \le 1$.
2.  **Calculate** the distance from the origin $(0,0)$ using the Pythagorean theorem: $d = \sqrt{x^2 + y^2}$.
3.  **Classify**: 
    *   If $d \le 1$, the point is **inside** the circle.
    *   If $d > 1$, the point is **outside** the circle.
4.  **Update**: Recalculate the estimate of $\pi$ after every new batch of points to show convergence.

---

## 💻 Tech Stack
- **Python 3.10**
- **Streamlit**: For the interactive web interface.
- **Matplotlib**: For real-time data visualization.
- **NumPy**: For high-performance random number generation.

---

## 👨‍💻 Author
**Nishani53**  
Check out my other projects on [GitHub](https://github.com).
