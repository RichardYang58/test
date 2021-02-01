class IO:
    supportedSrcs=["console","file"]
    def read(src):
        print("read from",src)

print(IO.supportedSrcs)
IO.read("file")
