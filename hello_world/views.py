from django.http import HttpResponse

def hello_world_view(request):
    file_path = "/tmp/logs"
    # Create the file and write to it
    with open(file_path, "w") as f:
        f.write("This is the first log entry\n")
    with open(file_path, "r") as f:
        content = f.read()
        print("Content of logs file inside container:")
        print(content)
    return HttpResponse("Hello World")