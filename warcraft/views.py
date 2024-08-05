from django.shortcuts import render, redirect

from warcraft.forms import CinematicForm, MusicForm, ScreenshotForm
from warcraft.models import About, Background, Company, Screenshot, Cinematic, Music, Characters


# Create your views here.


def index(request):
    about = About.objects.filter(pk=1)

    ctx = {
        'about': about,
        'company': About.objects.get(title='company'),
        'background': Background.objects.get(title='company'),
        'elfs': Company.objects.get(title='elfs'),
        'elfs_back': Background.objects.get(title='elfs'),
        'people': Company.objects.get(title='people'),
        'people_back': Background.objects.get(title='people'),
        'undead': Company.objects.get(title='undead'),
        'undead_back': Background.objects.get(title='undead'),
        'orgs': Company.objects.get(title='orgs'),
        'orgs_back': Background.objects.get(title='orgs'),
    }
    return render(request, 'warcraft/index.html', ctx)


def screenshot(request):

    ctx = {
        'screenshots': Screenshot.objects.all(),
    }

    return render(request, 'warcraft/screenshot.html', ctx)


def video(request):

    ctx = {
        'videos': Cinematic.objects.all(),
    }

    return render(request, 'warcraft/video.html', ctx)


def music(request):

    ctx = {
        'musics': Music.objects.all(),
        'chars': Characters.objects.all(),
    }

    return render(request, 'warcraft/music.html', ctx)


def add(request):

    ctx = {
        'vid_form': CinematicForm(),
        'music_form': MusicForm(),
        'screenshot_form': ScreenshotForm(),
    }

    return render(request, 'warcraft/add.html', ctx)


def add_video(request):
    if request.method == "POST":
        form = CinematicForm(request.POST, request.FILES)
        if form.is_valid():
            print(1)
            form.save()

    return redirect('add')


def add_music(request):
    if request.method == "POST":
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return redirect('add')


def add_screenshot(request):
    if request.method == "POST":
        form = ScreenshotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('add')