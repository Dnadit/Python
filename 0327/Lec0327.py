import matplotlib.pyplot as plt
import numpy as np

# 색상 변경 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='#FF5733')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
