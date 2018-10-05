from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, Resume, Offer
from .forms import PostForm, CommentForm, ResumeForm, OfferForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'resume/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'resume/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'resume/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'resume/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'resume/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'resume/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def resume_list(request):
    resumes = Resume.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'resume/resume_list.html', {'resumes': resumes})

def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resume/resume_detail.html', {'resume': resume})

@login_required
def resume_new(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.save()
            return redirect('resume_detail', pk=resume.pk)
    else:
        form = ResumeForm()
    return render(request, 'resume/resume_edit.html', {'form': form})

@login_required
def resume_edit(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    if request.method == "POST":
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.save()
            return redirect('resume_detail', pk=resume.pk)
    else:
        form = ResumeForm(instance=resume)
    return render(request, 'resume/resume_edit.html', {'form': form})

@login_required
def resume_draft_list(request):
    resumes = Resume.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'resume/resume_draft_list.html', {'resumes': resumes})

@login_required
def resume_publish(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    resume.publish()
    return redirect('resume_detail', pk=pk)

@login_required
def resume_remove(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    resume.delete()
    return redirect('resume_list')

def add_offer_to_resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    if request.method == "POST":
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.resume = resume
            offer.save()
            return redirect('resume_detail', pk=resume.pk)
    else:
        form = OfferForm()
    return render(request, 'resume/add_offer_to_resume.html', {'form': form})

@login_required
def offer_approve(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    offer.approve()
    return redirect('resume_detail', pk=offer.resume.pk)

@login_required
def offer_remove(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    offer.delete()
    return redirect('resume_detail', pk=offer.resume.pk)
