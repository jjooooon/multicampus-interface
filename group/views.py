from django.shortcuts import render, redirect, get_object_or_404
from .models import Recruit, Applicant, Comment
from django.utils import timezone
from .forms import RecruitForm, ApplicantForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    page = request.GET.get('page', '1')
    recruit_list = Recruit.objects.order_by('-create_date')
    paginator = Paginator(recruit_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'recruit_list' :   page_obj}
    return render(request, 'group/recruit_list.html', context)

def detail(request, recruit_id):
    recruit = Recruit.objects.get(id=recruit_id)
    context = {'recruit' : recruit }
    return render(request, 'group/recruit_detail.html', context)


@login_required(login_url='users:login')
def answer_create(request, recruit_id):
    recruit = Recruit.objects.get(id=recruit_id)
    if request.method == "POST":
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.author = request.user
            applicant.create_date = timezone.now()
            applicant.question = recruit
            applicant.save()
            return redirect('group:detail', recruit_id=recruit.id)
    else:
        form =ApplicantForm()
    context = {'recruit': recruit, 'form': form}
    return render(request, 'group/recruit_detail.html', context)


@login_required(login_url='users:login')
def recruit_create(request):
    if request.method == 'POST':
        form = RecruitForm(request.POST)
        if form.is_valid():
            recruit = form.save(commit=False)
            recruit.author = request.user
            recruit.create_date = timezone.now()
            recruit.save()
            return redirect('group:index')
    else:
        form = RecruitForm()
    context = {'form' : form}
    return render(request, 'group/recruit_form.html', context )




@login_required(login_url='users:login')
def recruit_modify(request, recruit_id):
    recruit = get_object_or_404(Recruit, pk=recruit_id)
    if request.method == "POST":
        form = RecruitForm(request.POST, instance=recruit)
        if form.is_valid():
            recruit = form.save(commit=False)
            recruit.modify_date = timezone.now()  # 수정일시 저장
            recruit.save()
            return redirect('group:detail', recruit_id=recruit.id)
    else:
        form = RecruitForm(instance=recruit)
    context = {'form': form}
    return render(request, 'group/recruit_form.html', context )


@login_required(login_url='users:login')
def recruit_delete(request, recruit_id):
    recruit = get_object_or_404(Recruit, pk=recruit_id)
    if request.user != recruit.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('group:detail', recruit_id=recruit.id)
    recruit.delete()
    return redirect('group:index')



@login_required(login_url='users:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Applicant, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('group:detail', recruit_id=answer.question.id)

    if request.method == "POST":
        form = ApplicantForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('group:detail', recruit_id=answer.question.id)
    else:
        form = ApplicantForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'group/answer_form.html', context)


@login_required(login_url='users:login')
def answer_delete(request, answer_id):

    answer = get_object_or_404(Applicant, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('group:detail', recruit_id=answer.question.id)


@login_required(login_url='users:login')
def comment_create_question(request, recruit_id):
    recruit = get_object_or_404(Recruit, pk=recruit_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = recruit
            comment.save()
            return redirect('group:detail', recruit_id=recruit.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'group/comment_form.html', context)


@login_required(login_url='users:login')
def comment_modify_question(request, comment_id):
    """
    pybo 질문댓글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('group:detail', recruit_id=comment.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('group:detail', recruit_id=comment.question.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'group/comment_form.html', context)


@login_required(login_url='users:login')
def comment_delete_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('group:detail', recruit_id=comment.question.id)
    else:
        comment.delete()
    return redirect('group:detail', recruit_id=comment.question.id)


@login_required(login_url='users:login')
def comment_create_answer(request, answer_id):

    answer = get_object_or_404(Applicant, pk=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('group:detail', recruit_id=comment.answer.question.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'group/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    """
    pybo 답글댓글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('pybo:detail', recruit_id=comment.answer.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('group:detail', recruit_id=comment.answer.question.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'group/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('group:detail', recruit_id=comment.answer.question.id)
    else:
        comment.delete()
    return redirect('group:detail', recruit_id=comment.answer.question.id)