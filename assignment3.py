import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.animation import FuncAnimation

student_id = 2585070
d1 = 7  # second last digit
d2 = 0  # last digit

k = (d1 + d2) % 4 + 2       # (7 + 0) % 4 + 2 = 5
shift = d1 - d2             # 7 - 0 = 7
n_points = 20 + d1          # 20 + 7 = 27
frame_step = d2 + 1         # 0 + 1 = 1

print(f"Student ID: {student_id}")
print(f"d1: {d1}, d2: {d2}")
print(f"k: {k}, shift: {shift}, n_points: {n_points}, frame_step: {frame_step}")
print("-" * 30)


# Task A1: 2D Line Plot
plt.figure(figsize=(8, 5))
x_a1 = list(range(1, n_points + 1))
y_a1 = [val**2 for val in x_a1]

# Safety checks from Lecture 10
if len(x_a1) == 0 or len(y_a1) == 0:
    print("Error: Data is empty")
elif len(x_a1) != len(y_a1):
    print("Error: Mismatched dimensions")
else:
    plt.plot(x_a1, y_a1)
    plt.title("Task A1: Squared Values (1 to n_points)")
    plt.xlabel("X Values")
    plt.ylabel("X Squared")
    plt.show()

# Task A2: Distribution Plot
data_values = np.random.normal(loc=50, scale=10, size=100)
print("First 10 values of data_values:", data_values[:10])

plt.figure(figsize=(8, 5))
# Using Seaborn style from Lecture 10
sns.kdeplot(data_values, color='green', fill=True, bw_adjust=0.5)
plt.title("Task A2: Distribution of Repeated Measurements")
plt.xlabel("Measurement Value")
plt.ylabel("Density")

plt.show()



# Task B1: Personalized 2D Plot
plt.figure(figsize=(8, 5))
# y2 = k * x + shift
y2_b1 = [k * val + shift for val in x_a1]

# Print first 5 (x, y2) pairs for verification
print("First 5 (x, y2) pairs:", list(zip(x_a1, y2_b1))[:5])

plt.plot(x_a1, y2_b1, marker='o', linestyle='--', color='red') # Different style from A1
plt.title(f"Task B1: ID {student_id} (k={k}, shift={shift})")
plt.xlabel("X Values")
plt.ylabel("Y2 Values (Linear)")
plt.show()

# Task B2: Personalized 3D Scatter Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

x_b2 = np.array(range(1, n_points + 1))
y_b2 = x_b2 + shift
z_b2 = k * x_b2

# Debugging print
print("First 5 (x, y, z) points:", list(zip(x_b2, y_b2, z_b2))[:5])

ax.scatter(x_b2, y_b2, z_b2, c='blue', marker='^')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label (X + Shift)')
ax.set_zlabel('Z Label (k * X)')
ax.set_title("Task B2: Personalized 3D Scatter")
plt.show()

# Task B3: Personalized Animation
fig_anim, ax_anim = plt.subplots(figsize=(8, 5))
x_anim_data = np.arange(0, n_points)
y_anim_data = k * x_anim_data + shift

line, = ax_anim.plot([], [], lw=2, color='purple')

def init():
    ax_anim.set_xlim(0, n_points)
    ax_anim.set_ylim(min(y_anim_data) - 5, max(y_anim_data) + 5)
    return line,

def update(frame):
    # Reveal graph gradually: advance by frame_step
    current_idx = frame * frame_step
    line.set_data(x_anim_data[:current_idx], y_anim_data[:current_idx])
    
    # Required debug output
    if frame < 5:  # Print for at least a few frames
        print(f"Animating frame: {frame}")
    
    return line,

# Number of frames is determined by total points / step
total_frames = int(n_points / frame_step) + 1

ani = FuncAnimation(fig_anim, update, frames=total_frames,
                    init_func=init, blit=True, repeat=False)

plt.title("Task B3: Gradual Linear Reveal")
plt.show()