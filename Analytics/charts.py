import matplotlib
matplotlib.use('Agg')   # server environment ke liye important

import matplotlib.pyplot as plt
import os
from django.conf import settings

def create_chart():

    skills = ['Python','Django','OpenCV','AI','Data Analyst']
    level = [90,85,80,75,70]

    plt.figure()
    plt.bar(skills, level)

    chart_dir = os.path.join(settings.BASE_DIR, "static", "charts")
    os.makedirs(chart_dir, exist_ok=True)

    path = os.path.join(chart_dir, "skills.png")

    plt.savefig(path)
    plt.close()

    return "charts/skills.png"