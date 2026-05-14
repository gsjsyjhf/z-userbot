import os, sys, struct, urllib.request, tarfile

REPO = "https://raw.githubusercontent.com/gsjsyjhf/z-userbot/main"
VERSION_URL = f"{REPO}/version.json"

def get_arch():
    bits = struct.calcsize("P") * 8
    machine = os.uname().machine.lower()
    if "arm" in machine or "aarch" in machine:
        return "arm64"
    return "x86_64"

def ensure_modules():
    arch = get_arch()
    mod_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "modules")
    flag = os.path.join(mod_dir, f".{arch}")
    if os.path.isfile(flag):
        return mod_dir
    os.makedirs(mod_dir, exist_ok=True)
    archive = f"modules_{arch}.tar.gz"
    url = f"{REPO}/{archive}"
    tmp = os.path.join(mod_dir, archive)
    print(f"⬇️ تحميل الوحدات ({arch})...")
    urllib.request.urlretrieve(url, tmp)
    with tarfile.open(tmp, "r:gz") as t:
        t.extractall(mod_dir)
    os.remove(tmp)
    open(flag, "w").close()
    return mod_dir

if __name__ == "__main__":
    mod = ensure_modules()
    sys.path.insert(0, mod)
    from loader import run
    run()
