import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(5, 6))
ax.set_xlim(-110, 110)
ax.set_ylim(-80, 160)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('white')

GREEN = '#3DDC84'

# ---- HEAD (half circle) ----
head = mpatches.Wedge(
    center=(0, 60), r=60,
    theta1=0, theta2=180,
    facecolor=GREEN, edgecolor='none'
)
ax.add_patch(head)

# ---- EYES ----
ax.add_patch(mpatches.Circle((-20, 75), 6, facecolor='white'))
ax.add_patch(mpatches.Circle((20, 75), 6, facecolor='white'))

# ---- ANTENNAS ----
antenna_props = dict(color=GREEN, linewidth=5, solid_capstyle='round')
# Left antenna (tilted left)
ax.plot([-30, -55], [115, 138], **antenna_props)
ax.add_patch(mpatches.Circle((-55, 138), 5, facecolor=GREEN))
# Right antenna (tilted right)
ax.plot([30, 55], [115, 138], **antenna_props)
ax.add_patch(mpatches.Circle((55, 138), 5, facecolor=GREEN))

# ---- BODY ----
body = mpatches.FancyBboxPatch(
    (-65, -40), 130, 100,
    boxstyle="round,pad=0,rounding_size=20",
    facecolor=GREEN, edgecolor='none'
)
ax.add_patch(body)

# ---- ARMS ----
left_arm = mpatches.FancyBboxPatch(
    (-100, -35), 30, 80,
    boxstyle="round,pad=0,rounding_size=14",
    facecolor=GREEN, edgecolor='none'
)
ax.add_patch(left_arm)

right_arm = mpatches.FancyBboxPatch(
    (70, -35), 30, 80,
    boxstyle="round,pad=0,rounding_size=14",
    facecolor=GREEN, edgecolor='none'
)
ax.add_patch(right_arm)

# ---- LEGS ----
left_leg = mpatches.FancyBboxPatch(
    (-58, -90), 35, 60,
    boxstyle="round,pad=0,rounding_size=14",
    facecolor=GREEN, edgecolor='none'
)
ax.add_patch(left_leg)

right_leg = mpatches.FancyBboxPatch(
    (23, -90), 35, 60,
    boxstyle="round,pad=0,rounding_size=14",
    facecolor=GREEN, edgecolor='none'
)
ax.add_patch(right_leg)

# ---- BODY DIVIDER LINE (between chest panels) ----
ax.plot([0, 0], [-38, 58], color='white', linewidth=3, alpha=0.4)

plt.tight_layout()
plt.savefig('android_logo.png', dpi=150, bbox_inches='tight')
plt.show()