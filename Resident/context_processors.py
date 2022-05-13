def greet(request):
    greeting = f"{request.user.username}"

    return{
        "greeting" : greet
    }