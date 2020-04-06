from django.shortcuts import render

from .models import Resume

# Create your views here.
def resume(request):
    """Страница с резюме(Resume)"""
    resume = Resume.objects.all
    context = {'resumes': resume}
    return render(request, 'resume/resume.html', context)