from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import User, Group
from .forms import UserModelForm, GroupModelForm


def index(request):
    return render(request, 'apps/base.html')


def users_list(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'apps/users_list.html', context)


def users_detail(request, pk):
    unique_user = get_object_or_404(User, pk=pk)
    context = {
        'unique_user': unique_user
    }
    return render(request, 'apps/users_detail.html', context)


def users_create(request):
    form = UserModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully created new user")
        return redirect('users_list')
    context = {
        'form': form
    }
    return render(request, 'apps/users_create.html', context)


def users_update(request, pk):
    unique_user = get_object_or_404(User, pk=pk)
    form = UserModelForm(request.POST or None,
                         instance=unique_user)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully updated user data")
        return redirect('users_list')
    context = {
        'form': form
    }
    return render(request, 'apps/users_update.html', context)


def users_delete(request, pk):
    unique_user = get_object_or_404(User, pk=pk)
    unique_user.delete()
    messages.success(request, "Successfully deleted user")
    return redirect('users_list')


def groups_list(request):
    groups = Group.objects.all()
    context = {
        'groups': groups
    }
    return render(request, 'apps/groups_list.html', context)


def groups_detail(request, pk):
    unique_group = get_object_or_404(Group, pk=pk)
    context = {
        'unique_group': unique_group
    }
    return render(request, 'apps/groups_detail.html', context)


def groups_create(request):
    form = GroupModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully created new group")
        return redirect('groups_list')
    context = {
        'form': form
    }
    return render(request, 'apps/groups_create.html', context)


def groups_update(request, pk):
    unique_group = get_object_or_404(Group, pk=pk)
    form = GroupModelForm(request.POST or None,
                         instance=unique_group)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully updated group data")
        return redirect('groups_list')
    context = {
        'form': form
    }
    return render(request, 'apps/groups_update.html', context)


def groups_delete(request, pk):
    unique_group = get_object_or_404(Group, pk=pk)
    try:
        unique_group.delete()
        messages.success(request, "Successfully deleted group")
        return redirect('groups_list')
    except:
        messages.warning(request, "Deletion is impossible because the user is assigned to this group")
        return redirect('groups_list')