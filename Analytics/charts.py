import matplotlib.pyplot as plt
import os
from django.conf import settings

def create_chart():

    skills = ['Python','Django','OpenCV','AI','Data Analyst']
    level = [90,85,80,75,70]

    plt.figure()
    plt.bar(skills, level)

    path = os.path.join(settings.STATICFILES_DIRS[0],"charts/skills.png")
    plt.savefig(path)
    plt.close()
    return "charts/skills.png"