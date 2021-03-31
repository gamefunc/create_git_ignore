import os, sys, re

folder = os.path.dirname(__file__)


# 不加入.gitignore的后缀名:
accept_extensions = [
    # c:
    "c", "cc", "cpp", "cxx", "h",
    "hpp", "cmake", "ui",
    # py:
    "py", "vpy", "PY", "pth", 
    # java:
    "java", "classpath", "gradle", "iml",
    # go:
    "go",
    # kotlin:
    "kt", "class", 
    # web:
    "js", "html", "css", "php",
    # office:
    "doc", "docx", "ppt", "pptx", "pub", 
    # db:
    "db", "accdb",
    # other:
    "txt", "xml", "bat", "sh", "properties", "json",
    "conf", "dnsmasq", "log"
]


# 会以: **/.git\n 优先写入到.gitignore的行:
priority_lines = [
    "**/.git",
    "**/build",
    "**/.idea",
    "**/app/build",
    "**/app/.cxx",
    "/build",
    "/.idea",
    "/app/build",
    "/app/.cxx"
]

# 会以: *.ico\n 写入.gitignore的后缀名:
ignore_extensions = [
    "ico", "msi", "user", "service", 
    "rsp", "in", "bin", "make", "ac", "cer", 
    "local", "so", "npz", "key", "sln", "lib", "md", "rar", "i", "o", "ijg", 
    "wav", "m4", "jpg", "pdf", "exe", "marks", "png", "ipch", "build", "dll", 
    "zip", "check_cache", "depend", "qrc", "s", "bmp", "pcm", "ver", "vcxproj", 
    "ppm", "filters", "gif", "rule", "pem", "recipe", "xsd", "webp", 
    "jar", "lastbuildstate", "pb", "jfif", "下载", "pyc", "obj", "pcap", 
    "mak2", "mak", "stamp", "tlog", "list", "am", "whl", "ffpreset"]


def search(folder_abs_path: str):
    """
    递归查找所有需要忽略的后缀名;
    """
    for fobj in os.scandir(folder_abs_path):
        if fobj.is_dir():
            search(fobj.path)
            continue
        
        if "." not in fobj.name:
            continue
        
        extension = fobj.name.rsplit(".", 1)[-1]
        if extension in accept_extensions:
            continue
        if extension not in ignore_extensions:
            ignore_extensions.append(extension)


def write_to_gitignore():
    """
    写入.gitignore文件;
    """
    gitignore_out_path = os.path.join(
        folder, ".gitignore")
    with open(gitignore_out_path, "wb") as f:
        for line in priority_lines:
            f.write(f"{line}\n".encode("utf-8"))
            print(line)
        for ext in ignore_extensions:
            f.write(f"*.{ext}\n".encode("utf-8"))
            print(ext)
        

search(folder)
write_to_gitignore()
os.system("pause")

