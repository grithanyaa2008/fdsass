from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task


def register(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():

            return render(request, "todo/register.html", {
                "error": "Username already exists"
            })

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect("/login/")

    return render(request, "todo/register.html")


def user_login(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("/")

        else:

            return render(request, "todo/login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "todo/login.html")


def user_logout(request):

    logout(request)

    return redirect("/login/")


@login_required(login_url="/login/")
def home(request):

    if request.method == "POST":

        title = request.POST["title"]
        category = request.POST["category"]
        task_type = request.POST["task_type"]
        status = request.POST["status"]
        priority = request.POST["priority"]
        due_date = request.POST["due_date"]

        Task.objects.create(
            user=request.user,
            title=title,
            category=category,
            task_type=task_type,
            status=status,
            priority=priority,
            due_date=due_date if due_date else None
        )

        return redirect("/")

    tasks = Task.objects.filter(user=request.user)
    sort = request.GET.get("sort")

    if sort == "newest":
      tasks = tasks.order_by("-id")

    elif sort == "oldest":
      tasks = tasks.order_by("id")

    elif sort == "priority":
      tasks = tasks.order_by("-priority")

    elif sort == "due_date":
        tasks = tasks.order_by("due_date")
    
    search = request.GET.get("search")
    category = request.GET.get("category")
    priority = request.GET.get("priority")
    status = request.GET.get("status")

    if search:
        tasks = tasks.filter(title__icontains=search)

    if category:
        tasks = tasks.filter(category=category)

    if priority:
        tasks = tasks.filter(priority=priority)

    if status:
        tasks = tasks.filter(status=status)

    # STEP 12 - Dashboard statistics

    total_tasks = Task.objects.filter(
        user=request.user
    ).count()

    completed_tasks = Task.objects.filter(
        user=request.user,
        status="Completed"
    ).count()

    in_progress_tasks = Task.objects.filter(
        user=request.user,
        status="In Progress"
    ).count()

    high_priority_tasks = Task.objects.filter(
        user=request.user,
        priority="High"
    ).count()

    return render(request, "todo/home.html", {
        "tasks": tasks,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "in_progress_tasks": in_progress_tasks,
        "high_priority_tasks": high_priority_tasks
    })


@login_required(login_url="/login/")
def complete_task(request, task_id):

    task = Task.objects.get(id=task_id)

    task.completed = True

    task.save()

    return redirect("/")

@login_required(login_url="/login/")
def delete_task(request, task_id):

    task = Task.objects.get(
        id=task_id,
        user=request.user
    )

    task.delete()

    return redirect("/")

@login_required(login_url="/login/")
def edit_task(request, task_id):

    task = Task.objects.get(
    id=task_id,
    user=request.user
)
   

    if request.method == "POST":

        task.title = request.POST["title"]
        task.category = request.POST["category"]
        task.task_type = request.POST["task_type"]
        task.status = request.POST["status"]
        task.priority = request.POST["priority"]

        due_date = request.POST["due_date"]

        task.due_date = due_date if due_date else None

        task.save()

        return redirect("/")

    return render(request, "todo/edit_task.html", {
        "task": task
    })
